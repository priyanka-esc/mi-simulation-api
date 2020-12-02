import geopandas as gpd
from shapely.geometry import box

class Simulator:
    booking_distance_distribution = [0.2, 0.1, 0.3, 0.4]
    max_popular_points = 10
    path_to_stops = '../resources/berlin_stops.geojson'

    def __init__(self, bounding_box):
        self.bounding_box = bounding_box

    def simulate(self, number_of_requests):
        booking_distance_bins = self.get_booking_distance_bins(
            number_of_requests)
        number_of_sample_points = min(
            number_of_requests, self.max_popular_points)
        most_popular_dropoff_points = self.get_random_points(
            number_of_sample_points)
        most_popular_pickup_points = self.get_random_points(
            number_of_sample_points)

        return {
            'booking_distance_bins': booking_distance_bins,
            'most_popular_dropoff_points': most_popular_dropoff_points,
            'most_popular_pickup_points': most_popular_pickup_points
        }

    def get_booking_distance_bins(self, number_of_requests):
        return {
            f'From {i}->{i+1}km': round(number_of_requests * x)
            for i, x in enumerate(self.booking_distance_distribution)}

    def get_random_points(self, n):
        bounding_box_shape = box(*self.bounding_box)
        print(bounding_box_shape.exterior.coords);
        geodataframe = gpd.read_file(self.path_to_stops)
        print('printing gdf')
        print(geodataframe.head())
        within_bounds = geodataframe[geodataframe.within(bounding_box_shape)]
        return within_bounds.sample(n).to_json()

def getSimulations(minLatitude, maxLatitude,minLongitude,maxLongitude, requestCount=2):
    # bounding_box = (13.34014892578125, 52.52791908000258, 13.506317138671875, 52.562995039558004)
    bounding_box = (minLatitude, maxLatitude,minLongitude,maxLongitude);
    simulator1 = Simulator(bounding_box)
    return simulator1.simulate(requestCount)


# __package__ = simulator
if __name__ == "__main__":
    import set_package_attribute
    set_package_attribute.init()