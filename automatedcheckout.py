from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import datetime

driver = webdriver.Firefox()
driver.get("http://ibstage.amtrak.com/")
wait = WebDriverWait(driver, 500)

element = wait.until(EC.presence_of_element_located((By.ID, "passengerInfoAnchor")));
element = driver.find_element_by_id("passengerInfoAnchor")
element.click();

#fill in passenger name
element = wait.until(EC.presence_of_element_located((By.ID, "firstname1")));
elem = driver.find_element_by_id("firstname1")
elem.click()
elem.send_keys("Test")

elem = driver.find_element_by_id("lastname1")
elem.click()
elem.send_keys("Too")

#fill in other passenger names, if applicable
try:
	elem = driver.find_element_by_id("firstname2")
	elem.click()
	elem.send_keys("Testa")
	
	elem = driver.find_element_by_id("lastname2")
	elem.click()
	elem.send_keys("Too")
except:
	pass

try:
	elem = driver.find_element_by_id("firstname3")
	elem.click()
	elem.send_keys("Testb")
	
	elem = driver.find_element_by_id("lastname3")
	elem.click()
	elem.send_keys("Too")
except:
	pass

try:
	elem = driver.find_element_by_id("firstname4")
	elem.click()
	elem.send_keys("Testc")
	
	elem = driver.find_element_by_id("lastname4")
	elem.click()
	elem.send_keys("Too")
except:
	pass
	
try:
	elem = driver.find_element_by_id("firstname5")
	elem.click()
	elem.send_keys("Testd")
	
	elem = driver.find_element_by_id("lastname5")
	elem.click()
	elem.send_keys("Too")
except:
	pass

try:
	elem = driver.find_element_by_id("firstname6")
	elem.click()
	elem.send_keys("Teste")
	
	elem = driver.find_element_by_id("lastname6")
	elem.click()
	elem.send_keys("Too")
except:
	pass	

try:
	elem = driver.find_element_by_id("firstname7")
	elem.click()
	elem.send_keys("Testf")
	
	elem = driver.find_element_by_id("lastname7")
	elem.click()
	elem.send_keys("Too")
except:
	pass
	
try:
	elem = driver.find_element_by_id("firstname8")
	elem.click()
	elem.send_keys("Testg")
	
	elem = driver.find_element_by_id("lastname8")
	elem.click()
	elem.send_keys("Too")
except:
	pass		

#enter AAA membership info if applicable
try:
	elem = driver.find_element_by_id("aaaclubcode1")
	elem.click()
	elem.send_keys("010")
	
	elem = driver.find_element_by_id("aaanumber1")
	elem.click()
	elem.send_keys("1234567")	
except:
	pass
	
#enter NARP membership info if applicable
try:
	elem = driver.find_element_by_id("narpnumber1")
	elem.click()
	elem.send_keys("123456")
except:
	pass
	
#enter Veteran's Advantage membership info if applicable
try:
	elem = driver.find_element_by_id("veteransadvantagenumber1")
	elem.click()
	elem.send_keys("9706926384")
except:
	pass
	
#enter Student Advantage membership info if applicable
try:
	elem = driver.find_element_by_id("studentadvantagenumber1")
	elem.click()
	elem.send_keys("6088516911809553")
except:
	pass

#enter Student Advantage membership info if applicable
try:
	elem = driver.find_element_by_id("isicnumber1")
	elem.click()
	elem.send_keys("123456789123")
except:
	pass
	
#fill in phone number	
elem = driver.find_element_by_id("businessphonenumber")
elem.click()
elem.send_keys("2029064406")

#fill in e-mail address
elem = driver.find_element_by_id("email_address")
elem.click()
elem.send_keys("eric.randall@amtrak.com")

elem = driver.find_element_by_id("confirm_email_address")
elem.click()
elem.send_keys("eric.randall@amtrak.com")

#click 'no' for travel insurance
elem = driver.find_element_by_id("WASCInsuranceOfferOption2")
elem.click()

#Hit 'next'
time.sleep(2)
elem = driver.find_element_by_xpath(".//div[@class='next']")
elem.click()

#insert credit card & billing information
time.sleep(5)
elem = driver.find_element_by_id("payment_cc_name")
elem.click()
elem.send_keys("Test Too")

elem = driver.find_element_by_id("creditcardprovidertype")
elem.click()
elem.send_keys("a")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("creditcardnumber")
elem.click()
elem.send_keys("370000000000002")

elem = driver.find_element_by_id("creditcardexpirymonth")
elem.click()
elem.send_keys("12")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("creditcardexpirydate")
elem.click()
elem.send_keys("2024")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("creditcardsecurityid")
elem.click()
elem.send_keys("2024")

elem = driver.find_element_by_id("billingaddressline1")
elem.click()
elem.send_keys("1600 Pennsylvania Ave NW")

elem = driver.find_element_by_id("billingcity")
elem.click()
elem.send_keys("Washington DC")

elem = driver.find_element_by_id("billingarea")
elem.click()
elem.send_keys("d")
elem.send_keys("d")
elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_id("billingpostcode")
elem.click()
elem.send_keys("20500")

#submit to terms and conditions
elem = driver.find_element_by_id("termsandconditions")
elem.click()

#hit submit
elem = driver.find_element_by_id("passenger_info_button")
elem.click()