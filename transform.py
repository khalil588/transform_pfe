import pandas as pd
pd.set_option("display.max.columns", None)
from cours import transfer_to_excel
import julian_date
from finding_the_newest_file import files_date
from bd_interm_hist import adding_new_copy
def new_data(df,df1) :
    x = df['RECID'].tolist()
    x2 = df1['RECID'].tolist()
    ls = pd.DataFrame()
    for i in  range(len(x)) :
       if x[i] not in x2 :
           d = df.loc[df['RECID'] == x[i],['COMPANY','RECID','CUSTOMER_NO','LR_ID_DEST','CHARGE_CCY','TOTAL_CHG_AMT','SWIFT_BQ_DEST','RELATED_REF','LR_REF_CORRESP','STATUS']]
           ls =ls.append(d)
    return ls

def transfer_data(df,df1,d):
    x = df['RECID'].tolist()

    x2 = df1['RECID'].tolist()
    for i in range(len(x)):
        statuts = df.loc[df['RECID'] == x[i] , 'STATUS'].tolist()
        if (x[i] not in x2 ) and (statuts[0] == 'UNPAID'):
            df.at[i,'STATUS'] = 'PAID'
            df.at[i,'DATE_CHG_TO_PAID'] = d
    return df

def swift_bq_dest(df) :
    ls = df['SWIFT_BQ_DEST'].tolist()
    ls1 = df['LR_ID_DEST'].tolist()
    ls_f =[]
    for i in range(len(ls)) :
        if type(ls[i]) == str :
            if len(ls[i]) == 12:
                x = ls[i]
                y = x[:8] + x[9:]
                ls_f.append(y)
            else :
                ls_f.append(ls[i])

        else:
            if type(ls1[i]) == str :
                if len(ls1[i]) == 12:
                    x = ls1[i]
                    y = x[:8] + x[9:]
                    ls_f.append(y)
                else :
                    ls_f.append(ls1[i])
            else:
                ls_f.append('')
    return ls_f


def swift_bq_reg(x,y):
    ls = x['CUSTOMER_NO'].tolist()
    ls_f = []
    for i in ls :
        ls2 = y.loc[y['bank_num']==i,'SWIFT_CODE'].tolist()
        if len(ls2) > 0:
            ls_f.append(ls2[0])
        else:
            ls_f.append((i))
    return ls_f

"""def id_swift(df1,df2) :
    x = df1.tolist()
    s_code = df2['SWIFT_CODE'].tolist()
    print(s_code)
    liste = []
    liste2 = []

    for i in range(len(x)):
        if type(x[i]) == str:
            y = s_code.index(x[i])
            liste.append(y+1)
        else:
            liste.append('0')
    return liste"""
def transforming(df,df3) :

    df2 = pd.read_excel(open('C:/frais/bd_src/bd_interm/bd_interm.xlsx', 'rb'), sheet_name='sheet1')

    df1 = new_data(df, df2)
    if len(df1) > 0:
        transfer_to_excel()
        z = files_date()
        y = list(z.keys())
        a = z[y[0]]
        adding_new_copy(df2)
        df_updated = transfer_data(df2, df,str(a[:10]))
        x = julian_date.add_rows(df1)
        liste = x['REGULAR_DATE'].tolist()
        df1['REGULAR_DATE'] = liste
        df1['SWIFT_BQ_DEST'] = swift_bq_dest(df1)
        df1['SWIFT_BQ_REG'] = swift_bq_reg(df1, df3)
        #df1['ID_SWIFT'] = id_swift(df1['SWIFT_BQ_DEST'],df3)
        df1['DATE_INS'] = str(a[:10])
        df1['DATE_CHG_TO_PAID'] = str(a[:10])
        df_updated = df_updated.append(df1)

        with pd.ExcelWriter('C:/frais/bd_src/bd_interm/bd_interm.xlsx') as writer:
            df_updated.to_excel(writer, sheet_name='sheet1', index=False)


"""df = pd.read_excel(open('C:/frais/bd_src/bank/bank_names.xlsx', 'rb'), sheet_name='sheet1')
df2 = pd.read_excel(open('C:/frais/bd_src/country/country.xls','rb'),sheet_name='Worksheet')
liste = df['Country'].tolist()
l1 = []
for x in liste :
    if(type(x)==str):
        if len(x) > 0 :
            y= x[len(x)-3:len(x)-1]
            y = y.upper()
            z = df2.loc[df2['alpha-2']==y,'country-code'].unique()

            l1.append(str(z[0]))
    else:
        l1.append("000")
print(len(l1))
df3 = pd.DataFrame(l1,columns=['country-code'])
df['country-code'] = df3['country-code']
with pd.ExcelWriter('C:/frais/bd_src/bank/bank_names.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1', index=False)
"""