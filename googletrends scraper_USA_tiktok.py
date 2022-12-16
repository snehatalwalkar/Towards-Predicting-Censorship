from pytrends.request import TrendReq
import pandas as pd
import time

startTime = time.time()
pytrend = TrendReq(hl='en-US', tz=360)

colnames = ["keyword"]
df = pd.read_csv("C:\\pytrendsdata.csv", names=colnames)
df2 = df["keyword"].values.tolist()
df2.remove("keyword")

dataset = []
for geo_code in ['US-SC','US-MD','US-UT','US-GA']:
    for x in range(0,len(df2)):
        keywords = [df2[x]]
        pytrend.build_payload(
        kw_list=keywords,
        cat=0,
        timeframe='2022-12-01 2022-12-15',
        geo=geo_code)
        data = pytrend.interest_over_time()
        if not data.empty:
            data = data.drop(labels=['isPartial'],axis='columns')
            data['geo']=geo_code
            dataset.append(data)

result = pd.concat(dataset)
result.to_csv("US.csv")
