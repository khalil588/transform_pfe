import glob
import pandas as pd
import os
import time
import xlrd
#creating a list full of the file's names under the directory needed
def ls_file(link):
    y = glob.glob(link)
    return y


#searching for the newest file
def finding_creation_date(x):

    ti_c = os.path.getctime(x)
    c_ti = time.ctime(ti_c)

    # Using the timestamp string to create a
    # time object/structure
    t_obj = time.strptime(c_ti)

    # Transforming the time object to a timestamp
    # of ISO 8601 format
    T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
    return T_stamp
def files_date(link ="c:/frais/bd_src/*.xlsx"):
    z = {}
    df = pd.DataFrame(ls_file(link), columns=['names'])
    df['creation_time'] = df.apply(lambda df : finding_creation_date(df['names']),axis=1)
    x = df['creation_time'].max()
    y = df.loc[df['creation_time']==x,'names'].values.item()
    z[y] = df.loc[df['names']==y,'creation_time'].values.item()
    return z

def sheet_name(x):
    xls = xlrd.open_workbook(r''+x, on_demand=True)
    sheet=xls.sheet_names()
    return sheet[0]

def open_sheet():
    file_name =next(iter(files_date()))
    df = pd.read_excel(open(file_name,'rb'),sheet_name=sheet_name(file_name))
    return df
def pdf_filename():
    x = next(iter(files_date('C:/frais/bd_src/cours/cours_recu/*.pdf')))
    return x


