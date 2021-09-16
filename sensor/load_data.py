import os,glob,csv

def load_sensor_data():
    sensor_data = []
    sensor_files = glob.glob(os.path.join(os.getcwd(),"datasets","*.csv"))
    for sensor_file in sensor_files:
        with sensor_file
