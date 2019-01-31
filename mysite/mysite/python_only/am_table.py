"""
"""
import pandas as pd 
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta
starting_principal =10000
current_principal = 10000
starting_date = date(2019,1,31)
last_action_date = date(2019,1,31)
total_interest = 0
interest_owed =0 
apr = 0.04
daily_rate = apr/365


current_date = date(2019,1,31)

pmt=350
cp = [10000]
dates = [current_date]
ipd = [0]
pp = [0]
ip = [0]

while cp[-1]>5:
    cd = dates[-1] + relativedelta(months=1)
    #print(cd)
    ipd_1 = daily_rate * cp[-1]
    #print(ipd_1)
    ip_1 = ipd_1 * (cd-dates[-1]).days
    #print(ip_1)
    pp_1 = pmt- ip_1
    #print(pp_1)
    cp_1 = cp[-1] - pp_1
    #print(cp_1)

    cp.append(round(cp_1,2))
    ipd.append(ipd_1)
    dates.append(cd)
    ip.append(round(ip_1,2))
    pp.append(round(pp_1,2))

my_table = pd.DataFrame({
    "Date":dates,
    "Principal":cp,
    "Payment":pmt,
    "Interest Paid":ip,
    "Principal Paid":pp,
    "Interest/Day":ipd
})
my_table.loc[0,"Payment"]=0
my_table.loc[0,"Interest/Day"]=daily_rate*starting_principal
print(my_table)


