WEIBO_ACCOUNT = [
    ('17125363489', 'cs363489dfg'),
    ('17125363429', 'anqi3429san'),
    ('17125363426', 'xiaoqr3426nijs'),
    ('17049178657', 'Urunposting1234'),
    ('18561858583', 'wlb131415'),
    ('0085264307716', 'abc123456qq'),
    ('15077459464', 'abc15077459464OK')
]

user = '17125363426'
accounts = []
for i in WEIBO_ACCOUNT:
    if user in i:
        accounts.append(i)
        break

print(accounts)

_dict = {
    'a': 'a',
    'b': 'b',
    'c': 'c'
}

for i in _dict:
    # if i == 'a':
    #     del _dict[i]
    print(i)
