from selenium.webdriver.common.by import By


class FormPage:
   practice_form_link = (By.XPATH,"//span[text()='Practice Form']")
   first_name = (By.ID,"firstName")
   last_name = (By.ID,"lastName")
   user_email = (By.ID,"userEmail")
   gender_male = (By.ID,"gender-radio-1")
   gender_female = (By.ID,"gender-radio-2")
   gender_other = (By.ID,"gender-radio-3")
   user_number = (By.ID,"userNumber")
   date_of_birth = (By.ID,"dateOfBirthInput")
   subject = (By.CLASS_NAME,"subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3")
   sports_hobby = (By.ID,"hobbies-checkbox-1")
   reading_hobby = (By.ID,"hobbies-checkbox-2")
   music_hobby = (By.ID,"hobbies-checkbox-3")
   upload_picture = (By.ID,"uploadPicture")
   current_address = (By.ID,"currentAddress")
   select_state = (By.XPATH,"//div[text()='Select State']")
   select_city = (By.XPATH,"//div[text()='Select City']")
   submit_button = (By.ID,"submit")


   def __init__(self, driver):
       self.driver = driver
       driver.find_element(*self.practice_form_link).click()
       #driver.maximize_window() 
       #driver.execute_script("window.scrollTo(0, 200)")
       
    
    
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

   def user_number(self, user_number):
       self.driver.find_element(*self.user_number).send_keys(user_number)
   
   def type_date_of_birth(self, date_of_birth):
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
       self.driver.find_element(*self.upload_picture).send_keys(filename)

       


           