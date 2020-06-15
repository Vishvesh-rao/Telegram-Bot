####################################################
    ############ Imporetd Modules ############

import telebot
import requests
import os
import pyautogui
from datetime import *
import time
from timeloop import Timeloop

####################################################

date = datetime.now()
tl = Timeloop()
repeat1 = False
repeat2 = False

#######################################################################
            ############# Gmail Automation #############
#######################################################################


def LoadBrowser():                        #--------- Loads chrome browser                           

	pyautogui.moveTo(0,479)
	pyautogui.click()

	pyautogui.moveTo(1346,43)
	pyautogui.hotkey('ctrl','t')

	pyautogui.click(876,516,duration = 2)

#_________________________________________

def OpenGmail():						  #--------- Opens Gmail from favouraites list

	pageLoad = pyautogui.pixelMatchesColor(868,181,(171,144,145))

	pyautogui.moveTo(868,181)
	pyautogui.click()

	print("Loading Gmail........")
	# while(not pageLoad):
	# 	pageLoad = pyautogui.pixelMatchesColor(868,181,(171,144,145))
	time.sleep(5)
	print("Done!!\n")

#_________________________________________


def openMailThread(ThreadName):           #--------- Opens the desired mail (set ThreadName to mail ID/Subject)
	
	SendMesg('Opening Thread')

	Wait = pyautogui.pixelMatchesColor(925,290,(204,185,177))
	mailLoad = pyautogui.pixelMatchesColor(969,343,(255,255,255))
	
	print('Scanning for mail')
	
	pyautogui.moveTo(1063,187)
	pyautogui.click()
	
	pyautogui.typewrite(ThreadName)
	pyautogui.press('enter')
	pyautogui.moveTo(925,290)
		
	while(not Wait):
		Wait = pyautogui.pixelMatchesColor(925,290,(204,185,177))
	#time.sleep(8)
	print("Opening Mailing list......")

	pyautogui.moveTo(1124,372)
	pyautogui.click()

	pyautogui.moveTo(969,343)

	while(not mailLoad):
		mailLoad = pyautogui.pixelMatchesColor(969,343,(255,255,255))
	#time.sleep(10)
	print("Opened Thread!!")

#_________________________________________


def doReplyAll():                         #-------- sets reply mode to reply all
	pyautogui.press('a')

#_________________________________________


def MailContent():						  #-------- Edit this funtion according to what you want as mail content

	pyautogui.write()
	
	pyautogui.hotkey('ctrl','b')	#---- To make tex bold
	pyautogui.write()

	pyautogui.hotkey('ctrl','b')

	pyautogui.write()
	pyautogui.hotkey('ctrl','shift','8') 

#_________________________________________


def sendMail():							 #--------- Sends email
	
	pyautogui.moveTo(1022,641, duration = 1)
	pyautogui.click()

#_________________________________________


def closeGmail():						 #--------- closes the curently open tab

	pyautogui.hotkey("ctrl",'w')

#_____________________________________________________________________#

#######################################################################
            ############# Telegram bot #############
#######################################################################

##### bot data #####

bot = telebot.TeleBot("YOUR_BOT_TOKEN/API")
url = 'https://api.telegram.org/bot1237217742:AAHI4-pmTZRIqTt8CSUZbipHFuj1QMnsQdk/sendMessage'
YOUR_CHAT_ID = 972187028

#________________________________________________#

def SendMesg(mesg):										 #-------------- Function to enable bot messages

	data = {'chat_id': {YOUR_CHAT_ID}, 'text': mesg}
	requests.post(url, data).json()

#_________________________________________________#

@bot.message_handler(commands=['start','help'])          #-------------- Sets Welcome command
def send_welcome(message):
	
	SendMesg("Hey!!\nI am Dustin!!\nHere is what all I can do....")
	SendMesg('> I can open gmail\n> Search for mail and send mail\n> Close tabs and Refresh browser\n> Put your laptop to sleep')
			
#_________________________________________________#

@bot.message_handler(func=lambda m: True)         		 #-------------- Listens for message from user
def rerply_to(message):

	if message.text == "Open gmail":
				
		LoadBrowser()
		OpenGmail()
		bot.reply_to(message,"opened gmail")

#_______________________________________
	
	if message.text == 'Send update':
		ThreadName = "Crypto"

		LoadBrowser()
		OpenGmail()
		openMailThread(ThreadName)				
			
		bot.reply_to(message,"Opened thread!")
			
		doReplyAll()
		MailContent()
		sendMail()

		bot.reply_to(message,"""Hey your mail has been sent!! :)""")

#_______________________________________

	if 'Open thread' in message.text:

		try:
			if ':' in message.text:
					ThreadName = str(message.text.split(':')[1])
		except:
			SendMesg('You dint provide thread name!!')
			LoadBrowser()
			OpenGmail()				

		LoadBrowser()
		OpenGmail()
		SendMesg("Opening {}".format(ThreadName))
		openMailThread(ThreadName)
				
#_______________________________________
	if message.text == "Stop":
		stopPyautogui()
#_______________________________________
	if message.text == 'Refresh':
		pyautogui.hotkey('ctrl','r')
#_______________________________________			
	if message.text == 'Thanks Dustin' or message.text == 'Thakns':
		bot.reply_to(message,'Just doin my job! :D')
#_______________________________________
	if message.text == "Close tab":
		closeGmail()
		bot.reply_to(message,"Closed tab")
#_______________________________________			
	if message.text == "Hello" or message.text == "Hey":
		bot.reply_to(message,"Howdy,how are you doing?")
#_______________________________________			
	if message.text == 'Sleep':
		bot.reply_to(message,'Laptop has been locked!')
		os.system('gnome-screensaver-command -l')
#_______________________________________
	if message.text == 'Ok':
		bot.reply_to(message,'Good!')
#_______________________________________
	if message.text == "Stop":
		bot.reply_to(message,'All actions Stopped!!')
		closeGmail()
		time.sleep(100)
#______________________________________________________#

#######################################################
         ########### Job Handler ###########
#######################################################

@tl.job(interval=timedelta(seconds=1))					#----------- Checks for messages on telegram [every 1 second]
def Check_Telegram_Every_1s():
	
	bot.polling()

#_______________________________________________________

@tl.job(interval=timedelta(seconds=1))					#------------ Checks current time to send update alerts at specified hour
def Check_Time_every_1s():

	global repeat1
	global repeat2

	if datetime.now().hour == 22 and repeat1 == False:
		
		repeat1 = True
		SendMesg('Hey dont forget to send your update!!')

	if (datetime.now().hour == 23 and  datetime.now().minute == 1 and repeat2 == False):
		
		repeat2 = True
		SendMesg('Hey vish hope u have not forgotten to send the daily status update!')
		SendMesg('If u have forgotten just type "Send update"and I will send it for you :)')

#########################################################
#########################################################

if __name__ == '__main__':
	
	repeat1 = False
	repeat2 = False
	tl.start(block=True)
