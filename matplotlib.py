# YahooFinance
from matplotlib.finance import quotes_historical_yahoo
from datetime import time
import pandas as pd 
today=date.today()
start=(today.year-1,today.month,today.day)
quotes=quotes_historical_yahoo('AXP',start,today)
df=pd.DataFrame(quotes)

print df
