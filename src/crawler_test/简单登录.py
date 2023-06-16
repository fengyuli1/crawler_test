from src.crawler_test.crawler1 import send_request

if __name__ == "__main__":
    url = "http://passport.isoftstone.com/"
    username = input("用户名：")
    password = input("用户密码：")
    data = {
        "emp_DomainName": username,
        "emp_Password": password,
        "DomainUrl": "",
        "returnUrl": "",
        "p": "",
        "t": "",
    }
    response = send_request.send_request(url=url, method="post", data=data)
    my_url = "https://ipsapro.isoftstone.com/Portal/"
    response = send_request.send_request(url=my_url, method="get")
    send_request.save(file=response.text)
