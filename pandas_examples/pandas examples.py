# import pandas_examples as pd
# l=[1,2,3,4,5,6,7]
# name=['sugan','xyz','abc','xy','z','z1','z2']
# print(l)
# print(name)
# table={"sno":[l], "names":[name]}
# print(table)
# df=pd.DataFrame(table)
# print(df)

import pandas as pd

l=[1,2,3,4,5,6]
names=['a','b','c','d','e','f']
m1=[45,67,76,54,89,67]
m2=[76,89,89,78,45,87]
m3=[98,98,67,74,67,45]
print(l)
print(names)
print(m2)
print(m3)
table={'sno':l,'names':names}
print(table)
tab2={'sno': l, 'name':'names','m1':m1}
print(tab2)
df=pd.DataFrame(table)
print(df)
print(df.shape)
print(df.head(2))
print(df.tail())
print(df.describe())