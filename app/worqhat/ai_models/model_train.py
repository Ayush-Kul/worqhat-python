import requests 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def list_datasets(api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    url = "https://api.worqhat.com/api/list-datasets"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.post(url, headers=headers)

    return response.text
    
def delete_dataset(dataset_id="123456789", api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    url = f"https://api.worqhat.com/api/delete-datasets/{dataset_id}"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.post(url, headers=headers)

    return response.text

    
def train_dataset(dataset_id="123456789", dataset_name="Sample Dataset", dataset_type="self", json_data="{'data':'This is sample Data'}", training_file=None, api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    url = "https://api.worqhat.com/api/ai/datasets/train-datasets"
    headers = {"Authorization": "Bearer " + api_key}

    # Construct payload with multipart form-data
    payload = {
            "datasetId": dataset_id,
            "dataset_name": dataset_name,
            "dataset_type": dataset_type,
            "json_data": (None, json_data),
            "training_file": (training_file, open(training_file, 'rb'))
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text
