import pandas as pd

df = pd.read_excel('20200716.xls')
# df = df[df.notnull()]
# df['公众号'] = df['公众号'][df['公众号'].str.contains('新浪微博')]
df = df[df['公众号'].str.contains('新浪微博')]
df['公众号'] = df['公众号'].str.extract(r'“(.*)”')
print(df)

# xl_df = xl_df.str.extract(r'“(.*)”')
# print(xl_df[0].tolist())
df.to_csv('20200716.csv', index=False)
# # for i in df.values:
# #     print(i)
