from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time



class Updatecontactdetail():
    def contact(self):


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

        #go to contact page
        personalpage = driver.find_element(By.XPATH, "//div[contains(text(),'HakanOnder N')]").click()
        contactpage=driver.find_element(By.XPATH,"//a[normalize-space()='Contact Details']").click()

        #updating each details
        addressst1=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Rosegarden")
        st2=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
        st2.send_keys("Sojournst")
        city=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("Coimbatore")
        state=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]").send_keys("Tamilnadu")
        postalcode=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[6]").send_keys("642002")

        country=driver.find_element(By.XPATH,"//label[text()='Country']/following::div[1]")
        act=ActionChains(driver)
        ActionChains(driver).move_to_element(country).click().perform()
        select_country=driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']")
        ActionChains(driver).move_to_element(select_country).click().perform()
        time.sleep(2)
        home=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[7]")
        home.send_keys(2611147)
        mobile=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input")
        mobile.send_keys(7639309123)
        work=driver.find_element(By.XPATH,"//div[@class='oxd-input-group__label-wrapper']/following::input[8]").send_keys(123)

        time.sleep(6)
        email=driver.find_element(By.XPATH,"//div[@class='oxd-input-group__label-wrapper']/following::input[9]").send_keys("hakanonder@ehrm.com")
        time.sleep(5)
        othermail = driver.find_element(By.XPATH, "//div[3]//div[1]//div[2]//div[1]//div[2]//input[1]").send_keys("hakanonder@shrm.com")
        time.sleep(5)
        save=driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)


        #validating all fields are present

        contactpage=driver.find_element(By.XPATH,"//a[normalize-space()='Contact Details']")
        save = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        emergencycontact=driver.find_element(By.XPATH,"//a[normalize-space()='Emergency Contacts']")
        print(emergencycontact.text)
        if emergencycontact.is_displayed():
            print("All values are displayed")
        else:
            print("values not displayed")


v1=Updatecontactdetail()
v1.contact()