#Made by Dennis Sarsozo during Prometheus Group QA Internship Summer 2020 (CLEANED)
#Python Selenium Script to auto-login into CLIENT's Testing Enviroment with Grid Card Credential. 
#Requires selenium and chrome driver to be installed.
#python 3.8.3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# #Intialize the CLIENT's Grid Card (FAKE)
# #row1 = ['AB','CD','EF','GH','IJ','KL','MN','OP','QR','ST']
# #row2 = ['UV','WX','YZ','A1','B2','C3','D4','F5','G6','H7']
# #row3 = ['I8','J9','K1','1L','2M','3N','4O','5P','6Q','7R']
# #row4 = ['8S','9T','ZA','YB','XC','A6','8H','L3','2D','PO']
# #row5 = ['33','53','Q5','HH','LM','WS','99','L3','J7','3F']
#Create the grid card as a 2D array
gridCard = [['AB','CD','EF','GH','IJ','KL','MN','OP','QR','ST'], ['UV','WX','YZ','A1','B2','C3','D4','F5','G6','H7'], ['I8','J9','K1','1L','2M','3N','4O','5P','6Q','7R'], ['8S','9T','ZA','YB','XC','A6','8H','L3','2D','PO'], ['33','53','Q5','HH','LM','WS','99','L3','J7','3F']]
#Use a Dictionary to convert letters to their column number abstraction.
letterColumnDictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

#Function to get the key values in the Card cell.
def gridcard_algo(cell):
    #Grab the letter (which represents the column on the Security Card)
    letter = cell[0]
    #Get the row number
    row = int(cell[1]) - 1
    #Translate the column letter to the column number in the gridCard 2D array.
    column = letterColumnDictionary.get(letter)
    #Return the specific key value.
    return gridCard[row][column]
  
#Open Client's Login Page for Testing Enviroment
driver = webdriver.Chrome()
driver.get("/testingclient-login.html")

#Username and password
driver.implicitly_wait(8) # Wait 8 seconds for the page to load & select input boxes.
driver.find_element_by_id("Enter user name").send_keys("testing.user.external@client.com")
driver.find_element_by_id("passwd").send_keys("ahskjdl123!@#$&*") #fake password, sorry hackers 👿

#Login
driver.find_element_by_id("Log_On").click()

#Grab Challenge
driver.implicitly_wait(5) # Wait 5 seconds for the page to load & select input boxes.
rawDialogue = driver.find_element_by_id("dialogueStr").text
print("grabbed", rawDialogue)

#Seperate trash and get challenge.
posFirstBracket = rawDialogue.find('[')
challenge = rawDialogue[posFirstBracket:posFirstBracket + 15]
challenge = challenge.replace(" ", "")
print("cleaned:", challenge)

#Get correct code from gridcard array
print("cell 1:",challenge[1:3])
print("cell 2:",challenge[5:7])
print("cell 3:",challenge[9:11])

#Now that we got the challenge, get the keys.
answer = ""
#grab first cell
answer += gridcard_algo(challenge[1:3])
#grab second cell
answer += gridcard_algo(challenge[5:8])
#grab third cell
answer += gridcard_algo(challenge[9:11])
print("ANSWER:", answer)

#Submit
driver.find_element_by_id("response").send_keys(answer)
#Login
driver.find_element_by_id("SubmitButton").click()

#Open the client's cloud software (passes the credentials)
driver.implicitly_wait(5) # Wait 5 seconds for the page to load & select input boxes.
driver.find_element_by_id("protocolhandler-welcome-installButton").click()
