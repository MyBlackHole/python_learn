# import requests
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Safari/537.36'
# }
#
# json = {
#     "adultPassengersCount": "1",
#     "departureDate": "2020-04-29",
#     "departureTimeOfDay": "ALL_DAY",
#     "destinationAirportCode": "BDL",
#     "fareType": "USD",
#     "int": "HOMEQBOMAIR",
#     "originationAirportCode": "LAX",
#     "passengerType": "ADULT",
#     "reset": "true",
#     "returnDate": "2020-05-01",
#     "returnTimeOfDay": "ALL_DAY",
#     "seniorPassengersCount": "0",
#     "tripType": "roundtrip",
#     "application": "air-booking",
#     "site": "southwest"
# }
#
# cookies = {
#     'Cookie': 'check=true; AMCVS_65D316D751E563EC0A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C04044033138492346900108077833255227802; s_cc=true; AMCV_65D316D751E563EC0A490D4C%40AdobeOrg=-432600572%7CMCIDTS%7C18380%7CMCMID%7C04044033138492346900108077833255227802%7CMCAAMLH-1588592243%7C11%7CMCAAMB-1588592243%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1587994647s%7CNONE%7CMCSYNCSOP%7C411-18387%7CMCAID%7CNONE%7CvVersion%7C4.5.2; sRpK8nqm_sc=AO5VbbtxAQAACvSPVvY_lcdetAyGBi7L2dR_lq5KfTrvno_9bcUOAyv72jNR|1|1|c99aceaeac0f8d27d42b972b809033a4bbbe9f6e; valid_promo=false; versaTag-orderID=ieybncvs8s; sRpK8nqm_dc=%7B%22c%22%3A%20%22RmFqREFYeUJ5dWVYUnJJMw%3D%3D6-4eQV8UVwWNF6FmkaDNzcDiFYL7YkIOU8rwb01pMTNABRW-YhCbEDvMiL2b5oClsrnHf4NQCQ_QUy2CqNOYX2Dzm2_RlhjN8PXOJbWN6r6ztoc%3D%22%2C%20%22dc%22%3A%20%22000%22%2C%20%22mf%22%3A%200%7D; s_gpv_pn=BOOK%3AAIR%3ASelect%20Flight%20Page; U08jgd0C=ADNip7txAQAA1zHsOSSz6s7lyJjkGLAjGguVRAo-IbWwaIZebdJUQHhejRY2; mbox=PC#38565db50a40408b9b08cd5d209dc62b.22_0#1651232246|session#df4f28c6a61643b38e5e7a712a006d86#1587993104; akavpau_prod_fullsite=1587991273~id=afcace657d126750ed70ed9b99f1fab3; RT="z=1&dm=southwest.com&si=6bc76fe8-d36a-498d-9c15-40b678fa6f90&ss=k9igs5zz&sl=1&tt=yjk&bcn=%2F%2F173e252a.akstat.io%2F&ld=83eq&nu=846ef8c2dcbeb68efdab9ec3e7416f78&cl=aaaa"; s_sq=swaprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DBOOK%25253AAIR%25253ASelect%252520Flight%252520Page%2526link%253DTHU%252520Apr%25252030%2526region%253Dair-booking-product-0%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c'
# }
#
# # response = requests.post(url='https://www.southwest.com/api/air-booking/v1/air-booking/page/air/booking/shopping',
# #                          json=json, headers=headers, cookies=cookies, verify=False)
from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://www.southwest.com/')

print(response.html.render())
print(response.status_code)
print(response.cookies)
