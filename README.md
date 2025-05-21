# VROOM für QGIS Plugin

This QGIS plugin connects QGIS and VROOM (Vehicle Routing Open-source Optimization Machine). VROOM is an open-source optimization engine to solve vehicle routing problems (VRP). For information regarding the capabilities and how to set up VROOM, please refer to [the project's GitHub page](https://github.com/VROOM-Project/vroom). This independent plugin is not affiliated with either VROOM or QGIS or any other project.

The plugin makes it possible to set up the problem (vehicles, pickups and deliveries) as QGIS layers with fields for all the relevant features (e.&nbsp;g. time windows). The Plugin wraps the data into a JSON and sends it to a running instance of [VROOM Express](https://github.com/VROOM-Project/vroom-express), transforming the result into QGIS layers again. Currently just the use of PDPTW (pickup-and-delivery problem with time windows) is implemented, no classical TSP or VRP wth jobs to be handled in one location.

## Steps before using this plugin

In the current version there are two supported ways to use the plugin: Either set up VROOM locally to access it via localhost or use the [Openrouteservice](https://openrouteservice.org/) [Optimization API](https://openrouteservice.org/dev/#/api-docs/optimization). To achive the first:

1. Set up a local routing engine: [OSRM](https://github.com/Project-OSRM/osrm-backend), [Openrouteservice](https://github.com/GIScience/openrouteservice) or [Valhalla](https://github.com/valhalla/valhalla)
2. Set up [VROOM](https://github.com/VROOM-Project/vroom) and [VROOM Express](https://github.com/VROOM-Project/vroom-express) locally
3. Use the port number of the running VROOM Express instance (normally 3000) in the plugin (see usage below)

To achieve the latter:
1. Go to https://openrouteservice.org/, create an account and get an API key
2. Use the API key in the plugin (see usage below)

Keep in mind that ORS is subject to [API limits](https://openrouteservice.org/restrictions/).

## Usage of the plugin

Download this repository and [zip](https://en.wikipedia.org/wiki/ZIP_(file_format)) it. Use the [Install from ZIP](https://docs.qgis.org/3.40/en/docs/user_manual/plugins/plugins.html#the-install-from-zip-tab) function to install the plugin. Afterwards you will find it in the [Processing Toolbox](https://docs.qgis.org/3.40/en/docs/user_manual/processing/toolbox.html). After opening it, you will find a window with some options.

Most Options refer to [features of the VROOM API](https://github.com/VROOM-Project/vroom/blob/master/docs/API.md). In the following list of options the feature's names are `written like code`. If the name is written in [`brackets`], the values have to be stored in an array. Since there is no way to have array fields in QGIS, you have to create string fields for this values and write the values in brackets, like `[100]` for a capacity of 100 of one kind or `[[0,600],[1200,1800]]` for a time window of two parts from 0 to 600 seconds and 1200 to 1800 seconds:


| Option | Description |
|--------|-------------|
| Use Openrouteservice (ORS) for routes | Tick it, if you are using ORS as the routing engine for VROOM or the ORS Optimization API. |
| Use ORS optimization API | Tick it, if you are using the ORS optimization API. |
| Key for ORS optimization API | Put your ORS API key here. |
| Travel mode for ORS | Select your preferred travel mode for ORS here. If you are using OSRM or Valhalla, it has no effect. |
| Port number of running Vroom Express | Put the port number (normally 3000) here. If you are using the ORS optimization API, this has no effect. |
| Layer with vehicle points | Select the layer, where the depot positions and features of your vehicles are stored. |
| Start from Depot | Set to true, if vehicles shall start at their respective depot location. If not, they will start at the location of their first job. |
| Return to Depot | Set to true, if vehicles shall end at their respective depot location. If not, they will end at the location of their last job. |
| Field for capacity array of vehicles | Select the field of the vehicle layer, where the vehicle [`capacity`] array is stored. |
| Field for description of vehicles | Select the field of the vehicle layer, where the vehicle `description` is stored. |
| Field for skill array of vehicles | Select the field of the vehicle layer, where the vehicle [`skills`] array is stored. |
| Field for time window arrays of vehicles (in seconds) | Select the field of the vehicle layer, where the vehicle [[`time windows`]] array is stored. |
| speed factor in the range (0, 5] (default 1), precision is two decimal points | Select the field of the vehicle layer, where the vehicle `speed factor` is stored. |
| Field for maximum number of tasks of vehicle | Select the field of the vehicle layer, where the vehicle `max_tasks` is stored. |
| Field for maximum travel time (in seconds) | Select the field of the vehicle layer, where the vehicle `max_travel_time` is stored. |
| Field for maximum distance in meters | Select the field of the vehicle layer, where the vehicle `max_distance` is stored. |
| Field for array of break objects | Select the field of the vehicle layer, where the vehicle [[`breaks`]] objects array is stored. |
| Layer with pickup points | Select the layer, where the positions and features of your pickup points are stored. |
| Start ID Field | Select an id field, which connects the pickup points to the corresponding delivery points. |
| Field for amount array | Select the field of the pickup layer, where the [`amount`] array for the shipment is stored. |
| Field for skills array | Select the field of the pickup layer, where the [`skills`] array for the shipment is stored. |
| Field for pickup description | Select the field of the pickup layer, where the `description` of pickup points is stored. |
| Field for priority of shipment (number from 0 to 100) | Select the field of the pickup layer, where the [`priority`] array for the shipment is stored. |
| Field for setup duration of pickup (in seconds) | Select the field of the pickup layer, where the `setup` duration for pickup is stored. |
| Field for service duration of pickup (in seconds) | Select the field of the pickup layer, where the `service` duration for pickup is stored. |
| Field for time windows array of pickup (in seconds) | Select the field of the pickup layer, where the [[`time windows`]] array for pickup is stored. |
| Layer with delivery points | Select the layer, where the positions and features of your delivery points are stored. |
| End ID Field | Select an id field, which connects the delivery points to the corresponding pickup points. |
| Field description of delivery (in seconds)| Select the field of the delivery layer, where the `description` of delivery points is stored. |
| Field for setup duration of delivery  (in seconds)| Select the field of the delivery layer, where the `setup` duration for delivery is stored. |
| Field for service duration of delivery  (in seconds)| Select the field of the delivery layer, where the `service` duration for delivery is stored. |
| Field for time windows array of delivery (in seconds) | Select the field of the delivery layer, where the [[`time windows`]] array for delivery is stored. |








