from service import BackgroundScheduleService, HttpService
import time
import argparse

def bg_handler():
    print('bg_handler run in background')
    http = HttpService('http://40.68.14.121:3000/api/sensors/test', 3000)
    http.post({ "id": "bruh", "mac": "asdadadasdasdasdasda", "hello": "world" })

def main():
    parser = argparse.ArgumentParser(description='Example script with named arguments')
    # Add a named argument for the platform
    parser.add_argument('--platform', type=str, help='Specify the platform (e.g., raspberry, pc, arduino)')
    args = parser.parse_args()
    
    print("args = ", args) # get platform parameter
    
    bgSchedule = BackgroundScheduleService()
    id = bgSchedule.add_background_job(bg_handler, 5)
    print("id = ", id)
    bgSchedule.start(id)
    
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

