from ConfigParser import SafeConfigParser
import telepot

# Get the API key
parser = SafeConfigParser()
parser.read('settings.ini')
api = parser.get('shadsbot_settings', 'api_key')

# Things to do when messages come in
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['txt']
	# Debugging: Output
	print('Command: %s' % command)
	# Handle actual commands here
	if command == '/based':
		bot.sendMessage(chat_id, 'Based Orlando has heard your plea, and it has been denied.')

bot = telepot.Bot(api)
bot.notifyOnMessage(handle)
print('ShadsBot has started. Ready when you are.')

while 1:
	time.sleep(5)
