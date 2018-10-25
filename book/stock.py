import pandas as pd
import pandas_datareader.data as web

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
print (gs[0])