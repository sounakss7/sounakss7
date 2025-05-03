import requests
import os
import json

token = os.environ["GH_TOKEN"]
repo = os.environ["REPO"]
headers = {"Authorization": f"token {token}"}

clone_url = f"https://api.github.com/repos/{repo}/traffic/clones"
views_url = f"https://api.github.com/repos/{repo}/traffic/views"

clone_data = requests.get(clone_url, headers=headers).json()
view_data = requests.get(views_url, headers=headers).json()

result = {
    "clones": clone_data.get("count", 0),
    "unique_cloners": clone_data.get("uniques", 0),
    "views": view_data.get("count", 0),
    "unique_visitors": view_data.get("uniques", 0)
}

with open("traffic.json", "w") as f:
    json.dump(result, f)
