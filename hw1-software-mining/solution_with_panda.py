import pandas as pd

df = pd.read_csv("/Users/jack/MyDocument/WebDevloper/DataMining/Intro/hw1-software-mining/Sample.csv", delimiter=" ")
# print(df)
# print(list(df.columns))

# for i in df.iterrows() :
#   print(i[0])
#   print(i[1]['Name'])
#   break

# ข้อ 1
# print(df.groupby('Platform').count()['Name'])
print(df['Platform'].value_counts().index[0])
print(df['Platform'].value_counts().index[1])

print("====================================================")

# ข้อ 2
df[df['Platform'] == 'Go']
print(df['License'].value_counts().index[0])
print(df['License'].value_counts().index[2])

print("====================================================")

# print(df[df['Stars'] > 1000])
# print(df[(df['Stars'] > 5000) & (df['Platform'] == 'Rubygems')])
# print(df[((df['Size']) < 1000) | (df['Size'] > 100000)])
# print(df[((df['Platform'] == 'Go') | (df['Platform'] == 'NPM')) & (df['Stars'] >= 10000)])

# ข้อ 3
print(df[df['NbOfVersions'] == df['NbOfVersions'].max()])

print("====================================================")

# print("====================================================")
# print(df['Size'].min())
# df1 = df[df['Language'] == 'Python']
# print(df1[df1['Size'] == df1['Size'].min()])
# df['Stars+1'] = df['Stars'] + 1
# df['P_L']  = df['Platform'] + '_' + df['Language']
# df2 = pd.DataFrame({'Name': ['ABC','DEF'], 'Platform': ['PyPi','NPM'], 'Stars':[4.0,6.0]})
# df4 = df.loc[:,['Name', 'Platform', 'Stars']]
# print(df2)
# df3 = pd.concat([df4,df2])
# print(df3)

# ข้อ 4
df1 = df[df['Language'] == 'Python']
result = df1['Size'].mean()
print(f'{result:.3f}')

print("====================================================")

# ข้อ 5
df1 = df[df['Host'] == 'GitHub']
result = df1['Language'].value_counts()
print(result[result == result.min()])

print("====================================================")

# ข้อ 6
# notContain = ['.md', '.markdown', '.MD']
# result = df[(df['ReadmeFilename'] != '-') & (df['ReadmeFilename'].str.contains('.')) & ~(df['ReadmeFilename'].str.contains('|'.join(notContain)))]
# print(result['ReadmeFilename'].str.lower().value_counts())

x = df['ReadmeFilename'].apply(lambda x: x.split(".")[-1] if "." in x else '-').value_counts()
print(x)
print(x.count())

print("====================================================")

# ข้อ 7 
print(df[df['Stars'] == df['Stars'].max()])

print("====================================================")

# ข้อ 8
print(df[(df['Name'].str.contains('js')) & (~df['Name'].str.contains('json'))].count()[1])