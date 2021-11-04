# imports stuff
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# load usernames
usernamesTxt = "usernames.txt"
usernames = []
with open(usernamesTxt) as openFile:
    for line in openFile:
        usernames.append(line.split()[0])

#log
logfile = "log.txt"
f = open(logfile, "a")
f.write("STARTED: "+ str(datetime.datetime.now()) +"\n" +
        "NAME COUNT: " + str(len(usernames)) + "\n")
f.close()


#get available users
availableusersTxt = "availableusernames.txt"
availableUsers = []
with open(availableusersTxt) as openFile:
    for line in openFile:
        availableUsers.append(line.split()[0])

# sets driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1100,500")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
browser.delete_all_cookies()

#save available users to text file
def saveAvailableUsers(username):
    if username not in availableUsers:
        availableUsers.append(user)
        f = open(availableusersTxt, "w")
        f.write("\n".join(availableUsers))
        f.close()

try:
    #load website
    browser.get('https://www.twitch.tv/signup')
    usernameInput = browser.find_element_by_id('signup-username')
    for user in usernames:

        #enter username
        usernameInput.send_keys(user)
        #while its loading wait
        while len(browser.find_elements_by_class_name('tw-loading-spinner')) > 0:
            time.sleep(0.15)
        #check if error text is there
        if browser.find_element_by_id('signup-username').value_of_css_property("border-color") == "rgb(255, 79, 77)":
            print("name "+ user +" taken or unavailable")
        else:
            print("username " + user + " available")
            saveAvailableUsers(user)
        #clear input field
        usernameInput.send_keys(Keys.CONTROL + "a")
        usernameInput.send_keys(Keys.DELETE)
finally:
    print("finished")
    browser.quit()
    f = open(logfile, "a")
    f.write("ENDED: " + str(datetime.datetime.now()) + "\n")
    f.close()





