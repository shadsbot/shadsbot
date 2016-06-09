from configparser import *
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
	flavor = telepot.flavor(msg)
	print("Flavor: %s" % flavor)
	chat_id = msg['chat']['id']
	command = msg['text']
	checkcmd(command,chat_id,bot)

bot = telepot.Bot(api)
bot.setWebhook()
getcontext().prec = 3
bot.message_loop(handle)

print('ShadsBot has started. Ready when you are.')

while 1:
	time.sleep(10)
