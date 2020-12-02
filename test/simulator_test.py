import sys
sys.path.append(".")
import unittest
from unittest.mock import MagicMock
from src.simulator import Simulator
import geopandas as gpd
import pandas as pd
# sys.modules['geopandas'] = Mock()

class TestSimulator(unittest.TestCase):
            
    def test_get_booking_distance_bins(self):
        number = 10
        bounding_box = (13.34014892578125, 52.52791908000258, 13.506317138671875, 52.562995039558004)
        instance = Simulator(bounding_box);
        response = Simulator.get_booking_distance_bins(instance, number);
        actualSum=sum(response.values())
        self.assertEqual(actualSum,number)
    
    def test_simulate(self):
    #     df = pd.DataFrame(
    #     {'City': ['Berlin', 'MUnich'],
    #  'Country': ['Germany', 'Germany'],
    #  'Latitude': [12.34014892578125, 11.52791908000258],
    #  'Longitude': [50.506317138671875, 51.562995039558004]});
    #     gdf = gpd.GeoDataFrame(
    #     df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude));
    #     gpd.read_file = MagicMock(return_value=gdf);
    #     number = 100
    #     bounding_box = (10.34014892578125, 50.52791908000258, 12.506317138671875, 49.562995039558004)
    #     instance = Simulator(bounding_box);
    #     actual = Simulator.simulate(instance, number);
    #     print(actual);
    #      #  assert
        
if __name__ == '__main__':
    unittest.main()