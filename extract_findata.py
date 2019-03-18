from pandas_datareader.data import DataReader
from datetime import date
import matplotlib.pyplot as plt

#stock price
START_DATE  = date ( 2018, 1, 1 )
END_DATE    = date ( 2018, 12, 31 )
TICKER      = 'AMZN'
DATA_SOURCE = 'yahoo'

stock_data = DataReader ( TICKER, DATA_SOURCE, START_DATE, END_DATE ) 

stock_data[ 'High' ].plot( title=TICKER )
plt.show()

#interest rates
RATE        = 'DGS-10'
DATA_SOURCE = 'fred'
START_DATE  = date ( 2018, 1, 1 )

rates_data = DataReader ( RATE, DATA_SOURCE, START_DATE )
rates_data.head()

stock_data [ 'High' ].plot( title = RATE )
plt.show()

#bonds and stocks
START_DATE = date ( 2008, 1, 1 )

SERIES = ['BAMLHYH0A0HYM2TRIV', 'SP500']

data = DataReader ( SERIES, 'fred', START_DATE )

data.plot ( title = " & ".join ( SERIES ) + " comparison" )
plt.show()