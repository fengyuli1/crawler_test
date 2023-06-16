import time
from multiprocessing.dummy import Pool

from lxml import etree

from src.crawler_test.crawler1 import SendRequest, send_request


def get_data(url):
    get_gif = SendRequest()
    while True:
        response = get_gif.send_request(method="get", url=url)
        tree = etree.HTML(response.text)
        for img_url in tree.xpath('//div[@class="Mid2L_con"]//img/@src'):
            img_name = img_url.split("/")[-1]
            img_data = get_gif.send_request(method="get", url=img_url).content
            get_gif.save(file=img_data, name=img_name)
        next_page = tree.xpath('//div[@class="page_css"]/a')[-1]
        if next_page.xpath("./text()")[0] == "下一页":
            url = next_page.xpath("@href")[0]
        else:
            return


if __name__ == "__main__":
    start_time = time.time()
    url = "https://www.gamersky.com/"
    response = send_request.send_request(url=url, method="get")
    tree = etree.HTML(response.text)
    sub_tree = tree.xpath('//ul[@class="SPimgtxt"]')[0]
    img_url_list = sub_tree.xpath("./li/a/@href")
    pool = Pool(8)
    pool.map(get_data, img_url_list)
    pool.close()
    pool.join()
    end_time = time.time()
    print(start_time - end_time)
