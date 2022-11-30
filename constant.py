import openpyxl
import pandas as pd
# les constants nécessaire pour les web_scrapping
path = r'C:/frais/package_to_install/chromedriver.exe'
link = "https://wise.com/fr/swift-codes/bic-swift-code-checker"
link2 = "https://www.ifscswiftcodes.com/SWIFT-Codes/"
link3 ="https://bank-code.net/fr/swift-code/"
clik = "arguments[0].click();"
# les contants concernant excel_adding
upload = "C:/frais/bd_src/bank/bank_names.xlsx"
# les  constants du julian date
bank_columns= ['SWIFT_CODE','Bank','Branch','Address','City','State','Country']

b_columns = ['SWIFT_CODE' ,'Bank','Address','City' ,'Country']


# bd_interm_hist link
bd_interm_hist = 'C:/frais/bd_src/bd_interm/bd_interm_hist/bd_interm_hist.xlsx'
bd_interm = 'C:/frais/bd_src/bd_interm/bd_interm.xlsx'
# cours hist
cours_hist = 'C:/frais/bd_src/cours/cours_res/cours_res_hist/cours_hist.xlsx'
cours='C:/frais/bd_src/cours/cours_res/cours.xlsx'


"""def change_bd_src():
    workbook=openpyxl.load_workbook('C:/Users/DELL/Desktop/Nouveaudossier/test.xlsx')
    x = workbook.sheetnames
    print(x[len(x)-1])
    df = pd.read_excel(open('C:/Users/DELL/Desktop/Nouveaudossier/test.xlsx','rb'),sheet_name=x[len(x)-1])
    with pd.ExcelWriter('C:/Users/DELL/Desktop/Nouveaudossier/test2.xlsx') as writer:
        df.to_excel(writer, sheet_name='sheet1', index=False)
    del workbook[x[len(x)-1]]
    workbook.save('C:/Users/DELL/Desktop/Nouveaudossier/test.xlsx')

change_bd_src()"""
