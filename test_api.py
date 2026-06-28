import requests

HEADERS = {
    "X-Frontend-Id": "6",
    "X-Frontend-Version": "0",
    "X-Niconico-Language": "ja-jp",
    "User-Agent": "nico-rss-feedly/1.0",
}

USER_ID = "1594318"

url = (
    f"https://nvapi.nicovideo.jp/v3/users/{USER_ID}/videos"
    "?sortKey=registeredAt"
    "&sortOrder=desc"
    "&pageSize=5"
    "&page=1"
)

r = requests.get(url, headers=HEADERS, timeout=30)

print("HTTP", r.status_code)
print(r.text[:1000])

import json

print(json.dumps(r.json(), indent=2, ensure_ascii=False))