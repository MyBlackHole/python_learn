import json

dic = {
    '17125363489': {
        'cookies': {
            'SUB': '_2A25ztmxWDeRhGeBL7lUW9ybMzj-IHXVQwtqerDV8PUNbmtANLWfTkW9NRu5yTJ5SCVmtimDBFutMBn_cjVCi6uS8',
        },
        "version": 1
    },
    '17125363488': {
        'cookies': {
            'SUB': '_2A25ztmxWDeRhGeBL7lUW9ybMzj-IHXVQwtqerDV8PUNbmtANLWfTkW9NRu5yTJ5SCVmtimDBFutMBn_cjVCi6uS8',
        },
        "version": 1
    },
}
print(len(dic))
print(json.dumps(dic))
del dic['17125363488']
print(len(dic))
