import requests
import hashlib
import json


def func2():
    s = set()
    offset = 20
    page = 1
    while True:
        url = f"https://ib.snssdk.com/api/feed/forum_hot/v1/?category=forum_hot_tab&query_id=6570895765428767246&tab_id=0&is_preview=0&stream_api_version=88&count={offset}&offset=20&app_extra_params=%7B%7D&client_extra_params=%7B%22playparam%22%3A%22codec_type%3A0%2Ccdn_type%3A1%2Cenable_dash%3A0%2Cunwatermark%3A1%2Ctt_enable_adaptive%3A1%2Ctt_device_score%3A7.5%2Ctt_net_energy%3A0%22%7D&os_api=23&device_type=MuMu&pos=5r_-9Onkv6e_eCQieCoDv7G_8fLz-vTp6Pn4v6esrKuzrqSqrq-ur6SrrqukpKuxv_H86fTp6Pn4v6eupLOkraWopayrrqmuqaSlrKixv_zw_O3e9Onkv6e_eCQieCoDv7G__PD87dHy8_r06ej5-L-nrKyrs66kqq6vrq-kq66rpKSrsb_88Pzt0fzp9Ono-fi_p66ks6StpailrKuuqa6ppKWsqOA%3D&ssmix=a&manifest_version_code=8050&dpi=233&uuid=440000000174795&rom_version=23&app_name=news_article&version_name=8.0.5&ab_version=668779%2C660830%2C2406606%2C2406630%2C662176%2C1859937%2C662099%2C2323528%2C668774%2C2184403%2C2376068%2C668775%2C2327816%2C2393595%2C2001177%2C1593455%2C1877263%2C2332006%2C2197733%2C2235008&ab_group=94566%2C102751&ac=wifi&host_abi=armeabi-v7a&update_version_code=80508&channel=wandoujia5&device_platform=android&iid=2058700123549015&version_code=805&mac_address=08%3A00%3A27%3AD7%3A1B%3AED&plugin=0&cdid=71e92dd5-4d9e-4f86-80f0-8432aa0e0474&openudid=74343f0e9e15edb2&device_id=70874905115&resolution=700*1120&os_version=6.0.1&language=zh&device_brand=Android&ab_feature=102749%2C94563&aid=13"

        payload = {}
        headers = {
            'Host': 'ib.snssdk.com',
            'accept': 'application/json',
            'user-agent': 'com.ss.android.article.news/7501 (Linux; U; Android 5.1.1; zh_CN; VOG-AL10; Build/HUAWEIVOG-AL10; Cronet/TTNetVersion:b97574c0 2019-09-24)',
            'Cookie': 'odin_tt=4f7e289ecfc841c0d280d2f74a08cd8d49e31bdabb57d4f93fd4dcafe1354e9017001a0c1fe8d560f1eb03c3631924d0483bf29153766db4e4ce06899d1ca201'
        }

        response = requests.request("GET", url, headers=headers, data=payload, proxies=get_zdy_proxy())
        _dict = json.loads(response.json()['data'][0]['content'])
        text = _dict['raw_data']['rich_title']
        print(text)
        print(page)

        h = hashlib.md5()
        h.update(text.encode())
        md5 = h.hexdigest()
        if md5 in s:
            print(f"md5={md5}")
        s.add(md5)
        offset += 20
        page += 1


if __name__ == "__main__":
    func2()
