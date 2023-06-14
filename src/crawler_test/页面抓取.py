from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "https://www.sogou.com/web"
    params = {"query": "英雄传说"}
    response = send_request.send_request(url=url, method="get", params=params)
    page_text = response.text
    send_request.save(file=page_text)
