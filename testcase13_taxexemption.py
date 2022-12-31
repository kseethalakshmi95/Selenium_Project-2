from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import softest


class Updatetaxexemptiondetail():
    def tax(self):
        driver = webdriver.Chrome()  # initiating the driver instance object

        driver.maximize_window()  # maximizing the browser window
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # getting the url of the page
        driver.implicitly_wait(10)
        # for username testcase1
        # finding xpath for the input fields uname and password
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")
        pwd = driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(4)
        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        # creating new employee
        # go to admin page xpath
        admin = driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
        time.sleep(5)
        pim = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']").click()
        time.sleep(3)

        personalpage = driver.find_element(By.XPATH, "//div[contains(text(),'HakanOnder N')]").click()

        #go to taxexemption page
        taxexemption=driver.find_element(By.XPATH,"(//a[normalize-space()='Tax Exemptions'])[1]").click()

        #filling all details
        #finding xpath for status
        status=driver.find_element(By.XPATH,"//label[text()='Status']/following::div[1]")

        act1=ActionChains(driver)
        act1.move_to_element(status).click().send_keys(Keys.ENTER).perform()
        sel=driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
        act1.move_to_element(sel).click().key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
        time.sleep(5)

        #finding xpath for Exemptions
        exemption=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(1)
        time.sleep(4)

        #federal income tax
        #finding xpath for state
        state=driver.find_element(By.XPATH,"//label[text()='State']/following::div[1]")
        act1.move_to_element(state).click().key_down(Keys.ENTER).perform()
        time.sleep(5)
        ele1=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]")
        act1.move_to_element(ele1).click().key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        #finding xpath for status
        status=driver.find_element(By.XPATH,"//div[@class='orangehrm-edit-employee-content']//div[2]//div[1]//div[2]//div[1]//div[1]//label[1]")
        act1.move_to_element(status).click().perform()
        ele=driver.find_element(By.XPATH,"//div[@class='oxd-form-row']//div[2]//div[1]//div[2]//div[1]//div[1]//div[1]")
        act1.move_to_element(ele).click().key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER)
        time.sleep(4)



        #finding xpath for unemployment
        unemploystate=driver.find_element(By.XPATH,"//label[text()='Unemployment State']/following::div[1]")
        act1.move_to_element(unemploystate).click().key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        sel1=driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]")
        act1.move_to_element(sel1).click().key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(5)

        #xpath for exemptions
        exemption=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]").send_keys(1)
        time.sleep(5)

        #xpath of work state
        workstate=driver.find_element(By.XPATH,"//label[text()='Work State']/following::div[1]")
        act1.move_to_element(workstate).click().perform()
        sel3=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]")
        act1.move_to_element(sel3).click().key_down(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(5)

        #xpath for save
        save=driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(6)

        #validating all fields
        reportto=driver.find_element(By.XPATH,"//a[normalize-space()='Report-to']")
        if save==reportto:
            print("All fields are successfully validated")
        else:
            print("All fields are not validated")


        driver.close()
        print("Successfully completed")




te=Updatetaxexemptiondetail()
te.tax()