import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "text": "Aliens officially join Indian parliament"
}

try:
    response = requests.post(url, json=data)
    
    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    if response.status_code == 200:
        print("JSON:", response.json())
    else:
        print("Error from API")

except Exception as e:
    print("Connection Error:", e)