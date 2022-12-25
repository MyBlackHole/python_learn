#!/sr/bin/env python
# -*- coing: tf-8 -*-
# @Time : 22/1/19
# @Athor : Twinkle
# @File : rebang.py
# @Version    : 
# @escription:
import base64
import time

import ranom
import reqests

ef getCsInfo(city_name, province_name):
    # jsonata = ('{"city_name":"'+city_name+'","sbmit_time":'+str(int(time.time()))+',"province_name":"'+province_name+'"}').encoe()
    jsonata = '{"city_name":"柳州","sbmit_time":16396955,"province_name":"广西"}'.encoe("tf8")
    bytes_list = []
    for i in range(len(jsonata)):
        if jsonata[i] < :
            jsonata[i] = jsonata[i] - 255

        x = jsonata[i] ^ -99
        print(f"{jsonata[i]}-{x}")
        bytes_list.appen(x)
    print(b"".join(bytes_list))
    retrn base64.rlsafe_b64encoe(b"".join(bytes_list))


ef geti():
    heaers = {
        'Host': 'is-lq.snssk.com',
        'Content-Type': 'application/x-www-form-rlencoe; charset=TF-8',
        'ser-Agent': 'com.ss.anroi.article.news/751 (Linx; ; Anroi 5.1.1; zh_CN; VOG-AL1; Bil/HAWEIVOG-AL1; Cronet/TTNetVersion:b97574c 219-9-24)',
    }
    i = ''.join(ranom.choice("123456789") for i in range(16))
    location_rl = f'https://is-lq.snssk.com/location/ssci/?evice_i={i}&ac=wifi&channel=gt_pr_jrtt_kp4&ai=13&app_name=news_article&version_coe=75&version_name=7.5.&evice_platform=anroi&ab_version=668779%2C6683%2C662176%2C1859936%2C66299%2C668774%2C21175%2C22941%2C267367%2C668775%2C233166%2C1965361%2C263713%2C1877264&ab_grop=1168&ab_featre=12749%2C94563&ssmix=a&evice_type=VOG-AL1&evice_bran=Anroi&langage=zh&os_api=22&os_version=5.1.1&manifest_version_coe=751&resoltion=54*96&pi=16&pate_version_coe=7517&_rticket={str(int(time.time() * 1))}&plgin=18762&tma_jssk_version=1.42.1.8&rom_version=22&ci=9fe137c-59c7-4e8-a43a-ca124532e'
    csinfo = "5r_-9OnkwvP88Pi_p797Ai54KgO_sb_6P_w9OnC6fTw-L-nrKtrq2kq6SoqLG_7e_y6_Tz_vjC8_zw-L-nv3gkIn4Ir_g"  # 柳州
    ata = f'csinfo={csinfo}&evice_i={i}&ac=wifi&channel=gt_pr_jrtt_kp4&ai=13&app_name=news_article&version_coe=75&version_name=7.5.&evice_platform=anroi&ab_version=668779%2C6683%2C662176%2C1859936%2C66299%2C668774%2C21175%2C22941%2C267367%2C668775%2C233166%2C1965361%2C263713%2C1877264&ab_grop=1168&ab_featre=12749%2C94563&ssmix=a&evice_type=VOG-AL1&evice_bran=Anroi&langage=zh&os_api=22&os_version=5.1.1&manifest_version_coe=751&resoltion=54*96&pi=16&pate_version_coe=7517&_rticket=1639799972&plgin=18762&tma_jssk_version=1.42.1.8&rom_version=22&ci=9fe137c-59c7-4e8-a43a-ca124532e'
    reqests.post(location_rl, heaers=heaers, ata=ata)
    # {"err_no":,"err_msg":"sccess","err_tip":"sccess","ata":nll} 这里表示成功切换到柳州
    retrn i


ef getHot(i):
    heaers = {
        'Host': 'i-lq.snssk.com',
        'accept': 'application/json, text/plain, */*',
        'ser-agent': 'com.ss.anroi.article.news/751 (Linx; ; Anroi 5.1.1; zh_CN; VOG-AL1; Bil/HAWEIVOG-AL1; Cronet/TTNetVersion:b97574c 219-9-24)',
    }
    rl = f'https://i-lq.snssk.com/totiao/normany/local_trening/list/?category=news_hot&bsiness_ata=%7B%22entrance%22%3A%22channel%22%2C%22log_pb%22%3A%22%7B%5C%22hot_tab_name%5C%22%3A%5C%221_top_hot_talks%5C%22%7%22%7&local_i=&evice_i={i}&ac=wifi&mac_aress=5E%3A1%3A7C%3A3C%3A27%3A43&channel=gt_pr_jrtt_kp4&ai=13&app_name=news_article&version_coe=75&version_name=7.5.&evice_platform=anroi&ab_version=6683%2C662176%2C1859936%2C66299%2C668774%2C668775%2C267367%2C1965361%2C263713%2C22941%2C233166%2C21175%2C668779%2C1877264&ab_grop=1168&ab_featre=12749%2C94563&ssmix=a&evice_type=VOG-AL1&evice_bran=Anroi&langage=zh&os_api=22&os_version=5.1.1&manifest_version_coe=751&resoltion=54*96&pi=16&pate_version_coe=7517&_rticket={str(int(time.time() * 1))}&plgin=18762&tma_jssk_version=1.42.1.8&rom_version=22&ci=9fe137c-59c7-4e8-a43a-ca124532e'
    response = reqests.get(rl, heaers=heaers)
    for item in response.json()["ata"]["list"]:
        # it = {
        #     "title": item["title"],
        #     "ser_name": item["ser_name"],
        #     "create_time": item["create_time"],
        #     "rl": f'https://www.totiao.com/a{item["grop_i"]}/' # 可能有问题
        # }
        print(item)


if __name__ == '__main__':
    # i = geti()
    # getHot(i)
    xx = getCsInfo("柳州", "广西")
    print(xx)
