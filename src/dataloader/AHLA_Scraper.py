from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class AHLA_Scraper():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.ahla.com/statefacts")
        self.driver.find_element_by_tag_name('body').send_keys("Keys.ESCAPE")
        iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(iframe)
        
        self.states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
                      "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
                      "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
                      "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
                      "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
                      "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                      "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
                      "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

    def _money_text_to_number(self, text):
        drop_dol = text[1:]
        
        txt_list = drop_dol.split()
        
        num = int(txt_list[0])
        zeros_str = txt_list[1]
        
        output = None
        
        if zeros_str == 'million':
            multiply = 1000000
            output = num * multiply
        elif zeros_str == 'billion':
            multiply = 1000000000
            output =  num * multiply
            
        return output
        
        

    def all_states_data(self):
        matrix = []
        for state in self.states:
            print("Collecting data for {} \n".format(state))
            state_data = []
            state_data.append(state)
            
            # Switch current state through the dropdown
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@class='select-state__select']/option[text()='{}']".format(state)))).click()

            # Get the hotel guest spending of hotels in that state
            str_spending = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div').get_attribute("innerHTML")
            tot_spendings = self._money_text_to_number(str_spending)
            state_data.append(tot_spendings)
            
            # Get the number of hotels in that state
            str_num_hotels = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div').get_attribute("innerHTML")
            num_hotels = int(str_num_hotels.replace(',', ''))
            state_data.append(num_hotels)
            
            # Get the number of rooms available in that state
            str_aval_rooms = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div').get_attribute("innerHTML")
            aval_rooms = int(str_aval_rooms.replace(',', ''))
            state_data.append(aval_rooms)

            # Get the number of jobs provided by hotel industry
            str_num_jobs = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div/div').get_attribute(
                "innerHTML")
            num_jobs = int(str_num_jobs.replace(',', ''))
            state_data.append(num_jobs)
            
            matrix.append(state_data)
        
        df = pd.DataFrame(matrix, columns=["state", "hotel_guest_spendings", "num_hotels", "num_avail_rooms", "num_jobs"])
        
        return df
        
    def save_df_as_csv(self, df):
        df.to_csv("../../data/hotel_data.csv", index=False)
    


#next > div > div > div.col-md-5 > h1 > div > div
if __name__ == "__main__":
    s = AHLA_Scraper()
    df = s.all_states_data()
    s.save_df_as_csv(df)