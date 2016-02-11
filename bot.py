from ConfigParser import SafeConfigParser
import telepot
import time
from commands import *
from decimal import *

# Get the API key
parser = SafeConfigParser()
parser.read('settings.ini')
api = parser.get('shadsbot_settings', 'api_key')

# Things to do when messages come in
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
        checkcmd(command,chat_id,bot)
        
bot = telepot.Bot(api)
bot.setWebhook()
bot.notifyOnMessage(handle)
getcontext().prec = 3
print('ShadsBot has started. Ready when you are.')

while 1:
	time.sleep(10)
