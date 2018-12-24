#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: kia
"""

from selenium import webdriver
import time
url = 'http://scores.iau-mahabad.ac.ir/loginb.aspx'
driver = webdriver.Chrome('/home/kia/Downloads/chromedriver')
driver.maximize_window()
driver.get(url)
driver.find_element_by_id('txtUserName').send_keys("960045403")
driver.find_element_by_id('txtPassword').send_keys("2860335307 ")
driver.find_element_by_xpath(".//input[@type='submit' and @name='btn_ent_stu']").click()
time.sleep(3)
print("LOGIN")
for master in range(0,3):
	print("Master:"+str(master+1))
	for qu in range(0,12):
		element = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_dataListTotalkarnameh_teacherassessment_stu_riz_'+str(master)+'_GRD_Questions_'+str(master)+'_Drp_Answer_'+str(qu)+'"]')
		for option in element.find_elements_by_tag_name("option"):
			status = "هميشه"
			status2 = "بسیار خوب"
			status = status.decode('utf-8')
			status2 = status2.decode('utf-8')
			if option.text == status:
				option.click()
				print(str("Question"+str(qu+1)))
				break
			if qu == 11:
				if option.text == status2:
					option.click()
					print(str("Question"+str(qu+1)))
					break
print(">>>>>>>> I AM PROGRAMMER <<<<<<<")
print(">>>>>>>>>>> KIA HAMEDI <<<<<<<<<")