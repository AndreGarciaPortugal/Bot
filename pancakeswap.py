import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import keyboard
from selenium.webdriver.chrome.options import Options as ChromeOptions

def element_presence(by, xpath, time,driver):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


## SELL - Approved Commented
def sell(contract,quantity,slippagevalor):
    chrome_options = ChromeOptions()
    chrome_options.add_extension('C:\BotMetamask\metamask.crx')

    driver = webdriver.Chrome(executable_path="C:\BotMetamask\chromedriver.exe", options=chrome_options)
    driver.get("https://v1exchange.pancakeswap.finance/#/swap?inputCurrency=" + str(contract) )
    driver.switch_to_window(driver.window_handles[-1])

    sleep(6)
    driver.find_element_by_xpath('//*[@id="understand-checkbox"]').click()
    sleep(4)
    driver.find_element_by_xpath('/html/body/reach-portal/div[3]/div/div/div/div/div/div[6]/button').click()
    #sleep(2)

    semilla = open('semilla.txt').readline().strip()
    contraseña = open('contraseña.txt').readline().strip()
    nombre_red = "Binance Smart Chain Mainnet"
    url = "https://bsc-dataseed.binance.org/"
    id_cadena = "56"

    #driver.switch_to_window(driver.window_handles[-1])
    sleep(2)
    driver.switch_to_window(driver.window_handles[0])
    element_presence(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/button', 2,driver)

    comenzar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/button')
    comenzar.click()
    sleep(4)

    importar_billetera = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button')
    importar_billetera.click()
    sleep(4)

    estoy_de_acuerdo = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[2]')
    estoy_de_acuerdo.click()
    sleep(4)

    input_semilla = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')
    input_contraseña = driver.find_element_by_xpath('//*[@id="password"]')
    input_re_contraseña = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    acepto_tyc = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
    importar = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/button')


    input_semilla.send_keys(semilla)
    input_contraseña.send_keys(contraseña)
    input_re_contraseña.send_keys(contraseña)
    acepto_tyc.click()
    sleep(2)
    importar.click()
    sleep(2)
    todo_listo = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button')
    todo_listo.click()


    element_presence(
            By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button', 15,driver)

    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/li[7]/span').click()
    sleep(2)

    input_nombre_red = driver.find_element_by_xpath('//*[@id="network-name"]')
    input_url = driver.find_element_by_xpath('//*[@id="rpc-url"]')
    input_id = driver.find_element_by_xpath('//*[@id="chainId"]')

    input_nombre_red.send_keys(nombre_red)
    input_url.send_keys(url)
    input_id.send_keys(id_cadena)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]/img[1]').click()
    sleep(2)

    #driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    #sleep(1)
    #driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    #sleep(1)

    # Cambiar de pestaña
    driver.switch_to_window(driver.window_handles[-1])
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/nav/div[2]/div[1]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="wallet-connect-metamask"]/div').click()
    sleep(2)

    driver.switch_to_window(driver.window_handles[0])
    driver.refresh()
    #driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]/img[1]').click()
    #sleep(1)
    element_presence(
            By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]', 10, driver)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    sleep(2)



    #driver.execute_script("window.open('');")
    driver.switch_to_window(driver.window_handles[-1])
    sleep(2)
    #driver.get("https://exchange.pancakeswap.finance/#/swap?inputCurrency=0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56&outputCurrency=0x190b589cf9Fb8DDEabBFeae36a813FFb2A702454")
    #sleep(1)
    #driver.find_element_by_xpath('//*[@id="understand-checkbox"]').click()
    #sleep(1)
    #driver.find_element_by_xpath('/html/body/reach-portal/div[3]/div/div/div/div/div/div[7]/button').click()

    element_presence(
            By.XPATH, '//*[@id="swap-currency-input"]/div/div[2]/input', 10, driver)
    input_moneda = driver.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[2]/input')

    input_moneda.send_keys(str(quantity))
    sleep(4)

    element_presence(
            By.XPATH, '//*[@id="swap-page"]/div[1]/div/div/h2', 60, driver)
    divclass = driver.find_element_by_xpath('//*[@id="swap-page"]/div[1]/div/div/h2')
    divclass.click()
    sleep(4)



