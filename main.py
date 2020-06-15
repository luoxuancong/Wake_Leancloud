import requests

def get_status(url):
    
    r=requests.get(url=url)

    return r.status_code

def main():
    status=get_status("https://valine.0941314.xyz/")

    if status==200:
        print("激活成功！")
    else:
        print("激活失败！HTTP状态码为：",status)

if __name__ == "__main__":
    main()
