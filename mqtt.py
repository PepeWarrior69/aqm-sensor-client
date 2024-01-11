from socket import socket
import uuid
import paho.mqtt.client as mqtt
from time import sleep
from config.config import PLATFORM, ENDPOINT_URL, MQTT
from AppWrapper import AppWrapper


app_wrapper = AppWrapper()
MAC = app_wrapper.sensor_app.platform_context.strategy.mac
TOPIC_BASE = f'sensor/{MAC}'

client = mqtt.Client(
    client_id=f'{MAC}_{str(uuid.uuid4())[0:8]}',
    clean_session=True
)

last_known_endpoint = ENDPOINT_URL
platform = PLATFORM

def get_app_meta():
    internal_ip = app_wrapper.sensor_app.platform_context.strategy.internal_ip
    external_ip = app_wrapper.sensor_app.platform_context.strategy.external_ip
    return f'{platform}|{last_known_endpoint}|{app_wrapper.state}|{internal_ip}|{external_ip}'

def send_app_meta():
    meta = get_app_meta()
    print(f'Attempt send {meta=}')
    try:
        res = client.publish(f'{TOPIC_BASE}/meta', meta)
        print('res = ', res)
    except Exception as err:
        print(f'Error during publish meta: err = ', err)

def handle_app_init(payload: str):
    if app_wrapper.state == 'ACTIVE':
        return

    args = payload.split("|") # 0 = endpoint; 1 = platform
    print('args = ', args)
    last_known_endpoint = args[0]
    platform = args[1]
    app_wrapper.start(last_known_endpoint, platform)
    # client.publish(f'{TOPIC_BASE}/status', app_wrapper.state)
    send_app_meta()
    

def handle_app_restart():
    app_wrapper.stop()
    app_wrapper.start(last_known_endpoint, platform)
    # client.publish(f'{TOPIC_BASE}/status', app_wrapper.state)
    send_app_meta()

def handle_app_deinit():
    app_wrapper.stop()
    # client.publish(f'{TOPIC_BASE}/status', app_wrapper.state)
    send_app_meta()


def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK Returned code=", rc)
    else:
        print("Bad connection Returned code=", rc)
        
def on_connect_fail(client, userdata, flags, rc):
    print(f'[on_connect_fail] {flags=} {rc=}')
    
def on_disconnect(client, userdata, rc):
    print(f'[on_disconnect] {rc=}')

# def on_log(*args):
#     print('[on_log] on_log: ', args)

def on_socket_open(client, userdata, socket: socket):
    print(f'[on_socket_open] socket={socket.getsockname()} peer={socket.getpeername()}')

def on_socket_close(client, userdata, socket: socket):
    print(f'[on_socket_close] socket={socket.getsockname()} peer={socket.getpeername()}')

def on_subscribe(client, userdata, flags, rc):
    print(f'[on_subscribe] {flags=} {rc=}')

def on_unsubscribe(client, userdata, flags, rc):
    print(f'[on_unsubscribe] {flags=} {rc=}')
        
# Callback when a message is received from the broker
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    
    if msg.topic == f'{TOPIC_BASE}/init':
        handle_app_init(msg.payload.decode())
    elif msg.topic == f'{TOPIC_BASE}/restart':
        handle_app_restart()
    elif msg.topic == f'{TOPIC_BASE}/deinit':
        handle_app_deinit()
        
client.on_connect = on_connect
client.on_message = on_message
client.on_connect_fail = on_connect_fail
client.on_disconnect = on_disconnect
# client.on_log = on_log
client.on_socket_open = on_socket_open
client.on_socket_close = on_socket_close
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe

try:
    res = client.connect(
        host=MQTT["HOST"],
        port=MQTT["PORT"],
        keepalive=MQTT["KEEPALIVE"]
    )
    
    client.subscribe(f'{TOPIC_BASE}/init')
    client.subscribe(f'{TOPIC_BASE}/restart')
    client.subscribe(f'{TOPIC_BASE}/deinit')
    
    client.loop_start()
    
    count = 0
    
    while True:
        sleep(10)
        is_connected = client.is_connected()
        
        if not is_connected:
            print("Attempt MQTT reconnect")
            reconn_res = client.reconnect()
            print("Reconnection response: ", reconn_res)
        
        count += 1
            
        if count >= 60:
            # send metadata every 10 minutes
            send_app_meta()
            count = 0
        
except Exception as err:
    client.loop_stop()
    print(err)
