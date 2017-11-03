import requests
import json

def retrieve_passwd():
    name = "aletan"
    mail = "aletan@gagogroup.com"
    link = "http://gagogroup.resetEmailAddress.com"
    url = "https://api.gagogroup.cn/api/v3/retrieve_password"
    header = {"Content-Type":"application/json"}
    data = {"username":name, "email":mail, "link":link}
    r = requests.post(url, headers=header, data=json.dumps(data), verify=False)
    print r.content

if __name__ == "__main__":
    retrieve_passwd()
