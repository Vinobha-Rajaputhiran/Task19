"""
Using Python Selenium and the URL https://www.cowin.gov.in/ you have to:-

        1. Click on the 'FAQ' and 'Partners' anchor tags present on the Home page and open two new windows.
        2. Now you have to fetch the Windows/Frame IDs and display the same on the console.
        3. kindly close the two new windows and come back to the Home page.

"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class Cowin:

    # Locators Data
    faq_locator = '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a'
    partners_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"

    #Construtor for the class
    def __init__(self, url):
        self.url=url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))


    #Method to start the webpage automation
    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)
            return True

        except Exception as _:
            print("Error: Unable to Start Python Automation")
            return False

    #Method to open multiple webpages and fetch the Window IDs
    def open_windows(self):
        if self.start_automation():
            home_window_handle = self.driver.current_window_handle
            self.driver.find_element(by=By.XPATH, value=self.faq_locator).click()
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=self.partners_locator).click()
            sleep(2)
            self.driver.switch_to.window(home_window_handle)
            sleep(2)
            return True
        else:
            print("Error: Unable to open the webpages")

    #Method to fetch the window handles and close the webpages
    def fetch_window_handles(self):
        try:
            home_window_handle = self.driver.current_window_handle
            all_window_handles = self.driver.window_handles
            for window in all_window_handles:
                if window != home_window_handle:
                    self.driver.switch_to.window(window)
                    sleep(2)
                    print(self.driver.current_window_handle)
                    self.driver.close()
            return True
        except Exception as _:
            print("Error: Unable to close the webpages")


    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None


if __name__ == '__main__':

    #The WebPage URL
    url='https://www.cowin.gov.in/'

    #Methods called using object
    covid=Cowin(url)
    covid.start_automation()
    covid.open_windows()
    print("The Window IDs are: ")
    covid.fetch_window_handles()
    covid.shutdown_automation()





