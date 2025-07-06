import requests
from json import loads, dumps
from dotenv import load_dotenv
import os
load_dotenv()
gist_id = os.getenv("GIST_ID")
token = os.getenv("GITHUB_TOKEN")

url = f"https://api.github.com/gists/{gist_id}"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28"
}


class GistAPI:
    def get_gist(self):
        get = requests.get(url, headers=headers).json()
        task_data = loads(get["files"]["data.json"]["content"])
        return task_data

    def patch_gist(self, new_data):
        data = {
            "description": "An updated gist description",
            "files": {
                "data.json": {
                    "content": dumps(new_data, indent=4)
                }
            }
        }
        print(requests.patch(url, headers=headers, json=data))
