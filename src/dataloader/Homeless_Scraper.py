from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


class Homeless_Scraper():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.usich.gov/tools-for-action/map/#fn[]=1400&fn[]=2800&fn[]=6200&fn[]=10000&fn[]=13200")
        
        self.states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
                       "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
                       "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
                       "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
                       "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
                       "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                       "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                       "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        
        self.states_abr = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia',
                           'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm',
                           'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa',
                           'wv', 'wi', 'wy']

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
            output = num * multiply
    
        return output
    
    def all_states_data(self):
        matrix = []
        for idx in range(len(self.states_abr)):
            state_data = []
            state_data.append(self.states[idx])
            
            self.driver.get("https://www.usich.gov/homelessness-statistics/{}".format(self.states_abr[idx]))
            
            tot_pop = self.driver.find_element_by_xpath("/html/body/div[3]/div[6]/div[1]/ul/li[1]/p").text
            tot_pop = int(tot_pop.replace(',', ''))
            state_data.append(tot_pop)
            
            tot_household = self.driver.find_element_by_xpath("/html/body/div[3]/div[6]/div[1]/ul/li[2]/p").text
            tot_household = int(tot_household.replace(',', ''))
            state_data.append(tot_household)
            
            tot_young_adults = self.driver.find_element_by_xpath("/html/body/div[3]/div[6]/div[1]/ul/li[5]/p").text
            tot_young_adults = int(tot_young_adults.replace(',', ''))
            state_data.append(tot_young_adults)
            
            tot_students = self.driver.find_element_by_xpath("/html/body/div[3]/div[6]/div[1]/ul/li[6]/p").text
            tot_students = int(tot_students.replace(',', ''))
            state_data.append(tot_students)
            
            matrix.append(state_data)
        
        df = pd.DataFrame(matrix, columns=["state", "tot_homeless_population", "tot_household_homelessness", "young_adult_homelessness",
                                           "tot_homeless_students"])

        self.driver.quit()
        return df

    
    def save_df_as_csv(self, df):
        df.to_csv("../../data/homeless_data.csv", index=False)


if __name__ == "__main__":
    h = Homeless_Scraper()
    df = h.all_states_data()
    h.save_df_as_csv(df)
    
    