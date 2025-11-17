import requests

url = "https://kollywoodclash.in"

try:
    r = requests.get(url, timeout=10)
    print("Status Code:", r.status_code)
except Exception as e:
    print("Error:", e)
