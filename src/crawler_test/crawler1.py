import json
import os
import time

import requests

Path = os.path.abspath(__file__).split("src")[0]
Log_path = os.path.join(Path, "save_log")
if not os.path.exists(Log_path):
    os.mkdir(Log_path)


class SendRequest:
    def __init__(self):
        self.session = requests.session()

    def send_request(self, **kwargs):
        default_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
        }
        url = kwargs.get("url")
        method = kwargs.get("method")
        headers = kwargs.get("headers", default_headers)
        params = kwargs.get("params")
        data = kwargs.get("data")
        body = dict()
        body["headers"] = headers
        if params:
            body["params"] = params
        if data:
            body["data"] = data
        response = self.session.request(method, url, **body)
        response.encoding = response.apparent_encoding
        # res = response.headers['Content-Type']
        # if 'json' in response.headers['Content-Type']:
        #     print(11111111111111111)
        # else:
        #     print(222222222222222)
        return response

    @staticmethod
    def save(**kwargs):
        file = kwargs.get("file")
        file_name = kwargs.get("name", f"1{time.time()}.html")
        print(file_name)
        file_path = os.path.join(Log_path, file_name)
        if isinstance(file, bytes):
            with open(file_path, "wb") as fp:
                fp.write(file)
        else:
            with open(file_path, "w", encoding="utf-8") as fp:
                if isinstance(file, dict) or isinstance(file, list):
                    json.dump(file, fp=fp, ensure_ascii=False)
                else:
                    fp.write(file)
        return file_path


send_request = SendRequest()

if __name__ == "__main__":
    url = "https://www.gamersky.com/news/202306/1607553.shtml"
    response = send_request.send_request(method="get", url=url)
    page_text = response.text
    send_request.save(file=page_text)
