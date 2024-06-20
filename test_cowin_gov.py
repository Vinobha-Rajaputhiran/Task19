from cowin_gov import Cowin
import pytest

url='https://www.cowin.gov.in/'
Tvirus=Cowin(url)

#Test case to launch the webpage
def test_start_automation():
    assert Tvirus.start_automation() == True

#Test case to fetch the window IDs and close the respective pages
def test_fetch_windows():
    assert Tvirus.fetch_window_handles() == True

#Test Case to close the browser
def test_stop_automation():
    assert Tvirus.shutdown_automation() == None