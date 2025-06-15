# ShellyPlusPlugS_Logger
This is a Tool that enables the user to log MQTT messages of a Shelly Plus Plug S in a csv file.

## Background
The main idea to this Repository was a question of my unclce. He likes to go camping an had the following question: I would like to buy a power station to power my caravan for a short time (e.g. 2 hours) when no power outlet is availabe. How much current and how many kilowatt hours does the power station has to deliver? The caravan has a refrigerator, a coffee maker, an electric water pumpt, lights, etc. He asked me if there is a way to measure the current to have an idea what power station he should order. <br>
As I had a Shelly Plus Plug S, a Login at HiveMQ and a Server at home that can listen to messages from the Broker, this seemed to be an easy way, as it only needs a Wifi network available (created by Teethering or Hotspot by a Smartphone) for the Shelly Plug that is near to the caravan. 




## Thing that are handeled in this Tool:
- Installing all needed Python components to be able to run the script.
- Creating a cost free login at HiveMQ a public available MQTT Broker. 
- Setting envico
