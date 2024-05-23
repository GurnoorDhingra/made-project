import os
import pandas as pd
import requests
import zipfile
import sqlite3
import io

def ensure_directory(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            print(f"Error creating directory {path}: {e}")
            exit(1)

def download_and_transform_dataset1(url, output_folder, db_path):
    ensure_directory(output_folder)
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        zip_file.extractall(output_folder)
    csv_filename = os.path.join(output_folder, zip_file.namelist()[1])
    df = pd.read_csv(csv_filename, on_bad_lines='skip')
    df.drop(columns=['Country Code'], inplace=True)
    df = df.loc[~(df==0).all(axis=1)]
    df.dropna(inplace=True)
    ensure_directory(os.path.dirname(db_path))
    conn = sqlite3.connect(db_path)
    df.to_sql('world_forest_data', conn, if_exists='replace', index=False)
    conn.close()

def download_and_transform_dataset2(url, output_folder, db_path):
    ensure_directory(output_folder)
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        zip_file.extractall(output_folder)
    csv_filename = os.path.join(output_folder, zip_file.namelist()[0])
    df = pd.read_csv(csv_filename, on_bad_lines='skip')
    
    df = df.loc[~(df==0).all(axis=1)]
    df.dropna(inplace=True)
    ensure_directory(os.path.dirname(db_path))
    conn = sqlite3.connect(db_path)
    df.to_sql('global_climate_insight_data', conn, if_exists='replace', index=False)
    conn.close()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Moves up two levels from current script's directory
    data_dir = os.path.join(base_dir, 'data')
    project_dir = os.path.join(base_dir, 'project')

    forest_data_url = 'https://www.kaggle.com/api/v1/datasets/download/webdevbadger/world-forest-area'

    climate_insight_data_url = 'https://www.kaggle.com/api/v1/datasets/download/goyaladi/climate-insights-dataset?datasetVersionNumber=4'


    download_and_transform_dataset1(forest_data_url, os.path.join(project_dir, 'forest_data'), os.path.join(data_dir, 'world_forest_data.sqlite'))
    download_and_transform_dataset2(climate_insight_data_url, os.path.join(project_dir, 'climate_insight_data'), os.path.join(data_dir, 'global_climate_insight_data.sqlite'))

if __name__ == "__main__":
    main()

     