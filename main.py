import warnings
warnings.simplefilter("ignore")
import constant as cnst
import pandas as pd
from web_scrapping.web_scrapping import Scrapper
from web_scrapping.web_scr import Scrapper2
from web_scrapping.web_scr3 import Scrapper3
from web_scrapping.swift_listing import swift_code,bank_num,country_code,country_code_sc1
from finding_the_newest_file import open_sheet
from transform import transforming
#opening the new sheet
df = open_sheet()
#opening the bank names file
df2 = pd.read_excel(open(cnst.upload, 'rb'), sheet_name='sheet1')
sw_code = swift_code(df)
print(sw_code)
#web_scrapping
"""if len(sw_code ) >0 :
    liste=[]
    liste2 = []

    for x in sw_code:
        try:
            with Scrapper2(teardown=True) as bot:
                bot.land_first_page(x)
                d = bot.collect_data()
                d['bank_num'] = bank_num(df,x)
                d['country-code'] = country_code(d['Country'])
                liste.append(d)
        except:
            with Scrapper(teardown=True) as bot:
                bot.land_first_page(x)
                d = bot.collect_data()
                d['bank_num'] = bank_num(df, x)
                d['country-code'] = country_code_sc1(d['Country'])
                liste.append(d)
        else:
            with Scrapper3(teardown=True) as bot:
                bot.land_first_page(x)
                d = bot.collect_data()
                d['bank_num'] = bank_num(df, x)
                d['country-code'] = country_code(d['Country'])
                liste.append(d)
    df1 = pd.DataFrame.from_dict(liste)
    df1 = df1.iloc[:, 0:8]
    df2 = df2.append(df1)
    with pd.ExcelWriter(cnst.upload) as writer:
        df2.to_excel(writer, sheet_name='sheet1',index=False)

"""
#transforming
transforming(df,df2)


