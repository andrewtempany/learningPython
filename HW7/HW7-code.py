# import csv
import numpy as np
import pandas as pd
import pandas_datareader as wb
from datetime import datetime


# Step 1(10 points): Remotely Download "Treasury Constant Maturity Rate" from FRED
# (https://fred.stlouisfed.org/categories/115) from 02/01/2014 to 02/01/2016
# Step 2( 5 points ): Determine the average and standard deviation for each of the maturities(maturity is 6-month, 1 year, etc.)
# Step 3( 5 points ): Select only those rows that have value more or less than avg +/- 1 std
# Step 4( 10 points ): Create a dataframe which has only those rows for which all of the maturities has value outside of avg +/- 1 std. Hint: think about joins for frames in step 3
# Step 5( 5 points): Save the generated dataframe as sigma.xlsx


# Please upload this filled file and sigma.xlsx


fromDate = "2014-02-01"
toDate = "2016-02-01"


################### 6-Month ###################

ticker6MO = 'DGS6MO'
df6MO = wb.DataReader(ticker6MO, 'fred', fromDate, toDate)
df6MO.to_csv("6month.csv")

mean6MO = df6MO['DGS6MO'].mean()
std6MO = np.std(df6MO['DGS6MO'])

outliers6MO = df6MO[(df6MO["DGS6MO"] > mean6MO + std6MO) |
                    (df6MO["DGS6MO"] < mean6MO - std6MO)]

# outliers6MO = outliers6MO[(outliers6MO["DGS6MO"] != Nan)]

print("-------------df6MO-------------")
# print("mean : ", mean6MO)
# print("standard deviation : ", std6MO)
# print("needs to be above : ", std6MO + mean6MO)
# print(df6MO.head)
# print(outliers6MO.head)


################### 1-Year ###################


ticker1Y = 'DGS1'
df1Y = wb.DataReader(ticker1Y, 'fred', fromDate, toDate)
df1Y.to_csv("1year.csv")

mean1Y = df1Y['DGS1'].mean()
std1Y = np.std(df1Y['DGS1'])

outliers1Y = df1Y[(df1Y["DGS1"] > mean1Y + std1Y) |
                  (df1Y["DGS1"] < mean1Y - std1Y)]

print("-------------df1Y-------------")
# print("mean : ", mean1Y)
# print("standard deviation : ", std1Y)
# print("needs to be above : ", std1Y + mean1Y)
# print(df1Y.head)
# print(outliers1Y.head)


################### 5-Year ###################
ticker5Y = 'DGS5'

df5Y = wb.DataReader(ticker5Y, 'fred', fromDate, toDate)
df5Y.to_csv("5year.csv")

mean5Y = df5Y['DGS5'].mean()
std5Y = np.std(df5Y['DGS5'])

outliers5Y = df5Y[(df5Y["DGS5"] > mean5Y + std5Y) |
                  (df5Y["DGS5"] < mean5Y - std5Y)]

print("-------------df5Y-------------")
# print("mean : ", mean5Y)
# print("standard deviation : ", std5Y)
# print("needs to be above : ", std5Y + mean5Y)
# print(df5Y.head)
# print(outliers5Y.head)


################### 10-Year ###################
ticker10Y = 'DGS10'

df10Y = wb.DataReader(ticker10Y, 'fred', fromDate, toDate)
df10Y.to_csv("10year.csv")

mean10Y = df10Y['DGS10'].mean()
std10Y = np.std(df10Y['DGS10'])

outliers10Y = df10Y[(df10Y["DGS10"] > mean10Y + std10Y) |
                    (df10Y["DGS10"] < mean10Y - std10Y)]

print("------------df10Y-------------")
# print("mean : ", mean10Y)
# print("standard deviation : ", std10Y)
# print("needs to be above : ", std10Y + mean10Y)
# print(df10Y.head)
# print(outliers10Y.head)


joinOne = df6MO.join(df1Y, how='inner')
joinTwo = joinOne.join(df5Y, how='inner')
joinThree = joinTwo.join(df10Y, how='inner')
print(joinThree.head())


joinThree.to_csv("sigma.csv")

# fn_in = 'sigma.xlsx'
# fn_out = 'sigma.xlsx'

# with open(fn_in, 'r') as inp, open(fn_out, 'w') as out:
#     writer = csv.writer(out)
#     for row in csv.reader(inp):
#         if len(row) <= 14:
#             writer.writerow(row)
