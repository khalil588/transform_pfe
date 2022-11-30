
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import constant as cnst
class Scrapper2 (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper2,self).__init__()
        self.implicitly_wait(30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()
    def land_first_page(self,swift):
        link = cnst.link2+swift+".htm"
        self.get(link)

#collecting the terms of data such as
    def collect_data_term(self):
        data = []
        data_res = []
        for i in range(2, 9):
            data_recap = self.find_element(by=By.XPATH,value='//*[@id="contentcolumn1"]/div[4]/table/tbody/tr['+str(i)+']/td[1]')
            data.append(data_recap.text)
        for x in data :
            data_res.append(x[:(len(x)-1)])
        return data_res
#collecting_data_for example pays : france
    def collect_data_def(self):
        data = []
        for i in range(2, 9):
            data_recap = self.find_element(by=By.XPATH,value='//*[@id="contentcolumn1"]/div[4]/table/tbody/tr['+str(i)+']/td[2]')
            data.append(data_recap.text)
        return data

    def collect_data(self):
        x =cnst.bank_columns
        y = self.collect_data_def()
        z = {}
        for i in range(7):
            if i == 0 :
               y[i] = y[i].strip()
            z[x[i]] = y[i]
        return z

