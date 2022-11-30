
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import constant as cnst
class Scrapper (webdriver.Chrome):

    def __init__(self,driver_path=cnst.path, teardown = False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH'] +=self.driver_path
        super(Scrapper,self).__init__()
        self.implicitly_wait(30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown :
            self.quit()
    def land_first_page(self,swift):
        self.get(cnst.link)
        sc = self.find_element(By.ID, 'swift-code')
        if swift !=None :
            sc.send_keys(swift)
            my_element = self.find_element(by=By.XPATH, value='//*[@id="checker"]/div/form/button')
            self.execute_script("arguments[0].click();", my_element)
#collecting the terms of data such as
    def collect_data_term(self):
        data = []
        for i in range(2, 7):
            data_recap = self.find_element(by=By.XPATH,value='//*[@id="main"]/section[1]/div/div/div[2]/div/dl/dt[' + str(i) + ']')
            data.append(data_recap.text)

        return data
#collecting_data_for example pays : france
    def collect_data_def(self):
        data = []
        for i in range(2, 7):
            data_recap = self.find_element(by=By.XPATH,value='//*[@id="main"]/section[1]/div/div/div[2]/div/dl/dd[' + str(i) + ']')
            data.append(data_recap.text)
        return data

    def collect_data(self):
        x = cnst.b_columns
        y = self.collect_data_def()
        z = {}
        for i in range(5):
            if i == 0 :
               y[i] = y[i].strip()
            z[x[i]] = y[i]
        return z

