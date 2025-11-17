import requests

try:
    r = requests.get("https://kollywoodclash.in", timeout=10)
    print("Ping success:", r.status_code)
except Exception as e:
    print("Ping failed:", e)
