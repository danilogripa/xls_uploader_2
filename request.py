import requests


def send(os, ag, tp, key, tg, af):
    url = 'http://192.168.1.66:5000/convert'
    myobj = {"os": os, "ag": ag, "type": tp, "key": key, "tg": tg, "af": af}
    x = requests.post(url, json=myobj)
    print(x.text)
    return x.text
