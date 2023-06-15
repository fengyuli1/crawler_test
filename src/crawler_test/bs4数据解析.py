from bs4 import BeautifulSoup

from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "https://www.gamersky.com/news/202306/1607553.shtml"
    while True:
        response = send_request.send_request(method="get", url=url)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "lxml")
        for img_url in soup.select(".picact"):
            img_url = img_url["src"]
            img_name = img_url.split("/")[-1]
            img_data = send_request.send_request(method="get", url=img_url).content
            send_request.save(file=img_data, name=img_name)
        next_page = soup.select(".page_css > a")[-1]
        if next_page.string == "下一页":
            url = next_page["href"]
        else:
            break
