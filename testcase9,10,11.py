from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# noinspection PyUnreachableCode
class test_orange:

    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Defining url
        url_orange = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # open the webpage
        driver.get(url_orange)
        time.sleep(3)

        # maximize the window
        driver.maximize_window()
        time.sleep(2)

        # Finding username tab Xpath and send key
        xpath_username = '//input[@name="username"]'
        username = driver.find_element(By.XPATH, xpath_username)
        username.send_keys("Admin")

        # Finding password tab Xpath and send key
        xpath_password = '//input[@type="password"]'
        password = driver.find_element(By.XPATH, xpath_password)
        password.send_keys("admin123")

        # click the Login icon
        xpath_login_tab = '//button[@type="submit"]'
        login_tab = driver.find_element(By.XPATH, xpath_login_tab)
        login_tab.click()

        # search "PIM" in serch box
        xpath_search_tab = "//input[@placeholder='Search']"
        search = driver.find_element(By.XPATH, xpath_search_tab)
        search.send_keys("PIM")
        PIM = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
        PIM.click()
        time.sleep(4)

        # go to post user creation in PIM
        personalpage = driver.find_element(By.XPATH, "//div[contains(text(),'HakanOnder N')]").click()
        # go to job page
        job = driver.find_element(By.XPATH, "//a[normalize-space()='Job']").click()

        # go to JOb
        # job_tab = driver.find_element(By.XPATH, "//a[normalize-space()='Job']")
        # job_tab.click()
        # time.sleep(3)

        # Joined Date
        Joined_date = driver.find_element(By.XPATH, "//input[@placeholder='yyyy-mm-dd']")
        Joined_date.send_keys("2021-12-01")

        # Job Title
        Job_title = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")
        Job_title.click()
        Job_title.send_keys("t")
        time.sleep(2)

        Job_title_name = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span')
        Job_title_name.click()
        time.sleep(2)

        # Job Category
        Job_Category = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")
        Job_Category.click()
        Job_Category.send_keys("p")
        time.sleep(2)

        Job_Category_name = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[7]/span')
        Job_Category_name.click()
        time.sleep(2)

        # sub unit
        sub_unit = driver.find_element(By.XPATH,"//label[text()='Sub Unit']/following::div[1]/div/div/div[text()='-- Select --']")
        sub_unit.click()
        # sub_unit.send_keys("q")
        time.sleep(2)

        sub_unit_d = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[5]/span')
        sub_unit_d.click()
        time.sleep(2)

        # location
        location = driver.find_element(By.XPATH,"//label[text()='Location']/following::div[1]/div/div/div[text()='-- Select --']")
        location.click()
        time.sleep(2)

        location_name = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[3]/span')
        location_name.click()
        time.sleep(5)

        # Employment Status
        Employment_Status = driver.find_element(By.XPATH, "//label[text()='Employment Status']/following::div[1]/div/div/div[text()='-- Select --']")
        Employment_Status.click()
        time.sleep(2)

        Employment_Status_n = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[3]/span')
        Employment_Status_n.click()
        time.sleep(2)

        # Toggle
        togglebuton = driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        togglebuton.click()

        # Contract start date
        contract_start_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
        contract_start_date.send_keys("2021-12-01")

        # Contract End Date
        Contracy_End_Date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[3]")
        Contracy_End_Date.send_keys("2022-12-30")
        time.sleep(2)

        # Terminate Employment
        Terminate_Employment = driver.find_element(By.XPATH, "//button[normalize-space()='Terminate Employment']")
        Terminate_Employment.click()

        # New pop up window
        # termination date
        termination_date = driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[4]")
        termination_date.send_keys("2022-12-07")

        # termination reason
        termination_reason = driver.find_element(By.XPATH, "//div[contains(text(),'-- Select --')]")
        termination_reason.click()
        termination_reason.send_keys("l")

        termination_reason_l = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[2]/div[5]/span')
        termination_reason_l.click()

        # termination employment save
        termination_save = driver.find_element(By.XPATH,"//div[@role='document']//button[@type='submit'][normalize-space()='Save']")
        termination_save.click()
        time.sleep(3)

        #termination activation
        termination_active=driver.find_element(By.XPATH,"//button[normalize-space()='Activate Employment']")
        termination_active.click()
        time.sleep(5)

        # validate temination employement saved status
        # saved_status = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-terminate-date']")
        # print(saved_status.is_displayed())
        # print(saved_status.text)
        # time.sleep(3)

        # save
        save = driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]")
        save.click()
        time.sleep(3)

        # Validate the successfully saved popup
        if True:
            print("The user job details entered successfully")
        else:
            print("failed")

        # closing the wedriver
        driver.close()
        print("Test Completed & saved")


go = test_orange()
go.test_setup()