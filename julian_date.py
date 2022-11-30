import pandas as pd
import finding_the_newest_file
import warnings
warnings.simplefilter("ignore")
from datetime import timedelta,datetime


def j_date(df):
    ls = df['RECID'].tolist()
    lis= []
    for i in ls :
        lis.append(i[3:8])
    return lis
#transforming one julian date into a regular date
def transforming_date(x) :
    year = x[0:2]
    input_date = year+"-01-01"
    input_date_temp = datetime.strptime(input_date, "%y-%m-%d")
    one_date_plus = input_date_temp + timedelta(days=(int(x[2:])-1))
    d = str(one_date_plus)
    return d[:10]


def t_date(x):
    ls = []
    for i in x :
       d={}
       d['REGULAR_DATE'] = transforming_date(i)
       ls.append(d)
    return ls

def add_rows(d) :

    x = j_date(d)
    ls = t_date(x)
    #df2 = pd.read_excel(open('C:/frais/bd_src/date_src/dates.xlsx','rb'),sheet_name='sheet1')
    df1 = pd.DataFrame.from_dict(ls)
    return df1
