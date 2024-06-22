"""
Using Python Selenium and the URL https://www.cowin.gov.in/  and complete the tasks given below:-

        1. Goto the Menu whose name is 'Documents' and download the monthly progress report.
        2. Goto the Menu whose name is 'Media' where you will find a sub-menu whose name is 'Photo-Gallery'.
           Your task is to download 10 photos from the webpage and save them in a folder.
           Kindly create the folder using Python.


"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import requests
import os


class Labour:


    #Construtor for the class
    def __init__(self, url):
        self.url=url
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.action_chain=ActionChains(self.driver)


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

    #Method to navigate to the Monthly Reports Section
    def navigate_to_monthly_reports(self):
        try:
            documents_locator=self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[7]/a')
            monthly_report_locator=self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[7]/ul/li[2]/a')
            self.action_chain.move_to_element(documents_locator).move_to_element(monthly_report_locator).click().perform()
            sleep(2)
            return True
        except Exception as _:
            print("Error: Unable to open the webpages")
            return False

    #Method to create a folder to hold the images
    def create_media_folder(self):
        file_name = 'WebPage_Downloads'
        os.mkdir(file_name)
        return True

    #Method to navigate to the Photo Gallery section
    def navigate_to_media(self):
        try:
            media_locator= self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[10]/a')
            photo_gallery_locator = self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[10]/ul/li[2]/a')
            self.action_chain.move_to_element(media_locator).move_to_element(photo_gallery_locator).click().perform()
            sleep(2)
            return True
        except Exception as _:
            print("Error: Unable to open the webpages")
            return False

    #Method to download the report
    def download_report(self):
        try:
            home_window_handle = self.driver.current_window_handle
            self.driver.find_element(by=By.XPATH, value='/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
            self.driver.switch_to.alert.accept()
            sleep(2)
            all_window_handle=self.driver.window_handles
            for window in all_window_handle:
                if window!=home_window_handle:
                    self.driver.switch_to.window(window)
                    current_url = self.driver.current_url
                    response = requests.get(current_url)
                    if response.status_code == 200:
                        with open("Monthly_Report.pdf", "wb") as file:
                            file.write(response.content)
                            sleep(2)
                            self.driver.switch_to.window(home_window_handle)
                            return True
                    else:
                        return "Failed to download the report"

        except Exception as _:
            print('Error:', _)
            return False

    #Method to take screenshots
    def take_screenshots(self):
        try:
                self.driver.find_element(by=By.LINK_TEXT, value='Swachhata Hi Seva').click()
                self.driver.execute_script('window.scrollBy(0,150);')
                sleep(2)
                for count in range(1,11):
                    folder_location = rf'C:\Users\Vinoba\Desktop\Workspace\selenium_python\Pytest_Introduction\WebPage_Downloads\image{count}.png'
                    self.driver.save_screenshot(folder_location)
                    self.driver.execute_script('window.scrollBy(0,525);')
                    sleep(2)
                return True
        except Exception as _:
           print('Error: ', _)
           return False

    #Method to navigate to the homepage
    def goto_homepage(self):
        self.driver.find_element(by=By.XPATH, value='/html/body/nav/div/div/div/ul/li[1]/a').click()
        sleep(2)

    #Method to close the webpage
    def shutdown_automation(self):
        self.driver.quit()
        return None

if __name__ == '__main__':

    #The WebPage URL
    url='https://labour.gov.in/'

    #Methods called
    farmers=Labour(url)
    farmers.start_automation()
    farmers.navigate_to_monthly_reports()
    farmers.download_report()
    farmers.goto_homepage()
    farmers.create_media_folder()
    farmers.navigate_to_media()
    farmers.take_screenshots()
    farmers.shutdown_automation()





