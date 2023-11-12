# AQM-SENSOR-CLIENT
**This software is running on Raspberry Pi**

### Area Of Responsibility
* Retrieve data from connected sensor
* During measurement save timestamp to associate it with retrieved data
* Send data and timestamp to [backend](https://github.com/DAWN-LV/aqm-backend) queue for processing
* Send status response whenever [backend](https://github.com/DAWN-LV/aqm-backend) send a request to **Raspberry Pi**

## Setup
**Clone Repository**
```bash
git clone https://github.com/PepeWarrior69/aqm-sensor-client.git
```
```bash
cd aqm-sensor-client
```
**Install Dependencies**
```bash
pip3 install -e
```

## Configuration
**Create .env file in the root and setup desired values**
```bash
BACKEND_IP=127.0.0.1
BACKEND_PORT=5000
MEASUREMENT_FREQUENCY_MS=10000
```
