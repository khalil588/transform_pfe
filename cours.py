import  warnings
warnings.simplefilter("ignore")
import slate3k as slate
import pandas as pd
from finding_the_newest_file import pdf_filename
from constant import cours_hist,cours
from bd_interm_hist import adding_new_copy

def opening_file() :

    with open(r''+pdf_filename(),'rb') as f :
        extracted_text =slate.PDF(f).text()
        #extracted_text =slate.PDF(f)

        ls = extracted_text.split()
        x=ls.index('Monnaie')
        ls = ls [x :]
        return ls
def get_column_name(ls) :
    colonne = ls [:10]

    colonne[7: 10] = [' '.join(colonne[7: 10])]
    col = []
    col.append(colonne[-1])
    del(colonne[-1])
    colonne[5: 7] = [' '.join(colonne[5: 7])]
    col.append(colonne[-1])
    del(colonne[-1])
    colonne[3: 5] = [' '.join(colonne[3: 5])]
    col.append(colonne[-1])
    del(colonne[-1])
    while len(col) > 0 :
        colonne.append(col[-1])
        del(col[-1])
    return colonne
def transfer_line(ls = []) :
    ls[len(ls)-4: len(ls)] = [' '.join(ls[len(ls)-3: len(ls)-1])]
    liste = ls[-4:]
    del(ls[-4:])
    ls[1: len(ls)] = [' '.join(ls[1: len(ls)])]
    lst = ls +liste
    return lst
def get_lines(ls,column):
    del (ls[:10])
    liste = []
    x = []
    j = 0
    for i in range(len(ls)) :
        if ls[i].find(':') >-1 :
           x = ls[j:i+1]
           j = i+1
           liste.append(x)
    lst = []

    for i in liste :
       d = {}
       cel = transfer_line(i)
       for y in range(len(column)) :
           d[column[y]] = cel[y]
       lst.append(d)
    return lst
def transfer_to_excel():
    ls = get_lines(opening_file(), get_column_name(opening_file()))
    df1 = pd.DataFrame.from_dict(ls)
    df2 = pd.read_excel(open(cours_hist,'rb'),sheet_name='sheet1')
    adding_new_copy(df2,cours_hist)
    with pd.ExcelWriter('C:/frais/bd_src/cours/cours_res/cours.xlsx') as writer:
        df1.to_excel(writer, sheet_name='sheet1',index=False)

