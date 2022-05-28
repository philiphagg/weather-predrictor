# IoT-Device Documentation
The Raspberry Pi Model B+ is connected to a BME680 sensor which can read temperature, air pressure, humidity and gasses. In our project we are not in need of the gas-readings. In our prediction model we are only interested in the first three mentioned. The Pi uses a python script to do all te actions needed. The libraries in the script are the BME680 library, time for setting a timeout, datetime for the timestamp and an azure library for uploading the data to the cloud. The device is connected to cloud via an Azure IoT-hub. The data uploaded to the IoT-hub is then fetched as an input to a Stream Analytics Job which takes the input and sends it to the SQL Database so that it can fetched for the web-app and the machine learning. 

## Step by step testing
The first step once the Raspberry Pi is up and running, has the I2C open for reading,  and the sensor is connected to the GPIO ports, is to check that the device can recognise the sensor on the right I2C-address. This is done through either a terminal command or via the sensor library in python which has the possible addresses as values( for example I2C_ADDR_PRIMARY). 
Once we can initialize an instance of the sensor in python we can test the data coming from the sensor by printing it to the terminal. Once we verify that the data is somewhat close to reality we can move on. 
The next step is initializing a connection to the Azure IoT hub, which is done through the Azure IoT device library. For this test we need the connection string provided by the IoT hub. To monitor the results we can make a try and catch statement in the script or just look at the terminal whether an error is returned by the library-function. Once a connection is established we can monitor the end points of the IoT hub via the stream analytics job or the VSCode Azure extension. Here we can also verify that the messages are in the right format, CSV. Once all of these steps are verified the IoT device works as intended and we can position it in the right position and boot it up again for the final release. 
