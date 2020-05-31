import telebot
import time,os
import pyautogui
import datetime
import requests
		
date = datetime.datetime.now()

#######################################################################
            ############# Gmail Automation #############
#######################################################################


def LoadBrowser():                        #--------- Loads mozilla firefox browser                           

	pyautogui.moveTo(20,40)
	pyautogui.click()

	pyautogui.moveTo(1319,79)
	pyautogui.click()

def OpenGmail():						  #--------- Opens Gmail from favouraites list

	pageLoad = pyautogui.pixelMatchesColor(900,618,(16,39,65))

	pyautogui.moveTo(968,492)
	pyautogui.click()

	print("Loading Gmail........")
	while(not pageLoad):
		pageLoad = pyautogui.pixelMatchesColor(900,618,(16,39,65))
		
	print("Done!!\n")

def openMailThread(ThreadName):           #--------- Opens the desired mail (set ThreadName to mail ID)

	Wait = pyautogui.pixelMatchesColor(1090,301,(188,148,139))
	mailLoad = pyautogui.pixelMatchesColor(1020,368,(232,171,2))
	
	print("Opening Mailing list......")

	pyautogui.moveTo(1122,194)
	pyautogui.click()
	
	pyautogui.typewrite(ThreadName)
	pyautogui.press('enter')
		
	while(not Wait):
		Wait = pyautogui.pixelMatchesColor(1090,301,(188,148,139))
	# time.sleep(10)
	pyautogui.moveTo(1124,372,duration = 1.0)
	pyautogui.click()

	pyautogui.moveTo(1020,368)

	while(not mailLoad):
		mailLoad = pyautogui.pixelMatchesColor(1020,368,(232,171,2))
	# time.sleep(10)
	print("Opened Thread!!")

def doReplyAll():                         #-------- sets reply mode to reply all
	pyautogui.press('a')

def MailContent():						  #-------- Edit this funtion according to what you want as mail content

	pyautogui.write("Namah Shivaya\n\n", interval = 0.1)
	pyautogui.write('Tasks Done,\n', interval = 0.1)

	pyautogui.hotkey('ctrl','shift','8') 
	pyautogui.write('Went through Pohligg\nPlayed pwn2win ctf\n\n\n',interval = 0.1)
	pyautogui.hotkey('ctrl','shift','8') 

def sendMail():							 #--------- Sends email
	
	pyautogui.moveTo(1050,698, duration = 1)
	pyautogui.click()

def closeGmail():						 #--------- closes the rightmost tab

	pyautogui.moveTo(1256,78)
	pyautogui.click()

#######################################################################
            ############# Telegram bot #############
#######################################################################

##### bot data #####

bot = telebot.TeleBot("1237217742:AAHI4-pmTZRIqTt8CSUZbipHFuj1QMnsQdk")
url = 'https://api.telegram.org/bot1237217742:AAHI4-pmTZRIqTt8CSUZbipHFuj1QMnsQdk/sendMessage'
YOUR_CHAT_ID = 972187028

#-------------------#

def SendMesg(mesg):								#------------ Function to enable bot messages

	data = {'chat_id': {YOUR_CHAT_ID}, 'text': mesg}
	requests.post(url, data).json()

if date.hour == 22:
	SendMesg('Hey dont forget to send your update!!')

@bot.message_handler(commands=['start','help'])           #-------------- Sets Welcome command
def send_welcome(message):
	bot.reply_to(message, "Hey!!\nI am Dustin!!\nHere is what all I can do....")
	bot.reply_to(message,'"Open Gmail": to open gmail')


@bot.message_handler(func=lambda m: True)          #-------------- Listens for message from user
def echo_all(message):

	Terminal = 'closed'

	if message.text == "Open gmail":
		
		LoadBrowser()
		OpenGmail()
		bot.reply_to(message,"opened gmail")

	if message.text == 'Send update':
		ThreadName = "Crypto"

		LoadBrowser()
		OpenGmail()
		openMailThread(ThreadName)
		
		bot.reply_to(message,"Opened thread!")

		doReplyAll()
		MailContent()
		sendMail()

		bot.reply_to(message,"""Hey Vish your update has been sent!!\nHope you had a productive day!! :)""")


	if message.text == 'Open thread':
		ThreadName = "Crypto"

		LoadBrowser()
		OpenGmail()
		openMailThread(ThreadName)
		
		bot.reply_to(message,"Opened thread!")

		doReplyAll()
		
		SendMesg('')


	if message.text == 'Refresh':
		pyautogui.hotkey('ctrl','r')
	
	if message.text == 'Thanks Dustin' or message.text == 'Thakns':
		bot.reply_to(message,'Just doin my job vish! :D')

	if message.text == "Close tab":
		closeGmail()
		bot.reply_to(message,"Closed tab")
	
	if message.text == "Hello" or message.text == "Hey":
		bot.reply_to(message,"Howdy, Vish how are you doing?")
	
	if message.text == 'Sleep':
		bot.reply_to(message,'Laptop has been locked!')
		os.system('gnome-screensaver-command -l')

	if message.text == 'Ok':
		bot.reply_to(message,'Good!')

	if Terminal == 'active':
		os.system(message.text)

bot.polling()