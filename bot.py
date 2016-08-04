import threading
import uuid
from configparser import *
import telepot
import time
from commands import *
from decimal import *
# Get the API key
parser = SafeConfigParser()
parser.read('settings.ini')
api = parser.get('shadsbot_settings', 'api_key')


class myThread(threading.Thread):
    def __init__(self,threadID,cmd,msgID,fbot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.cmd = cmd
        self.msgID = msgID
        self.bot = fbot
    def run(self):
        checkcmd(self.cmd,self.msgID,self.bot)
        

# Things to do when messages come in
def handle(msg):
        flavor = telepot.flavor(msg)
        print("Flavor: %s" % flavor)
        chat_id = msg['chat']['id']
        command = msg['text']
        thread = myThread(uuid.uuid1(), command, chat_id, bot)
        thread.start()
        #thread.join()
        #checkcmd(command,chat_id,bot)

bot = telepot.Bot(api)
bot.setWebhook()
getcontext().prec = 3
bot.message_loop(handle)

print('ShadsBot has started. Ready when you are.')

while 1:
        time.sleep(10)
