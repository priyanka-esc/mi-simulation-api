# mi-simulation-api
This module ```(mainClass.py)``` provides an API(GET method) that returns some mock simulation results. It does not actually simulate any services, etc, but it should be used as if it did.

##Setup
Initialize a virtual environment and install the requirements in requirements.txt.
Run ```mainClass.py``` which starts a server(ideally on port 5000, but can verify on the console when it starts).

##Usage
This API is a get call with minLtitude, maxLatitude, minLongitude, maxLongitude as mandatory query parameters. 
requestCount parameter is where number_of_requests is the number of requests to our Ridepooling service to "simulate".If not provided, default value of 2 is taken.
Example : http://localhost:5000/v2/simulator?minLatitude=13.34014892578125&maxLatitude=52.52791908000258&minLongitude=13.506317138671875&maxLongitude=52.562995039558004&requestCount=500

##Output
The result we get is a json that looks like the following:

Key	Type	Description
booking_distance_bins	json	How many bookings happened for every "kilometer bin". E.g. how many bookings had a distance between 0 and 1km, 1 and 2kms, etc.
most_popular_dropoff_points	String (valid .geojson)	Which points within the simulated bounding box were the most popular dropoff points.
most_popular_pickup_points	String (valid .geojson)	Which points within the simulated bounding box were the most popular pickup points.
