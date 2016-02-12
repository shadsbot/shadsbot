from users import *
import re

def checkcmd(command, chat_id, bot, colin,julian,jake):
	print('Command: %s' % command)
	print('From: %s' % chat_id)
	# Handle actual commands here
	if command == '/based':
		bot.sendMessage(chat_id, 'Based Orlando has heard your plea, and it has been denied.')
	if '/math' in command:
		# Parse because this is dangerous!
		doThis = command[5:]
		doThis = re.sub(r'([A-Z]|[a-z])|[!|,|@|#|$|&|\\|;|\/|<|>|"|\'|_|?|:|=]','',doThis)
		doThis = doThis.replace(" ","")
		try:
			bot.sendMessage(chat_id, eval(doThis))
		except:
			bot.sendMessage(chat_id, "This only accepts mathematical statements.")
	if command == '/furriest':
		bot.sendMessage(chat_id, '''Here are the current standings:
Current Mascot: Jake
Most Posted: Julian
Most Adorable: Colin
Biggest Furry: Jake''')
	if command == '/sam':
		bot.sendMessage(chat_id, 'Your mother was a hamster and your father smelled of elder berries.')
	if command == '/holyshit':
		bot.sendMessage(chat_id, 'A talking cat')
	if '/powerlevel' in command:
		message = ''
		if 'jake' in command or 'Jake' in command:
			message += 'Jake\'s powerlevel: %(jake)i' %{"jake": jake.powerlevel()} + '\n'
		if 'julian' in command or 'Julian' in command:
			message += 'Julian\'s powerlevel: %(julian)i' %{"julian": julian.powerlevel()} + '\n'
		if 'colin' in command or 'Colin' in command:
			message += 'Colin\'s powerlevel: %(colin)i' % {"colin": colin.powerlevel()} + '\n'
		bot.sendMessage(chat_id, message)
	if '/addpower' in command:
		if 'jake' in command or 'Jake' in command:
			jake.addpl()
		if 'julian' in command or 'Julian' in command:
			julian.addpl()
		if 'colin' in command or 'Colin' in command:
			colin.addpl()

