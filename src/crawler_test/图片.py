from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "https://img1.gamersky.com/image2023/06/20230614_ls_red_141_3/1332.jpg"
    response = send_request.send_request(method="get", url=url)
    img_data = response.content
    send_request.save(file=img_data)
