from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class UNISI_Class:
    def __init__(self,Name,link,GMeet=True,userdatadir='/chrome_app_path/google-chrome/Default'):

        self.Name = Name
        self.link = link
        self.GMeet = GMeet
        self.userdatadir = userdatadir

        #Chrome 
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument(f"--user-data-dir={userdatadir}")  # Path to chrome profile
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chromeOptions)
        
        #Firefox
        #self.userdatadir = userdatadir
        #self.driver =webdriver.Firefox(webdriver.FirefoxProfile(userdatadir))


    def Join2Class(self):
        if self.GMeet == True:
            self.driver.get(self.link)
            time.sleep(5)
            self.driver.maximize_window()            
            try:
                # Disable microphone
                self.driver.find_element(By.XPATH,"//div[@class='button_mic_div_name']").click()
            except:
                pass
            # Join2Meet
            self.driver.find_element(By.XPATH,"//div[@class='button_div_name']").click()
        else:
            pass
            # need a way to avoid webex captcha








