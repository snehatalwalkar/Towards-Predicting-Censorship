from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US', tz=360)

colnames = ["keywords"]
df = pd.read_csv("C:\\pytrendsdata.csv", names=colnames)
df2 = df["keywords"].values.tolist()
df2.remove("keywords")
#print(df(head))
print(len(df2))

dataset = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrends.build_payload(kw_list=keywords,cat=0,timeframe='2022-09-14 2022-12-14', geo='IR')
     data = pytrends.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

result = pd.concat(dataset, axis=1)
result.to_csv('search_trends3.csv') #rate limited, multiple files exist


