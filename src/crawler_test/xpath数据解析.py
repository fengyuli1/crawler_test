from lxml import etree

from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "https://www.gamersky.com/news/202306/1608051.shtml"
    while True:
        response = send_request.send_request(method="get", url=url)
        tree = etree.HTML(response.text)
        for img_url in tree.xpath('//div[@class="Mid2L_con"]//img/@src'):
            img_name = img_url.split("/")[-1]
            img_data = send_request.send_request(method="get", url=img_url).content
            send_request.save(file=img_data, name=img_name)
        next_page = tree.xpath('//div[@class="page_css"]/a')[-1]
        if next_page.xpath("./text()")[0] == "下一页":
            url = next_page.xpath("@href")[0]
        else:
            break
