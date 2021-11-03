import xml.etree.ElementTree as ET

from fontTools.ttLib import TTFont

font = TTFont('tff.woff')
font.saveXML('tff.xml')

xml = ET.parse('tff.xml')
root = xml.getroot()

list1ss = []
my_dict = {}
for i in root[8]:
    my_d = {}
    a = []
    g = 0
    for j in i:
        f = 0
        if j.tag != 'contour':
            continue
        else:
            g = g + 1
        for z in j:
            if z.tag == 'pt':
                f = 1 + f
                a.append(z.attrib)
        my_d[g] = f
        a.append({'f': f, 'lena': len(a)})
    # list1s.append(f)
    my_dict[i.attrib['name']] = my_d
    list1ss.append(a)

dan_dict = {3: [53, ], 1: [16, ], 7: [26, ], 5: [39, ], 2: [49, ]}
er_dict = {6: [37, 16], 9: [45, 17], 4: [12, 4], 0: [25, 16]}
san_dict = {8: [25, 15, 17]}

di_keys = my_dict.keys()
dan1_dict = {}
er1_dict = {}
san1_dict = {}
for i in di_keys:
    if len(my_dict[i]) == 1:
        dan1_dict[i] = my_dict[i]
    if len(my_dict[i]) == 2:
        er1_dict[i] = my_dict[i]
    if len(my_dict[i]) == 3:
        san1_dict[i] = my_dict[i]
a = []
for i in dan_dict.keys():
    f = 9
    for j in dan1_dict.keys():
        d = dan1_dict[j][1] - dan_dict[i][0]
        if abs(d) < f:
            a.clear()
            f = abs(d)
            a.append([i, j])
            print(a)

for i in er_dict.keys():
    f = 9
    e = 0
    for h in er_dict[i]:
        e = e + h
    for j in er1_dict.keys():
        e1 = 0
        for h in er1_dict[j].keys():
            e1 = e1 + er1_dict[j][h]
        d = e1 - e
        if abs(d) < f:
            a.clear()
            f = abs(d)
            a.append([i, j])
            print(a)
