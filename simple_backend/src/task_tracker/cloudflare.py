import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_url = os.getenv("API_BASE_URL")
token = os.getenv("CLOUDFLARE_API_TOKEN")

headers = {"Authorization": f"Bearer {token}"}


class CloudFlare:

    def change_input(self, input_msg):
        inputs = [
            {"role": "system",
             "content": "You are a suggesting user how to get their tasks done, advise, help find solution. It must be short! 50 symbols limit! No nice talk, just solution!"},
            {"role": "user", "content": input_msg}]
        input_msg = {"messages": inputs}

        return input_msg

    def run(self, task_text: str):
        model = "@cf/meta/llama-3-8b-instruct"
        input_msg = self.change_input(task_text)
        response_json = requests.post(f"{api_url}{model}", headers=headers, json=input_msg).json()
        result = response_json["result"]["response"]
        return result



