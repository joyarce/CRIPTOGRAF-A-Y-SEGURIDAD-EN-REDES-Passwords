

    import unittest
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    import pyautogui
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import os
    import msvcrt as m
    import random
    import string
    ## sudo pip install names ##
    import names  
    from selenium.common.exceptions import TimeoutException


    def Randomfakeemail(length):
        email = ''.join(random.choice(string.ascii_letters) for x in range(length))
        print("Random fake email is:",email+"@gmail.com")
        return(email+"@gmail.com")
    def Randompassword(length):
        password_characters = string.ascii_letters + string.digits + string.punctuation + string.printable
        password = ''.join(random.choice(password_characters) for i in range(length))
        print("Random string password is:", password)
        return(password)

    class SitioCL():

        def setUp(self):
            self.driver = webdriver.Chrome()
            driver = self.driver
        def Registro(self):
            driver = self.driver
            driver.get("DIRECCION-SITIO-CHILENO")
            try:
                gen = random.randint(1,2) # Genero usuario aleatorio
                if gen == 1:
                    driver.find_element_by_css_selector("input[type='radio'][value='1']").click() 
                else:
                    driver.find_element_by_css_selector("input[type='radio'][value='2']").click()

                nombre =  driver.find_element_by_xpath("//*[@id='customer-form']/section/div[2]/div[1]/input")
                apellidos = driver.find_element_by_xpath("//*[@id='customer-form']/section/div[3]/div[1]/input")  
                email = driver.find_element_by_xpath("//*[@id='customer-form']/section/div[4]/div[1]/input")
                pw = driver.find_element_by_xpath("//*[@id='customer-form']/section/div[5]/div[1]/div/input")
                nombre.send_keys(names.get_first_name())
                apellidos.send_keys(names.get_last_name())
                email.send_keys(Randomfakeemail(5))
                pw.send_keys(Randompassword(7))
                time.sleep(2)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='customer-form']/footer/button"))).click() 
                
            except:
                driver.find_element_by_xpath("//*[@id='PopupSignupForm_0']/div[2]/div[1]").click()
                self.Registro()
        def Logear(self,correo,password):
            driver = self.driver
            driver.get("DIRECCION-SITIO-CHILENO-INICIAR-SESION")
            time.sleep(3)
            try:

                email = driver.find_element_by_xpath("//*[@id='login-form']/section/div[1]/div[1]/input")
                pw = driver.find_element_by_xpath("//*[@id='login-form']/section/div[2]/div[1]/div/input")
                email.send_keys(correo)
                pw.send_keys(password)
                time.sleep(3)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='login-form']/footer/button"))).click() 
            except:
                driver.find_element_by_xpath("//*[@id='PopupSignupForm_0']/div[2]/div[1]").click()
                self.Logear(correo,password)
        def Restablecer(self,correo):
            driver = self.driver
            driver.get("DIRECCION-SITIO-CHILENO-RECUPERAR-PW")
            time.sleep(3)
            try:
                email = driver.find_element_by_xpath("//*[@id='email']")
                email.send_keys(correo)
                time.sleep(3)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/form/section/div/button[2]"))).click() 
            except:
                driver.find_element_by_xpath("//*[@id='PopupSignupForm_0']/div[2]/div[1]").click()
                self.Restablecer(correo)

        def Modificar(self,correo,ctpw,nwpw):

            self.Logear(correo,ctpw)
            driver = self.driver
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='identity-link']/span "))).click() 
            time.sleep(3)
            try:
                currentpw = driver.find_element_by_xpath("//*[@id='customer-form']/section/div[5]/div[1]/div/input")
                newpw = driver.find_element_by_xpath("//*[@id='customer-form']/section/div[6]/div[1]/div/input")
                currentpw.send_keys(ctpw)
                newpw.send_keys(nwpw)
                time.sleep(3)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='customer-form']/footer/button"))).click()
            except:
                driver.find_element_by_xpath("//*[@id='PopupSignupForm_0']/div[2]/div[1]").click()
                self.Modificar(correo,ctwp,nwpw)


    class SitioEU():

        def setUp(self):
            self.driver = webdriver.Chrome()
            driver = self.driver
        def Registro(self):
            driver = self.driver
            driver.get("DIRECCION-SITIO-EU-CREAR-CUENTA")
            time.sleep(2)
            try:
                nombre = driver.find_element_by_name('firstname')
                apellidos = driver.find_element_by_name('lastname')
                email = driver.find_element_by_name('email')
                pw = driver.find_element_by_name('password')
                repeatpw = driver.find_element_by_name('confirmation')

                nombre.send_keys(names.get_first_name())
                apellidos.send_keys(names.get_last_name())
                email.send_keys(Randomfakeemail(7))
                password = Randompassword(7)
                pw.send_keys(password)
                repeatpw.send_keys(password)
                time.sleep(2)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section/section/section/div[4]/div/div/div/div/div/form/div[3]/button"))).click()
            except:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section/section/div/div/div[2]/a/button"))).click()
        def Logear(self,correo,password):
            driver = self.driver
            driver.get("DIRECCION-SITIO-EU-LOGIN")
            time.sleep(3)
            try:
                email = driver.find_element_by_xpath("//*[@id='email']")
                pw = driver.find_element_by_xpath(" //*[@id='pass'] ")
                email.send_keys(correo)
                pw.send_keys(password)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='send2']"))).click()
            except:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section/section/div/div/div[2]/a/button"))).click()
        def Restablecer(self,correo):

            driver = self.driver
            driver.get("DIRECCION-SITIO-EU-RECUPERARPW")
            time.sleep(2)
            try:
                email = driver.find_element_by_xpath("//*[@id='email_address']")
                email.send_keys(correo)
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='form-validate']/div[2]/button"))).click()
            except:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"/html/body/section/section/div/div/div[2]/a/button"))).click()

        

    if __name__ == "__main__":

        x = SitioEU()
        x.setUp() 
        x.Registro()
        """for i in range(1, 101):
            print("Iteracion :",i)
            x.Logear("hVyoQug@gmail.com","123456")"""

