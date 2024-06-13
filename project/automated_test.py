import unittest
import os
from pipeline import download_and_transform_dataset1, download_and_transform_dataset2

class TestPipeline(unittest.TestCase):

    def setUp(self):
        # Set up the test directories and database paths
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Moves up two levels from current script's directory
        data_dir = os.path.join(base_dir, 'data')
        self.project_dir = os.path.join(base_dir, 'project')
        self.forest_data_path = os.path.join(data_dir, 'world_forest_data.sqlite')
        self.climate_insight_data_path = os.path.join(data_dir, 'global_climate_insight_data.sqlite')


    def test_download_and_transform_dataset1(self):
        # Call the function from pipeline.py
        forest_data_url = 'https://www.kaggle.com/api/v1/datasets/download/webdevbadger/world-forest-area'
        download_and_transform_dataset1(forest_data_url, os.path.join(self.project_dir, 'forest_data'), self.forest_data_path)

        # Validate that the output SQLite file exists
        self.assertTrue(os.path.exists(self.forest_data_path), "world_forest_data.sqlite does not exist")

    def test_download_and_transform_dataset2(self):
        # Call the function from pipeline.py
        climate_insight_data_url = 'https://www.kaggle.com/api/v1/datasets/download/goyaladi/climate-insights-dataset?datasetVersionNumber=4'
        download_and_transform_dataset2(climate_insight_data_url, os.path.join(self.project_dir, 'climate_insight_data'), self.climate_insight_data_path)

        # Validate that the output SQLite file exists
        self.assertTrue(os.path.exists(self.climate_insight_data_path), "global_climate_insight_data.sqlite does not exist")


if __name__ == '__main__':
    unittest.main()