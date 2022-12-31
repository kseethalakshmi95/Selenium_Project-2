from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import softest



class Updateemergencycontactdetail():
    def emergency(self):


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

        personalpage = driver.find_element(By.XPATH, "//div[contains(text(),'HakanOnder N')]").click()
        emergencycontact=driver.find_element(By.XPATH,"//a[normalize-space()='Emergency Contacts']").click()

        #go to emergency contact page
        add1=driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Add'])[1]" ).click()

        name=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Dimple")
        relationship=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("married")
        telephone=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys(8459625889)
        mobile=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]").send_keys(7890543320)
        worktelephone=driver.find_element(By.XPATH,"//div[3]//div[1]//div[2]//input[1]")
        worktelephone.send_keys(2611145)
        save=driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)

        #validate for emergency contact
        dependence=driver.find_element(By.XPATH,"//a[normalize-space()='Dependents']").click()
        if save==dependence:
            print("values are validated")
        else:
            print("values are not validated")


        driver.quit()
        print("successfully stored all details")


ss=Updateemergencycontactdetail()
ss.emergency()







