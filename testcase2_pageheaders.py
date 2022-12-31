from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

class dropdownheader():
    def admin(self):


        driver = webdriver.Chrome()#initiating the driver instance object

        driver.maximize_window()#maximizing the browser window
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")#getting the url of the page
        driver.implicitly_wait(10)

    #finding xpath for the input fields uname and password
        uname = driver.find_element(By.NAME, "username").send_keys("Admin")
        pwd = driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(4)
        button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

        # validate menu are displaying on admin page
        menu = driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']")
        print(menu.is_displayed())
        print(menu.text)


        #go to admin page xpath
        admin = driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
        time.sleep(5)
        usermanagement=driver.find_element(By.XPATH,"//span[@class='oxd-topbar-body-nav-tab-item']/parent::li[.='User Management ']").click()
        time.sleep(2)
        user=driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()
        time.sleep(2)

        #for Admin dropdown
        user_Role = driver.find_element(By.XPATH,"//label[text()='User Role']/following::div[1]/div/div/div[text()='-- Select --']")
        ActionChains(driver).move_to_element(user_Role).click().perform()
        selecting_role = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Admin']")
        ActionChains(driver).move_to_element(selecting_role).click().perform()
        time.sleep(5)
        status = driver.find_element(By.XPATH,"//label[text()='Status']/following::div[1]/div/div/div[text()='-- Select --']")
        ActionChains(driver).move_to_element(status).click().perform()
        Status_option = driver.find_element(By.XPATH, "//div[@role='option']/span[text()='Enabled']")
        ActionChains(driver).move_to_element(Status_option).click().perform()
        time.sleep(6)

        user_Role1 = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[1]/label")
        ActionChains(driver).move_to_element(user_Role1).click().perform()
        time.sleep(2)
        ess=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
        ess.click()

        #ActionChains(driver).move_to_element(ess).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        time.sleep(5)
        status1 = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[1]/label")
        ActionChains(driver).move_to_element(status1).click().perform()
        disable = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]")
        disable.click()
        #ActionChains(driver).move_to_element(disable).click().key_down(Keys.ARROW_DOWN).perform()
        time.sleep(5)



m1=dropdownheader()
m1.admin()