# ------------------------APPROVE ALLOW CTA #
#     #Approve
#     element_presence(
#         By.XPATH, '//*[@id="swap-page"]/div[2]/div[2]/div[1]/button[1]', 10, driver)
#     approve = driver.find_element_by_xpath('//*[@id="swap-page"]/div[2]/div[2]/div[1]/button[1]')
#     approve.click()
#     sleep(2)
#     print("aprrove clicked")
#
#     #Metamask Approve
#     driver.switch_to_window(driver.window_handles[2])
#     print("Switched")
#     sleep(2)
#
#
#     element_presence(
#             By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]', 60, driver)
#
#     driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[2]').click()
#     print("footer clicked")
#
#
#     print("approve")

    # ------------------------FIM  ALLOW CTA #



    #BUY
    element_presence(
        By.XPATH, '//*[@id="swap-page"]/div[1]/div/button[1]', 10, driver)
    slippage = driver.find_element_by_xpath('//*[@id="swap-page"]/div[1]/div/button[1]')
    slippage.click()
    sleep(2)


    element_presence(
            By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/input', 10, driver)
    input_slippage = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/input')
    slippage_value = str(slippagevalor)
    input_slippage.clear()
    sleep(2)
    input_slippage.send_keys(slippage_value)
    sleep(5)

    element_presence(
        By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/button', 10, driver)
    exitslippage = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/button')
    exitslippage.click()

    sleep(6)
    element_presence(
            By.XPATH, '//*[@id="swap-page"]/div[2]/div[1]', 60, driver)
    divclass = driver.find_element_by_xpath('//*[@id="swap-page"]/div[2]/div[1]')
    divclass.click()
    sleep(6)


    element_presence(
            By.XPATH, '//*[@id="swap-button"]', 60, driver)
    swap = driver.find_element_by_xpath('//*[@id="swap-button"]')
    swap.click()




    sleep(6)
    driver.find_element_by_xpath('//*[@id="confirm-swap-or-send"]').click()


    sleep(2)
    driver.switch_to_window(driver.window_handles[2])

    sleep(4)


    element_presence(
            By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]', 60, driver)

    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]').click()


    sleep(6)
    driver.switch_to_window(driver.window_handles[-1])
    element_presence(
            By.XPATH, '/html/body/reach-portal[4]/div[3]/div/div/div/div/div/div[3]/button', 60, driver)
    driver.find_element_by_xpath('/html/body/reach-portal[4]/div[3]/div/div/div/div/div/div[3]/button').click()

    print("Bought " + str(contract) + " with sucess! ")

    driver.quit()
    time.sleep(2)
    #driver.execute_script("window.open('');")


##BUY
def buy(contract,quantity,slippagevalor):
    chrome_options = ChromeOptions()
    chrome_options.add_extension('C:\BotMetamask\metamask.crx')

    driver = webdriver.Chrome(executable_path="C:\BotMetamask\chromedriver.exe", options=chrome_options)
    driver.get("https://v1exchange.pancakeswap.finance/#/swap?outputCurrency=" +str(contract))
    driver.switch_to_window(driver.window_handles[-1])

    sleep(4)
    driver.find_element_by_xpath('//*[@id="understand-checkbox"]').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/reach-portal/div[3]/div/div/div/div/div/div[6]/button').click()
    #sleep(2)

    semilla = open('semilla.txt').readline().strip()
    contraseña = open('contraseña.txt').readline().strip()
    nombre_red = "Binance Smart Chain Mainnet"
    url = "https://bsc-dataseed.binance.org/"
    id_cadena = "56"

    #driver.switch_to_window(driver.window_handles[-1])
    sleep(1)
    driver.switch_to_window(driver.window_handles[0])
    element_presence(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/button', 2,driver)

    comenzar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/button')
    comenzar.click()
    sleep(2)

    importar_billetera = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button')
    importar_billetera.click()
    sleep(2)

    estoy_de_acuerdo = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[2]')
    estoy_de_acuerdo.click()
    sleep(2)

    input_semilla = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')
    input_contraseña = driver.find_element_by_xpath('//*[@id="password"]')
    input_re_contraseña = driver.find_element_by_xpath('//*[@id="confirm-password"]')
    acepto_tyc = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
    importar = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/button')


    input_semilla.send_keys(semilla)
    input_contraseña.send_keys(contraseña)
    input_re_contraseña.send_keys(contraseña)
    acepto_tyc.click()
    sleep(1)
    importar.click()
    sleep(1)
    todo_listo = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/button')
    todo_listo.click()


    element_presence(
            By.XPATH, '//*[@id="popover-content"]/div/div/section/header/div/button', 15,driver)

    driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/li[7]/span').click()
    sleep(1)

    input_nombre_red = driver.find_element_by_xpath('//*[@id="network-name"]')
    input_url = driver.find_element_by_xpath('//*[@id="rpc-url"]')
    input_id = driver.find_element_by_xpath('//*[@id="chainId"]')

    input_nombre_red.send_keys(nombre_red)
    input_url.send_keys(url)
    input_id.send_keys(id_cadena)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[4]/div/div[2]/div[2]/div/div[2]/div[2]/div[7]/button[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]/img[1]').click()
    sleep(1)

    #driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    #sleep(1)
    #driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    #sleep(1)

    # Cambiar de pestaña
    driver.switch_to_window(driver.window_handles[-1])
    sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/nav/div[2]/div[1]/button').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="wallet-connect-metamask"]/div').click()
    sleep(1)

    driver.switch_to_window(driver.window_handles[0])
    driver.refresh()
    #driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[1]/img[1]').click()
    #sleep(1)
    element_presence(
            By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]', 10, driver)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    sleep(1)



    #driver.execute_script("window.open('');")
    driver.switch_to_window(driver.window_handles[-1])
    sleep(1)
    #driver.get("https://exchange.pancakeswap.finance/#/swap?inputCurrency=0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56&outputCurrency=0x190b589cf9Fb8DDEabBFeae36a813FFb2A702454")
    #sleep(1)
    #driver.find_element_by_xpath('//*[@id="understand-checkbox"]').click()
    #sleep(1)
    #driver.find_element_by_xpath('/html/body/reach-portal/div[3]/div/div/div/div/div/div[7]/button').click()

    element_presence(
            By.XPATH, '//*[@id="swap-currency-input"]/div/div[2]/input', 10, driver)
    input_moneda = driver.find_element_by_xpath('//*[@id="swap-currency-input"]/div/div[2]/input')

    input_moneda.send_keys(str(quantity))
    sleep(1)

    element_presence(
        By.XPATH, '//*[@id="swap-page"]/div[1]/div/button[1]', 10, driver)
    slippage = driver.find_element_by_xpath('//*[@id="swap-page"]/div[1]/div/button[1]')
    slippage.click()
    sleep(1)


    element_presence(
            By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/input', 10, driver)
    input_slippage = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/input')
    slippage_value = str(slippagevalor)
    input_slippage.clear()
    sleep(1)
    input_slippage.send_keys(slippage_value)
    sleep(4)

    element_presence(
        By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/button', 10, driver)
    exitslippage = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/button')
    exitslippage.click()
    sleep(4)
    element_presence(
            By.XPATH, '//*[@id="swap-page"]/div[2]/div[1]', 60, driver)
    divclass = driver.find_element_by_xpath('//*[@id="swap-page"]/div[2]/div[1]')
    divclass.click()
    sleep(2)

    element_presence(
            By.XPATH, '//*[@id="swap-button"]', 60, driver)
    swap = driver.find_element_by_xpath('//*[@id="swap-button"]')
    swap.click()



    sleep(4)
    driver.find_element_by_xpath('//*[@id="confirm-swap-or-send"]').click()


    sleep(1)
    driver.switch_to_window(driver.window_handles[2])

    sleep(2)


    element_presence(
            By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]', 60, driver)

    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]').click()


    sleep(4)
    driver.switch_to_window(driver.window_handles[-1])
    element_presence(
            By.XPATH, '/html/body/reach-portal[4]/div[3]/div/div/div/div/div/div[3]/button', 60, driver)
    driver.find_element_by_xpath('/html/body/reach-portal[4]/div[3]/div/div/div/div/div/div[3]/button').click()

    print("Bought " + str(contract) + " with sucess! ")

    driver.quit()
    #driver.execute_script("window.open('');")



#OCTA Slippage 9
octans = '0x86c3e4ffacdb3af628ef985a518cd6ee22a22b28'

#SAFEMOON SLIPPAGE 11
safemoon = '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3'

#ELONGATE Slippage 11
elongate = '0x2A9718defF471f3Bb91FA0ECEAB14154F150a385'

#Safemars Slippage 7
safemars = '0x3ad9594151886ce8538c1ff615efa2385a8c3a88'

#STRITE Slippage 2
strite = '0x9b93c29595dd603f75854eba3c5f4ee078ee4454'

input("Presiona [ENTER] para cerrar el navegador")
try:  # used try so that if user pressed other than the given key error will not be shown
        i = 1
        random = 102303
        while i <= 10000:
                try:
                    #sell(safemoon,21404350,11)
                    #sell(elongate, 272588, 11)
                    #buy(safemars, 0.006,7)
                    #buy(strite,0.006,2)
                    #buy(octans, 0.009, 9)
                    #buy(octans, 0.005, 9)
                    #buy(octans, 0.004, 9)
                    buy(octans, 0.002, 9)
                    buy(octans, 0.002, 9)
                   # sell(octans, 53388897.530763429 + int(random), 9)
                    sell(octans, 188897.530763429 + int(random), 9)
                    buy(octans, 0.002, 9)
                    random += 453
                    print("Sold Number " + str(i))
                    i += 1
                except:
                    i = i

        print("LoopFinished")
except:
    print("error")