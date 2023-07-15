
import json
import pickle
import numpy as np
import pandas as pd

__model = None
__data_columns = None
__suburbs = None
__types = None
__region_names = None


def load_saved_artifacts():
    global __data_columns
    global __suburbs
    global __types
    global __region_names
    global __model

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __suburbs = list(
            pd.Series([col.split("suburb_")[1] for col in __data_columns if col.startswith("suburb_")]).unique())
        __types = ["house"] + list(
            pd.Series([col.split("type_")[1] for col in __data_columns if col.startswith("type_")]).unique())
        __region_names = list(pd.Series(
            [col.split("regionname_")[1] for col in __data_columns if col.startswith("regionname_")]).unique())
    print("__data_columns:", __data_columns)
    print("__suburbs:", __suburbs)
    print("__types:", __types)
    print("__region_names:", __region_names)
    with open("./artifacts/melbourne_house_price_prediciton_model.pickle", "rb") as f:
        __model = pickle.load(f)


def predict_price(rooms, distance, bathroom, car, landsize, suburb, house_type, region_name):
    input_data_encoded = np.zeros(len(__data_columns))
    input_data_encoded[0] = rooms
    input_data_encoded[1] = distance
    input_data_encoded[2] = bathroom
    input_data_encoded[3] = car
    input_data_encoded[4] = landsize

    try:
        idx = __data_columns.index("Suburb" + suburb)
        input_data_encoded[idx] = 1
    except:
        pass

    if house_type != "house":
        try:
            idx = __data_columns.index("Type" + house_type)
            input_data_encoded[idx] = 1
        except:
            pass

    try:
        idx = __data_columns.index("Regionname" + region_name)
        input_data_encoded[idx] = 1
    except:
        pass

    return round(__model.predict(input_data_encoded.reshape(1, -1))[0], 2)


def get_suburbs():
    return __suburbs


def get_types():
    return __types


def get_region_names():
    return __region_names


if __name__ == "__main__":
    load_saved_artifacts()
    print(predict_price(4, 4, 5, 1, 200.0, 'Abbotsford', 'unit', 'Northern Metropolitan'))
