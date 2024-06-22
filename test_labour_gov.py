from labour_gov import Labour
import pytest

url='https://labour.gov.in/'
engineer=Labour(url)

#Test case to launch the webpage
def test_start_automation():
    assert engineer.start_automation() == True

#Test case to navigate to the Monthly Reports Section
def test_navigate_reports():
    assert engineer.navigate_to_monthly_reports() == True

#Test case to download the monthly report
def test_download_report():
    assert engineer.download_report() == True

#Test case to create a folder to hold the images
def test_create_media_folder():
    assert engineer.create_media_folder() == True

#Test case to navigate to the Photo Gallery section
def test_navigate_media():
    assert engineer.navigate_to_media() == True

#Test case to take screenshots
def test_screenshots():
    assert engineer.take_screenshots() == True

#Test Case to close the browser
def test_stop_automation():
    assert engineer.shutdown_automation() == None