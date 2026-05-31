import pandas as pd
df = pd.read_csv('stu.csv')
print(df)

df2 = pd.read_json('stu.json')
print(df2)

df3 = pd.read_xml('stu.xml')
print(df3)

#conver xml to csv as stu2
df3.to_excel('stu3.xlsx',index=False)

#Review
import numpy as np
 #diagonal matrix
#print(np.diag ([2,5,3]))
 #Identity matrix
#print(np.eye(3))
 #tril.u
#print(np.tril(np.ones((3,3))))
#print(np.triu(np.ones((3,3))))

import yfinance as yf
import pandas as pd
#data = yf.download(tickers='USD-USD', start='2018-01-01', end='2020-12-31')
#df = pd.DataFrame(data)
#print(df.info())

#a = [[1,2,3],[4,5,6]]
#print(pd.Series(a))
#print(pd.DataFrame(a))
#series = pd.Series(a)
#dataframe = pd.DataFrame(a)
#print(type(series))
#print(type(dataframe))

