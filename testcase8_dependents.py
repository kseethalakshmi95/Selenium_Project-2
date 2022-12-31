from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time




class Updatedependents():
    def dependents(self):


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
        #go to dependents page
        dependentspage=driver.find_element(By.XPATH,"//a[normalize-space()='Dependents']").click()


        #filling the details of dependents page
        addbutton=driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Add'])[1]").click()
        name=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        name.send_keys("Eugiene")
        relationship=driver.find_element(By.XPATH,"//label[normalize-space()='Relationship']")
        time.sleep(3)
        element = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']")
        actions = ActionChains(driver)


        actions.move_to_element(to_element=element).click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]").send_keys("jhgdd")
        time.sleep(2)
        dob=driver.find_element(By.XPATH,"//input[@placeholder='yyyy-mm-dd']")
        dob.send_keys("2021-08-12")


        buton=driver.find_element(By.XPATH,"//button[@type='submit']").click()

        time.sleep(10)

        #validating details of dependents
        job = driver.find_element(By.XPATH, "//a[normalize-space()='Job']").click()

        if buton == job:
            print("values are displayed")
        else:
            print("values are not displayed")

        driver.close()
        print("successfully entered all details")

w=Updatedependents()
w=w.dependents()

