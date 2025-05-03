import requests
import os
import json
import sys

token = os.environ.get("GH_TOKEN")
repo = os.environ.get("REPO")

if not token or not repo:
    print("GH_TOKEN or REPO environment variable not set.")
    sys.exit(1)

headers = {"Authorization": f"token {token}"}

clone_url = f"https://api.github.com/repos/{repo}/traffic/clones"
views_url = f"https://api.github.com/repos/{repo}/traffic/views"

clone_resp = requests.get(clone_url, headers=headers)
view_resp = requests.get(views_url, headers=headers)

if clone_resp.status_code != 200:
    print(f"Error fetching clone data: {clone_resp.status_code} - {clone_resp.text}")
    sys.exit(1)

if view_resp.status_code != 200:
    print(f"Error fetching view data: {view_resp.status_code} - {view_resp.text}")
    sys.exit(1)

clone_data = clone_resp.json()
view_data = view_resp.json()

result = {
    "clones": clone_data.get("count", 0),
    "unique_cloners": clone_data.get("uniques", 0),
    "views": view_data.get("count", 0),
    "unique_visitors": view_data.get("uniques", 0)
}

with open("traffic.json", "w") as f:
    json.dump(result, f, indent=4)

