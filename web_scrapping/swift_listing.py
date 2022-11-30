import pandas as pd
import numpy as np
import constant as cnst


def swift_code_collecter(df):
    l= df['SWIFT_BQ_DEST'].tolist()
    xl = df[['LR_ID_DEST']]
    """for i in xl :
        if str(i).startswith("ABSAZ"):
           # print("ok")
    lx = xl[(len(xl['LR_ID_DEST'].str)>=8)]"""

    l3 = df.loc[df['SWIFT_BQ_DEST'].isna(),'LR_ID_DEST'].to_list()

    print(len(l3))
    ls = l+l3
    """if "ABSAZAJJCCT" in xl:
        print("ok")"""
    lis_finale = []
    for x in ls :
        if type(x) == str and x not in lis_finale:
            lis_finale.append(x)
    return  lis_finale
def swift_code_end(l):
    l2 = swift_code_collecter(l)
    l_finale = []
    for x in l2 :
        if len(x)> 0 :
            l_finale.append(x)
    return l_finale
def bank_num(df,x):
    res = df.loc[df['SWIFT_BQ_DEST']==x,'LR_ID_DEST'].unique()
    return int(res[0])
def country_code(x):
    z = ""
    if(type(x)==str):
        if len(x) > 0 :
            df2 = pd.read_excel(open('C:/frais/bd_src/country/country.xls', 'rb'), sheet_name='Worksheet')
            y = x[len(x) - 3:len(x) - 1]
            y = y.upper()
            z = df2.loc[df2['alpha-2'] == y, 'country-code'].unique()
            return str(z[0])
    else:
        return z
def country_code_sc1(x):
    z = ""
    if(type(x)==str):
        if len(x) > 0 :
            df2 = pd.read_excel(open('C:/frais/bd_src/country/country.xls', 'rb'), sheet_name='Worksheet')
            y = x[:2]
            y = y.upper()
            z = df2.loc[df2['alpha-2'] == y, 'country-code'].unique()
            return str(z[0])
    else:
        return z

def swift_code(link) :
    liste1 = swift_code_end(link)

    df = pd.read_excel(open('C:/frais/bd_src/bank/bank_names.xlsx','rb'),sheet_name='sheet1')

    liste2 = df['SWIFT_CODE'].tolist()


    liste =[]
    liste3 = []
    for i in liste2 :
        liste.append(i)

    for i in liste1 :
        if i not in liste:
            liste3.append(i)
    return liste3
