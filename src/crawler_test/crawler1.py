import json
import os
import time
import requests

Path = os.path.abspath(__file__).split("src")[0]
Log_path = os.path.join(Path, "save_log")


class SendRequest:
    @staticmethod
    def send_request(**kwargs):
        default_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
        }
        url = kwargs.get("url")
        method = kwargs.get("method")
        headers = kwargs.get("headers", default_headers)
        params = kwargs.get("params")
        data = kwargs.get("data")
        body = dict()
        if headers:
            body["headers"] = headers
        if params:
            body["params"] = params
        if data:
            body["data"] = data
        response = requests.request(method, url, **body)
        # res = response.headers['Content-Type']
        # if 'json' in response.headers['Content-Type']:
        #     print(11111111111111111)
        # else:
        #     print(222222222222222)
        return response

    @staticmethod
    def save(**kwargs):
        file = kwargs.get("file")
        file_name = f"1{time.time()}.html"
        print(file_name)
        file_path = os.path.join(Log_path, file_name)
        with open(file_path, "w", encoding="utf-8") as fp:
            if isinstance(file, dict) or isinstance(file, list):
                json.dump(file, fp=fp, ensure_ascii=False)
            else:
                fp.write(file)
        return file_path


send_request = SendRequest()

if __name__ == "__main__":
    url = "https://www.sogou.com/"
    response = send_request.send_request(method="get", url=url)
    page_text = response.text
    send_request.save(file=page_text)
