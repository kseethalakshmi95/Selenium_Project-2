from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time

class OrangeDemoproject():
    def search(self):


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
        time.sleep(5)



        # search "Admin" in serch box & validate (both Uppercase and lowercase)
        xpath_search_tab = "//input[@placeholder='Search']"
        driver.find_element(By.XPATH, xpath_search_tab).send_keys("admin")
        search = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
        print(search.is_displayed())
        print(search.text)

        # validate the menu options on side pane) are displaying on admin page
        menu = driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']")
        print(menu.is_displayed())
        print(menu.text)

        #validating the search(textbox)
        search =driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']")
        print(search.is_displayed())
        time.sleep(4)


        #typing module as lowercase
        search=driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("admin")
        # validating menu are on the admin page
        # admin = driver.find_element(By.XPATH,"//span[text()='Admin']")
        # print(admin.get_attribute("innerHTML"))
        # if 'Admin'==admin.get_attribute("innerHTML"):
        #     print("It is present")
        # else:
        #     print("It is not present")
    #for pim
        act = ActionChains(driver)
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("pim")
        #
        time.sleep(4)
        #
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        # #for leave
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("leave")
        time.sleep(3)
        # #for time
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("time")
        time.sleep(2)
        # #for Recruitment
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("recruitment")
        time.sleep(2)
        # #My info
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("my info")
        time.sleep(2)
        # #for performance
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("performance")
        time.sleep(2)
        # #for dashboard
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("dashboard")
        time.sleep(2)
        # #for directory
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("directory")
        time.sleep(2)
        # #for Maintenance
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("maintenance")
        time.sleep(2)
        #
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("buzz")
        time.sleep(2)
        #
        #
        # #searching with uppercase
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        search=driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("ADMIN")
        time.sleep(5)
        # #for pim
        act = ActionChains(driver)
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("PIM")
        #
        time.sleep(4)

        # #for leave
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("LEAVE")
        time.sleep(3)
        # #for time
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("TIME")
        time.sleep(2)
        # #for Recruitment
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("RECRUITMENT")
        time.sleep(2)
        # #My info
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("MY INFO")
        time.sleep(2)
        # #for performance
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("PERFORMANCE")
        time.sleep(2)
        # #for dashboard
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("DASHBOARD")
        time.sleep(2)
        # #for directory
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("DIRECTORY")
        time.sleep(2)
        # #for Maintenance
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        #
        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("MAINTENANCE")
        time.sleep(2)
        #
        act.click(driver.find_element(By.XPATH, "//input[@placeholder='Search']")).key_down(Keys.CONTROL).send_keys( "a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

        driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("BUZZ")


tree=OrangeDemoproject()
tree.search()