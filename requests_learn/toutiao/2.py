import requests

url = "https://ib.snssdk.com/search/?device_type=MuMu&app_name=news_article&channel=wandoujia5&device_platform=android&language=zh&aid=13&source=sug&offset=0&count=10&action_type=sug_keyword_search&from=huati&format=json&keyword=工资&search_start_time=1613618461&pd=huati"

payload={}
headers = {
  'Accept-Encoding': 'gzip',
  'X-SS-REQ-TICKET': '1611635376309',
  'passport-sdk-version': '30',
  'sdk-version': '2',
  'Cookie': 'qh[360]=1; odin_tt=1cacf31943c52e803d36b6c29c33efcb32d9179ec0b850f3508c03cf88ce4ccd5d94daf962268b0a94fe59bc19dd69b5525c0d67fd63aadb7908c397af05172f; install_id=2058700123549015; ttreq=1$7857f888dfce4b0fb75057e506d3896fd65de16e; WIN_WH=481_694; PIXIEL_RATIO=1.4562500715255737; FRM=new',
  'X-Tyhon': 'DRktIW86IyBCTjZrCW0/aGpEByJ6SiEQZn1ZEvU=',
  'X-Khronos': '1611635376',
  'X-Gorgon': '0404809d4001ae5ca252cb9a89bebe3d057da9c75d01ecb026e1',
  'Host': 'ib.snssdk.com',
  'Connection': 'Keep-Alive',
  'User-Agent': 'okhttp/3.10.0.1'
}

while True:
  response = requests.request("GET", url, headers=headers, data=payload)
  print(f"status={response.status_code}, html={response.text[:50]}")



