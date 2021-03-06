from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys
import random

class FormPage:
   #selectors 
   practice_form_link = (By.XPATH,"//span[text()='Practice Form']")
   first_name = (By.ID,"firstName")
   last_name = (By.ID,"lastName")
   user_email = (By.ID,"userEmail")
   gender_male = (By.CSS_SELECTOR,"label[for='gender-radio-1']")
   gender_female = (By.CSS_SELECTOR,"label[for='gender-radio-2']")
   gender_other = (By.CSS_SELECTOR,"label[for='gender-radio-3']")
   user_number = (By.ID,"userNumber")
   date_of_birth = (By.ID,"dateOfBirthInput")
   subject = (By.ID,"subjectsInput")
   sports_hobby = (By.CSS_SELECTOR,"label[for='hobbies-checkbox-1']")
   reading_hobby = (By.CSS_SELECTOR,"label[for='hobbies-checkbox-2']")
   music_hobby = (By.CSS_SELECTOR,"label[for='hobbies-checkbox-3']")
   upload_picture = (By.ID,"uploadPicture")
   current_address = (By.ID,"currentAddress")
   state_dropdown = (By.ID,"react-select-3-input")
   city_dropdown = (By.ID,"react-select-4-input")
   submit_button = (By.ID,"submit")
   modal_close_button = (By.ID,"closeLargeModal")
   ads_close_button = (By.ID,'close-fixedban')


   def __init__(self, driver):
       self.driver = driver
       driver.find_element(*self.practice_form_link).click()
       
    
   def type_first_name(self, first_name):
       self.driver.find_element(*self.first_name).send_keys(first_name)
   
   def type_last_name(self, last_name):
       self.driver.find_element(*self.last_name).send_keys(last_name)

   def type_user_email(self, user_email):
       self.driver.find_element(*self.user_email).send_keys(user_email)    

   def select_gender(self, gender):
       if(gender == 'male'):
        self.driver.find_element(*self.gender_male).click()
       
       elif(gender == 'male'):
        self.driver.find_element(*self.gender_female).click()
       
       elif(gender == 'other'):
        self.driver.find_element(*self.gender_other).click()
       
       else:
        NameError('Invalid gender type')

   def type_user_number(self, user_number):
       self.driver.find_element(*self.user_number).send_keys(user_number)
   
   def type_date_of_birth(self, date_of_birth):
       self.driver.find_element(*self.date_of_birth).clear()
       self.driver.find_element(*self.date_of_birth).send_keys(date_of_birth)

   def type_subject(self, subject):
       self.driver.find_element(*self.subject).send_keys(subject)
   
   def select_hobby(self, *hobbies):

       for hobby in hobbies:
           if(hobby == 'sports'):
              self.driver.find_element(*self.sports_hobby).click()

           elif(hobby == 'reading'):
               self.driver.find_element(*self.reading_hobby).click()

           elif(hobby == 'music'):
               self.driver.find_element(*self.music_hobby).click()

           else:
             NameError('Invalid hobby')

   def select_file_for_picture_upload(self, filename):
       self.driver.find_element(*self.upload_picture).send_keys(os.getcwd()+'/'+filename)

   def type_current_address(self, current_address):
       self.driver.find_element(*self.current_address).send_keys(current_address)   

   def select_state_from_state_dropdown(self, state):
       self.driver.find_element(*self.state_dropdown).send_keys(state, Keys.RETURN)
       
   def select_city_from_city_dropdown(self, city):
       self.driver.find_element(*self.city_dropdown).send_keys(city, Keys.RETURN)
       

   def submit_form(self):
       self.driver.find_element(*self.submit_button).click()

   def close_modal(self):
       self.driver.find_element(*self.modal_close_button).click()
   
   def close_ads(self):
       self.driver.find_element(*self.ads_close_button).click()

   #helper method 
   def get_random_email(self):
       return 'hilsha.fish_'+str(random.randint(1,1000))+'@sea.com';    
                    