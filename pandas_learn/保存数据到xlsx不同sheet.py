import pandas as pd

df = pd.read_excel('1.xlsx')
print(df)
print(df.columns)
print(df['户 籍 地'].unique())
print(df.loc[df['户 籍 地'] == '北京'])
print(df['户 籍 地'] == '北京')

writer = pd.ExcelWriter('2.xlsx')
bj_data = df.loc[df['户 籍 地'] == '北京']
hs_data = df.loc[df['户 籍 地'] == '黄石']
bj_data.to_excel(writer, sheet_name='北京')
hs_data.to_excel(writer, sheet_name='黄石')
writer.save()
writer.close()
