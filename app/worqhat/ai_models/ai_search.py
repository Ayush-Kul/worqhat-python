import requests 

def search_ai_v2(api_key=None,question="", training_data="" ):
    url = "https://api.worqhat.com/api/ai/search/v2"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "question": question,
        "training_data": training_data
        }

    response = requests.request("POST",url, json=payload, headers=headers)

    return response.text

    
def search_ai_v3(api_key=None, question="", training_data="", search_count=10):
   
    url = "https://api.worqhat.com/api/ai/search/v3"
    headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
    }

    payload = {
            "question": question,
            "training_data": training_data,
            "search_count": search_count
    }

    response = requests.request("POST",url, json=payload, headers=headers)

    return response.text
