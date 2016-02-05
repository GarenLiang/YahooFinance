# YahooFinance
ListDji=['AXP','BA','CAT',....,'VZ','WMT','XOM']
quotes=[[0 for col in range(90)]for row in range(30)]
listTemp=[[0 for col in range(90)] for row in range(30)]
for i in range(30):
    quotes[i]=quotes_historical_yahoo(listDji[i],start,end)
listTemp[i][j]=1 or -1
data=vstack(listTemp)
centroids,_=kmeans(data,4)
result,_=vq(data,centroids)
