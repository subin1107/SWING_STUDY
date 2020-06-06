from selenium import webdriver

driver=webdriver.Chrome('C:/Users/btsiu/Desktop/chromedriver_win32/chromedriver.exe')
driver.get('http://zzzscore.com/1to50/')

num=1
while(1):
    btns=driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    
    for btn in btns:
        if btn.text==str(num):
            btn.click()
            print("number " + str(num) +" clicked!")
            num+=1
    if num>50:
            break
