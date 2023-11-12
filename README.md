# AQM-SENSOR-CLIENT

**This software is running on Raspberry Pi**

### Area Of Responsibility
* Retrieve data from connected sensor
* During measurement save timestamp to associate it with retrieved data
* Send data and timestamp to [backend](https://github.com/DAWN-LV/aqm-backend) queue for processing
* Send status response whenever [backend](https://github.com/DAWN-LV/aqm-backend) send a request to **Raspberry Pi**
