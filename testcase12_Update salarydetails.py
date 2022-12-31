from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import softest



class Updatesalary():
    def salary(self):


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

        #go to salary details page
        salarypage=driver.find_element(By.XPATH,"(//a[normalize-space()='Salary'])[1]").click()

        #fiull the salry details page
        add=driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Add'])[1]").click()
        time.sleep(3)
        #xpath for salary component
        salarycomponent=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("gghjjhjhjhkj")
        #xpath for pay grade
        paygrade=driver.find_element(By.XPATH,"//label[text()='Pay Grade']/following::div[1]/div/div/div[text()='-- Select --']")
        act=ActionChains(driver)
        act.move_to_element(paygrade).click().send_keys(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        time.sleep(5)
        #xpath for payfrequency
        payfrequency=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")
        act.move_to_element(payfrequency).click().send_keys(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        time.sleep(5)
        currency=driver.find_element(By.XPATH,"//label[text()='Currency']/following::div[1]/div/div/div[text()='-- Select --']")
        currency.send_keys("i")
        act.move_to_element(currency).send_keys(Keys.ENTER).perform()
        time.sleep(5)
        amount=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]").send_keys(50000)
        time.sleep(2)
        comments=driver.find_element(By.XPATH,"(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical'])[1]").send_keys("ahdfjvrubvjbiwehwbr")
        time.sleep(3)


        toggle=driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(5)
        accountnumber=driver.find_element(By.XPATH,"//div[4]//div[1]//div[1]//div[1]//div[2]//input[1]").send_keys("128923456")
        time.sleep(5)
        routingnumber=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[5]").send_keys(12343)
        time.sleep(5)
        amount=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input").send_keys(50000)
        time.sleep(4)
        accounttype = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")

        act.move_to_element(accounttype).click().perform()

        selecting_accounttype = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span')

        act.move_to_element(selecting_accounttype).click().perform()

        time.sleep(3)

        savebtn=driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(5)


        #validating each details
        taxexemption = driver.find_element(By.XPATH, "(//a[normalize-space()='Tax Exemptions'])[1]").click()

        if savebtn==taxexemption:
            print("values are succesfully validated")
        else:
            print("values are not updated")
            

        driver.close()
        print("Successfully completed")
s1=Updatesalary()
s1.salary()