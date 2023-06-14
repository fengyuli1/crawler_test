from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    params = {
        'type': '11',
        'interval_id': '100:90',
        'action': "",
        'start': '0',
        'limit': '20',
    }
    response = send_request.send_request(url=url, method="get", params=params)
    page_json = response.json()
    send_request.save(file=page_json)
