import pandas as pd
from datetime import datetime
import pandas_datareader as web
# import matplotlib.pyplot as plt


#pick any date after January of 2010
#let's pretend that you had $1000 dollars to invest at that date
#how much would it be today if you have invested back then and sold in on 1st of April 2019
#remotely download the SPX index from your date to 1st of April 2019
#load the FTSE from the file, and select values from your date  to 1st of April 2019
#normalize the return of each index for "Close" column so you can calculate your total return at any given date
#"invest" $1000 dollars on your date and make sure that you show your total gain/loss at every date
#plot both "investments" in SPX and FTSE on the same graph with names of "US Returns" and "EUR Returns" respectively.


startDate = "2015-12-15"
toDate = datetime.today()
init_investment = 1000

sp500 = web.DataReader("SP500", 'fred', startDate, toDate)
sp500['sp500_pct'] = (sp500.SP500/sp500.SP500[0]-1)
sp500['sp500_investment'] = (sp500.sp500_pct+1)*init_investment
sp500.to_csv("SP500.csv")


ftse = pd.read_csv("^ftm_d.csv")
ftse['ftse_pct'] = (ftse.Close/ftse.Close[0]-1)
ftse['ftse_investment'] = (ftse.ftse_pct+1)*init_investment

# ftse['ftse_investment'].plot()
# sp500['sp500_investment'].plot()
# plt.show()

# print(sp500)
# print(ftse.tail)


