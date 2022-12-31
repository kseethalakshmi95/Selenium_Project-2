from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time







class Updatepersonaldetail():
    def personal(self):


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

        #go to personal page
        personalpage = driver.find_element(By.XPATH, "//div[contains(text(),'HakanOnder N')]").click()
        #Updating personal detail of the employee
        personaldetail=driver.find_element(By.XPATH,"//a[@class='orangehrm-tabs-item --active']").click()
        nickname = driver.find_element(By.XPATH, "//label[text()='Nickname']/following::div[1]/input")
        time.sleep(2)
        nickname.send_keys("Sneha")
        time.sleep(5)
        otherid = driver.find_element(By.XPATH, "//label[text()='Other Id']/following::input")
        otherid.send_keys("1999")

        license=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
        license.send_keys("123458")
        licensexperi = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
        licensexperi.send_keys("2022-12-08")
        ssnumber = driver.find_element(By.XPATH, "(//input)[10]")
        ssnumber.send_keys("908")
        sinnum = driver.find_element(By.XPATH, "(//input)[11]")
        sinnum.send_keys(250)
        nationality = driver.find_element(By.XPATH, "//label[text()='Nationality']/following::div[1]")
        action = ActionChains(driver)
        ActionChains(driver).move_to_element(nationality).click().perform()
        selecting_role = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Indian']")
        ActionChains(driver).move_to_element(selecting_role).click().perform()
        time.sleep(6)

        maritalstatus = driver.find_element(By.XPATH, "//label[text()='Marital Status']/following::div[1]")
        ActionChains(driver).move_to_element(maritalstatus).click().perform()
        status = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Married']")
        ActionChains(driver).move_to_element(status).click().perform()
        time.sleep(3)

        dob =driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
        dob.send_keys("2018-04-09")
        driver.find_element(By.XPATH, "//label[normalize-space()='Female']").click()

        gender = driver.find_element(By.XPATH, "//label[normalize-space()='Female']").is_selected()

        militryservice = driver.find_element(By.XPATH, "(//input)[15]").send_keys("2years")

        Save = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        bloodtype = driver.find_element(By.XPATH, "//label[text()='Blood Type']/following::div[1]")
        ActionChains(driver).move_to_element(bloodtype).click().perform()
        result = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='B+']")
        ActionChains(driver).move_to_element(result).click().perform()
        time.sleep(10)
        save2 = driver.find_element(By.XPATH,"//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']").click()
        time.sleep(5)

         #validate all fields are present or not
        # try:
        #     assert driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']/ancestor::div[5]/div/div")
        # except:
        #     print("exception occurred!!")

        allfields=driver.find_elements(By.XPATH,"//input[@class='oxd-input oxd-input--active']/ancestor::div[5]/div/div")
        for values in allfields:
            if values in allfields:
                print("values are present")
            else:
                print("all values are not there")


            driver.close()
            print("Successfully filled")

e1=Updatepersonaldetail()
e1.personal()
