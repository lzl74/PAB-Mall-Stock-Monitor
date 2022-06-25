import time
import json
import requests
from plyer import notification

url = 'https://mapi.wanlitong.com/mobileapi/m2s/mallgoods/queryProdInfo.json?authType=SHA1_1&coordinate=168.49679,28.82855&custString=1.36&machineNo=864375028810514&msgVersion=3.6.1&platform=ios&reqAppId=ios_app_wanlitong&screenSize=960*480&itemId=54124383&repositoryId=5974&areaId=&picAttr=750_750.webp&yqbToken=&goodsId=16379525&reqtranceno=bd330fbe-155c-4710-a5d8-591fced110c7&reqTime=1656123333028&mallModeId=STANDARD&sourceAppId=M&mediumId=PAB&reqChannelFlag=YQB_M&sign=cb74efd17c3a072f4b2bb53e98d5fb6e24b0df2a'

def get_page():
   a = requests.get(url)
   b = a.text
   c = type(b)
   d = json.loads(b)
   e = d['body']
   f = e['result']
   g = f['stock']
   print(g)

   if g != 0 :
       print("有货了")
       print(g)
       notification.notify(
           title="有货了",
           message="抢！",
           timeout =10)
       time.sleep(2)
   else:
       print("还没有")
       print(time.asctime(time.localtime(time.time())))
       time.sleep(1)

if __name__ == '__main__':
    while 1:
        get_page()