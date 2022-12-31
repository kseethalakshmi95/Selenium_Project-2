from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

class Createnewemployee():
    def create(self):


        driver = webdriver.Chrome()#initiating the driver instance object

        driver.maximize_window()#maximizing the browser window
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")#getting the url of the page
        driver.implicitly_wait(10)
    # for username testcase1
    #finding xpath for the input fields uname and password
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")
        pwd = driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(4)
        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        #creating new employee
        # go to admin page xpath
        admin = driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
        time.sleep(5)
        pim=driver.find_element(By.XPATH,"//a[@href='/web/index.php/pim/viewPimModule']").click()
        time.sleep(3)

        # validating menu are on the admin page
        pim = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
        if pim.is_displayed():
            print("yes it is displayed on the pim page")
        else:
            print("No its not displayed")
        time.sleep(5)

        #in pim page we are clicking add button
        add=driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
        time.sleep(2)
        toggle=driver.find_element(By.XPATH,"//input[@type='checkbox']/following::span[1]").click()
        time.sleep(5)
        firstname=driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("HakanOnder")
        middlename=driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("N")
        lastname=driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Charles")
        employeeid=driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]").send_keys(1234)
        username=driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("HakanOnder")
        pwd1=driver.find_element(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']").send_keys("HakanOnder@96")
        confpwd=driver.find_element(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']").send_keys("HakanOnder@96")
        radioenabledbutton=driver.find_element(By.XPATH,"//label[normalize-space()='Enabled']")
        save=driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)





s1=Createnewemployee()
s1.create()
