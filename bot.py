# Sometimes works with python3 or python2? Uncomment whichever one works
try:
	from ConfigParser import SafeConfigParser
except:
	from configparser import *
import telepot
import time
from commands import *
from decimal import *
from users import *
from inlcommands import *
# Get the API key
parser = SafeConfigParser()
parser.read('settings.ini')
api = parser.get('shadsbot_settings', 'api_key')

# Things to do when messages come in
def handle(msg):
	flavor = telepot.flavor(msg)
	print("Flavor: %s" % flavor)
#	if flavor == 'normal' or flavor == 'chat':
	chat_id = msg['chat']['id']
	command = msg['text']
	checkcmd(command,chat_id,bot,colin,julian,jake)
	# elif flavor == 'inline_query':
	# 	print("Inline Query")
	# 	checkinlcmd(msg,bot)

bot = telepot.Bot(api)
bot.setWebhook()
getcontext().prec = 3
bot.message_loop(handle)
#create users - this is not permanent
colin = User("Colin", 0)
julian = User("Julian", 50)
jake = User("Jake", 100)

print('ShadsBot has started. Ready when you are.')

while 1:
	time.sleep(10)
