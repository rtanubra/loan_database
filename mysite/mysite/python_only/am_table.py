"""
Goal of this module is to help the user visualize the ammortization table 
at the start of the loan
Required inputs are 

"""
import pandas as pd 
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta
def table_builder(starting_p,apr,pmt=350,starting_date=date.today()):
    starting_principal =9000
    starting_date = date(2019,1,31)
    apr = 0.04
    daily_rate = apr/365
    pmt=pmt


    current_date = starting_date
    cp = [starting_principal]
    dates = [current_date]
    ipd = [0]
    pp = [0]
    ip = [0]

    while cp[-1]>pmt:
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
    total_interest = sum(list(my_table["Interest Paid"]))

    return my_table, total_interest

"""
if this module is imported 
outputs
my_table
total_interest

fx
table_builder(starting_p,apr,pmt=350,starting_date=date.today()):
"""

my_table,total_interest =table_builder(9000,0.04)
print(my_table)


