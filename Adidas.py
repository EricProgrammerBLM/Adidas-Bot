from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import datetime, time

#THEIR ARE 3 STEPS

Complete = 50000 #STEP 1 CHANGE TO ZERO 0
CreditCard = "38738738783" #Your Credit Card number goes here
Shoe_Name = "WE ALL WE GOT RIVALRY HI SHOES" #Name of the shoe or sneaker goes here
#STEP 2
#Doesn't have to be exact but pretty close
#Name of the sneaker or shoe goes here

driver = webdriver.Chrome(executable_path=(r'C:\Users\John Doe\Desktop\Driver\chromedriver_win32\chromedriver.exe'))
driver.get('https://www.adidas.com/us?clickId=R0HRx11evxyOWTJ0TbWK8Xs3UknXVU1VW3nOQ00&cm_mmc=AdieAffiliates_IR-_-MyPoints.com%20Inc%20-%20Affiliate-_-general-_-TEXT_LINK-_-&cm_mmc2=adidas-NA-eCom-Affiliates-_-MyPoints.com%20Inc%20-%20Affiliate-_-None-None-US-always-on-None-1801&irgwc=1')

today = datetime.datetime.now()

Activate = (datetime.datetime(today.year, today.month, today.day, 23, 20, 0) - today).seconds
#Uses Military Time 23, 25, 0 = 11:25:00PM                     STEP 3 CHANGE TIME TO TIME YOU WANT TO ACTIVATE
print('Waiting for ' + str(datetime.timedelta(seconds=Activate)))
time.sleep(Activate)
#Rest of the code will activate at the correct time that you set it

driver.maximize_window()
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/form/input[1]').send_keys(Shoe_Name)
#Types the name of the sneaker in the search bar

driver.find_element_by_name('q').send_keys(Keys.RETURN)
#Presses the Enter key so we can search the site for the shoe name
driver.implicitly_wait(3)
sleep(2)


SortBy = "//button[@title='Sort By']"
def CloseBox():
    try:
        XButton = "//button[@aria-label='Close']"
        driver.find_element_by_xpath(XButton).click()
    except ElementClickInterceptedException:
        XButton = "//button[@aria-label='Close']"
        driver.find_element_by_xpath(XButton).click()
    #This is for the adidas pop up asking if we're over the age of 13


#-------------------------- Start of Continue to Check Out Function----------

def continueCheckOut(): #If causes any error just recopy script after the function and paste into the function
    driver.implicitly_wait(3)
#sleep(2)


    try:
        driver.find_element_by_xpath('/html/body/div[9]/div[2]').click()
    #Should close random adidas pop up
    except:
        print ('Continue to pick the size')
    #Didn't get the exception error yet.
    #If they ever remove the pop up this is the solution


    #NEED AN IF STATEMENT BELOW TO CHOOSE SHOE SIZES - 3/5/2020

    try:
        Size3 = "//button[@class='gl-label size___3NFO4']" #Without the selection bar, it'll choose the first size avaliable. Universal for every size chart
        driver.find_element_by_xpath(Size3).click()
        AddToBag = "//button[@data-auto-id='add-to-bag']"
        driver.find_element_by_xpath(AddToBag).click()
    except (NoSuchElementException, ElementNotInteractableException) as e:
        driver.implicitly_wait(30)
        SelectSize = "//button[@title='Select size']"
        driver.find_element_by_xpath(SelectSize).click()
        sleep(1) #Change to 1 or 2 when done
        Size3 = "//button[@class='gl-menu__element']"
    #Above is a universalexpath for every drop down size, should always click the first size in the dropdown
        driver.find_element_by_xpath(Size3).click() #We got a click
    #This is for the size chart incase it chooses to have a dropdown instead
        AddToBag = "//button[@data-auto-id='add-to-bag']"
        driver.find_element_by_xpath(AddToBag).click()
    finally:
        print ('Clicked on the size...')
