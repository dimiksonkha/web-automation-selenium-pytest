from selenium.webdriver.common.by import By


class HomePage:
   form_page_link = (By.XPATH,"//h5[text()='Forms']")

   def __init__(self, driver):
       self.driver = driver
       driver.get('https://demoqa.com/')
       driver.maximize_window() 
       driver.execute_script("window.scrollTo(0, 200)")
       
    
    
   def visit_form_page(self):
       self.driver.find_element(*self.form_page_link).click()

       

