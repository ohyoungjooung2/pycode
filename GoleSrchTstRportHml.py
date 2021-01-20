from selenium import webdriver
import unittest
#pip install html-testRunner
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys

class Gsrch(unittest.TestCase):
    #@classmethod
       self.driver = webdriver.Firefox()
       #self.driver.implicitly_wait(10)
       #self.driver.maximize_window()

    def test_srch_ansible(self):
       driver=self.driver
       driver.get("https://google.com")
       elem=driver.find_element_by_name("q")
       elem.send_keys("Ansible")
       elem.send_keys(Keys.RETURN)
       assert "No result found." not in driver.page_source

PS C:\Users\oyj\seltst\sampleproj> cat .\GoleSrchTstRportHml.py
#This py script is for slenium to use firefox driver for searching ansible using google srch engine and generating html rport using html-testRunner
from selenium import webdriver
import unittest
#pip install html-testRunner
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys

class Gsrch(unittest.TestCase):
    #@classmethod
    def setUp(self):
       self.driver = webdriver.Firefox()
       #self.driver.implicitly_wait(10)
       #self.driver.maximize_window()

    def test_srch_ansible(self):
       driver=self.driver
       driver.get("https://google.com")
       elem=driver.find_element_by_name("q")
       elem.send_keys("Ansible")
       elem.send_keys(Keys.RETURN)
       assert "No result found." not in driver.page_source

#    def test_srch_ruby(self):
#       driver=self.driver
#       driver.get("https://google.com")
#       elem=driver.find_element_by_name("q")
#       elem.send_keys("ruby")
#       elem.send_keys(Keys.RETURN)
#       assert "No result found." not in driver.page_source

    def tearDown(self):
       #driver.close()
       #driver.quit()
       print("Test completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./"))
