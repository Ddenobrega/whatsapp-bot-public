from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import urbandict
import json

driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com")

element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, "b77wc"))
    )

canvas = driver.find_element_by_css_selector("canvas")
action = ActionChains(driver)




WebDriverWait(driver,120).until(EC.presence_of_element_located((By.CLASS_NAME, "_3Qnsr")))
#chat_select = input("Who Would you like to chat with: ")
#driver.find_element_by_xpath(" //*[ contains (text(), '" + chat_select + "' )]").click()
nl = "                                                                                                                                                                                                                "   

def send_message_key():
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

def message_send(ctx, args):
    print(ctx)
    #message_bar = driver.find_element_by_xpath(" //*[ contains (text(), 'Type a message')]")
    message_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')

   # message_bar.click()
    message_input.send_keys( args + nl + "*======================*" + nl + "*World's First WA bot Alpha v2.542*" + nl + "Check out my github below" + nl + "https://github.com/ddenobrega" + nl + "*---------------*" + nl)
    send_message_key()
def message_send_multiline(vargs, args):
    message_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
    if vargs > 1:
        message_input.send_keys(args + nl)
    else :
        message_input.send_keys(args + nl)
        message_ad()
        send_message_key()
def message_ad():
    message_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
    message_input.send_keys( nl + "*======================*" + nl + "*World's First WA bot Alpha v2.542*" + nl + "Check out my github below" + nl + "https://github.com/ddenobrega" + nl + "*---------------*" + nl)

    
    
    

#message_input_text = input("Test Message Send: ")
#message_send("", message_input_text)
def cmd_test(prefix, safe_group):
    driver.find_element_by_xpath(" //*[text()='" + prefix + "test']").click()
    message_send(0, "test command successful")
    driver.find_element_by_xpath(" //*[ contains (text(), '" + safe_group + "' )]").click()

def cmd_help(prefix, safe_group):
    driver.find_element_by_xpath(" //*[text()='" + prefix + "help']").click()
    message_input = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[1]/div')
    message_input.send_keys("Coming SOON")
    send_message_key()
    driver.find_element_by_xpath(" //*[ contains (text(), '" + safe_group + "' )]").click()

def cmd_arg(prefix, safe_group):
     args = driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "args' )]").text
     parsed = args.removeprefix("$d.args")
     driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "arg' )]").click()
     print(parsed)
     message_send(0, parsed)
     driver.find_element_by_xpath(" //*[ contains (text(), '" + safe_group + "' )]").click()


def cmd_urban(prefix, safe_group):
    args = driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "urban' )]").text
    parsed =  args.removeprefix("$d.urban")
    args = driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "urban' )]").click()
    define = urbandict.define(parsed)
    parsed2 = json.dumps(obj=define, indent=nl)
    parsed3 = parsed2.replace("[", "*URBAN DICTIONARY*")
    parsed4 = parsed3.replace("{", "```Definition Start```")
    parsed5 = parsed4.replace("}", "```Definition End```")
    parsed6 = parsed5.replace(': \"', "  ")
    parsed7 = parsed6.replace("\",", " ")
    message_send("parsing urban", "parsing please wait")
    message_send(0, parsed7)
    driver.find_element_by_xpath(" //*[ contains (text(), '" + safe_group + "' )]").click()

def cmd_spam(prefix, safe_group):
    args = driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "spam' )]").text
    driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "spam' )]").click()
    parse = args.removeprefix("$d.spam")
    i = 0 
    iargs = 100
    while iargs > i:
        message_send(0, parse)
        i = i + 1





def bot(): 
    prefix = "$d."
    sfg = "test group"

    while True:
        try:
            while True:
                driver.find_element_by_xpath(" //*[ contains (text(), '" + prefix + "' )]")
                while True:
                    try: 
                        cmd_test(prefix, sfg)
                    except:
                        break
                while True:
                    try:
                        cmd_help(prefix, sfg)
                    except:
                        break
                while True:
                    try:
                        cmd_arg(prefix, sfg)
                    except:
                        break
                while True:
                    try:
                        cmd_urban(prefix, sfg)
                    except:
                        break
                while True:
                    try:
                        cmd_spam(prefix, sfg)
                    except:
                        break

        except:
            print("awaiting command")
            sleep(1)

bot()
