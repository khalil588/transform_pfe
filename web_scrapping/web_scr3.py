
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import constant as cnst
class Scrapper3 (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper3,self).__init__()
        self.implicitly_wait(30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()
    def land_first_page(self,swift):
        link = cnst.link3+swift+".html"
        self.get(link)


#collecting the terms of data such as
    def collect_data_term(self):
        data = []
        data_res = []
        for i in range(2, 10):
            data_recap = self.find_element(by=By.XPATH,value='/html/body/div[2]/table/tbody/tr['+str(i)+']/th[2]')
            data.append(data_recap.text)
        for x in data :
            data_res.append(x[:(len(x)-1)])
        return data_res


#collecting_data_for example pays : france
    def collect_data_def(self):
        data = []
        for i in range(2, 10):
            if i  == 5 :
                data_recap = self.find_element(by=By.XPATH,value='/html/body/div[2]/table/tbody/tr['+str(i)+']/th[2]')
                data.append(data_recap.text)
            else:
                data_recap = self.find_element(by=By.XPATH,value='/html/body/div[2]/table/tbody/tr['+str(i)+']/th[2]')
                data.append(data_recap.text)
        return data

    def collect_data(self):
        x =cnst.bank_columns
        y = self.collect_data_def()
        z = {}
        a = y[0]+y[3]
        z[x[0]] = a.strip()
        z[x[1]] = y[1]
        z[x[2]] = y[2][1 : -1]
        z[x[3]] = y[7]
        z[x[4]] = y[6]
        z['state'] = ""
        z[x[6]] = y[5]
        return z