#Adds it to the bag
    print ('Added to the bag')

    GoToCheckout = "//button[@data-auto-id='overlay-checkout']"
    GoToCheckout2 = "//a[@data-auto-id='overlay-checkout']"

    def CheckOutFunc():
        try:
            driver.find_element_by_xpath(GoToCheckout).click()
        except NoSuchElementException:
            driver.find_element_by_xpath(GoToCheckout2).click()
    #Clicks on the check out button


    WaitingForCheckOutPopUp = "//div[@data-auto-id='added-to-bag-modal']"
    wait = WebDriverWait(driver,900)
    wait.until(EC.presence_of_element_located((By.XPATH, WaitingForCheckOutPopUp)))

    try:
        print ('No Errors...Continue')
        CheckOutFunc() #If this causes an error, place it in the exception below
    except:
        ErrorAddTo = "//div[@data-auto-id='cart-error-message']"
        wait = WebDriverWait(driver,1)
        wait.until(EC.presence_of_element_located((By.XPATH, ErrorAddTo)))
        driver.find_element_by_xpath(AddToBag).click()
        CheckOutFunc()
#Should handle the add to bag error

    driver.implicitly_wait(20)
    driver.find_element_by_id('firstName').send_keys('Eric')
    driver.find_element_by_id('lastName').send_keys('Byam')
    driver.find_element_by_id('address1').send_keys('123 Main Street')
    driver.find_element_by_id('city').send_keys('Queens')
    driver.find_element_by_id('zipcode').send_keys('11216')

    opt = driver.find_element_by_name('stateCode')
    dropdown = Select(opt)
    dropdown.select_by_visible_text('New York')
#Was a dropdown, had to import Select

    driver.find_element_by_id('phoneNumber').send_keys('6465367483')
    driver.find_element_by_id('emailAddress').send_keys('johndoe@gmail.com')
#Filled out Shipping Details
    print ('Shipping Filled Out...')

    Review = "//button[@data-auto-id='review-and-pay-button']"
    driver.find_element_by_xpath(Review).click()

    driver.implicitly_wait(900)
#sleep(3)

    Visa = "//img[@data-auto-id='visa-icon']"
    wait = WebDriverWait(driver,900)
    wait.until(EC.presence_of_element_located((By.XPATH, Visa)))
#Should wait until the Visa image appears before it puts card numbers

    driver.find_element_by_name('card.number').send_keys(CreditCard)
    Expire = "//input[@data-auto-id='expiry-date-field']"
#sleep(2)
    wait = WebDriverWait(driver,900)
    wait.until(EC.presence_of_element_located((By.XPATH, Expire)))

    sleep(1)
    driver.find_element_by_xpath(Expire).send_keys('1234')
    driver.find_element_by_name('card.cvv').send_keys('647')
    sleep(Complete)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/button/span').click()
    print ('Order Complete')


#----------------------End-----------------------------

try:
    driver.find_element_by_xpath(SortBy).click()
except NoSuchElementException:
    CloseBox()
    try:
        continueCheckOut()
    except:
        print ('ok')


#driver.find_element_by_xpath(SortBy).click()



#Clicks the Sort By Filter Button
Newest = "//button[@value='newest-to-oldest']"
driver.find_element_by_xpath(Newest).click()
#Clicks on Newest
print ('Sorting by Newest...')

Gender = "//div[@data-auto-id='plp-collapsable-sidebar-item-container_Gender']"
try:
    driver.find_element_by_xpath(Gender).click()
except (ElementClickInterceptedException, NoSuchElementException) as e:
    XButton = "//button[@aria-label='Close']"
    driver.find_element_by_xpath(XButton).click()
    try:
        driver.find_element_by_xpath(Gender).click()
    except NoSuchElementException:
        print ('No Gender Button')
    #This is for the adidas pop up asking if we're over the age of 13

try:
    driver.find_element_by_name('Men').click()
    #Clicks on Men
    print ('Filtering by Mens Sneakers Only...')
    FirstPick = "//div[@data-index='0']"
    driver.find_element_by_xpath(FirstPick).click()
except (NoSuchElementException, StaleElementReferenceException) as e:
    print ('No Mens Filter or it Went directly to the Size Chart')

    
