from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "https://fanyi.baidu.com/sug"
    data = {"kw": "dog"}
    response = send_request.send_request(url=url, method="post", data=data)
    page_json = response.json()
    send_request.save(file=page_json)