#FirstPick = "//div[@data-index='0']"
#driver.find_element_by_xpath(FirstPick).click()    #This was originally here
#Picks the 1st Sneaker in the row

driver.implicitly_wait(3)
#sleep(2)


try:
    driver.find_element_by_xpath('/html/body/div[9]/div[2]').click()
    #Should close random adidas pop up
except:
    print ('Continue to pick the size')
    #Didn't get the exception error yet.
    #If they ever remove the pop up this is the solution


    #NEED AN IF STATEMENT BELOW TO CHOOSE SHOE SIZES - 3/5/2020

try:
    Size3 = "//button[@class='gl-label size___3NFO4']" #Without the selection bar, it'll choose the first size avaliable. Universal for every size chart
    driver.find_element_by_xpath(Size3).click()
    AddToBag = "//button[@data-auto-id='add-to-bag']"
    driver.find_element_by_xpath(AddToBag).click()
except (NoSuchElementException, ElementNotInteractableException) as e:
    driver.implicitly_wait(30)
    SelectSize = "//button[@title='Select size']"
    driver.find_element_by_xpath(SelectSize).click()
    sleep(1) #Change to 1 or 2 when done
    Size3 = "//button[@class='gl-menu__element']"
    #Above is a universalexpath for every drop down size, should always click the first size in the dropdown
    driver.find_element_by_xpath(Size3).click() #We got a click
    #This is for the size chart incase it chooses to have a dropdown instead
    AddToBag = "//button[@data-auto-id='add-to-bag']"
    driver.find_element_by_xpath(AddToBag).click()
finally:
    print ('Clicked on the size...')
#Adds it to the bag
print ('Added to the bag')

GoToCheckout = "//button[@data-auto-id='overlay-checkout']"
GoToCheckout2 = "//a[@data-auto-id='overlay-checkout']"

def CheckOutFunc():
    try:
        driver.find_element_by_xpath(GoToCheckout).click()
    except NoSuchElementException:
        driver.find_element_by_xpath(GoToCheckout2).click()
    #Clicks on the check out button


WaitingForCheckOutPopUp = "//div[@data-auto-id='added-to-bag-modal']"
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, WaitingForCheckOutPopUp)))

try:
    print ('No Errors...Continue')
    CheckOutFunc() #If this causes an error, place it in the exception below
except:
    ErrorAddTo = "//div[@data-auto-id='cart-error-message']"
    wait = WebDriverWait(driver,1)
    wait.until(EC.presence_of_element_located((By.XPATH, ErrorAddTo)))
    driver.find_element_by_xpath(AddToBag).click()
    CheckOutFunc()
#Should handle the add to bag error

driver.implicitly_wait(20)
driver.find_element_by_id('firstName').send_keys('Eric')
driver.find_element_by_id('lastName').send_keys('Byam')
driver.find_element_by_id('address1').send_keys('123 Main Street')
driver.find_element_by_id('city').send_keys('Queens')
driver.find_element_by_id('zipcode').send_keys('16273')

opt = driver.find_element_by_name('stateCode')
dropdown = Select(opt)
dropdown.select_by_visible_text('New York')
#Was a dropdown, had to import Select

driver.find_element_by_id('phoneNumber').send_keys('6377387263')
driver.find_element_by_id('emailAddress').send_keys('johndoe@gmail.com')
#Filled out Shipping Details
print ('Shipping Filled Out...')

Review = "//button[@data-auto-id='review-and-pay-button']"
driver.find_element_by_xpath(Review).click()

driver.implicitly_wait(900)
#sleep(3)

Visa = "//img[@data-auto-id='visa-icon']"
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, Visa)))
#Should wait until the Visa image appears before it puts card numbers

driver.find_element_by_name('card.number').send_keys(CreditCard)
Expire = "//input[@data-auto-id='expiry-date-field']"
#sleep(2)
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, Expire)))

sleep(1)
driver.find_element_by_xpath(Expire).send_keys('0823')
driver.find_element_by_name('card.cvv').send_keys('377')
sleep(Complete)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/main/button/span').click()
print ('Order Complete')


