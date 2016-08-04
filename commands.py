import re
import json
import requests
import urllib
import time
import uuid
import os
from configparser import *

parser = SafeConfigParser()
parser.read('settings.ini')
wordnik_api = parser.get('shadsbot_settings','wordnik_api')

def mtgtext(cardn, text):
        if text is True:
                isCreature = False
                msg = ""
                try:
                        response = requests.get('https://api.deckbrew.com/mtg/cards?name=%s' % (cardn))
                        data = response.json()
                        msg += "%s \n" % (data[0]['name'])
                        for m in data[0]['cost']:
                                go = True
                                if m == '{' or m == '}':
                                        go = False
                                if go == True:
                                        msg += m
                        msg += "\n"
                        for ctype in data[0]['types']:
                                msg += "%s " % ctype.title()
                                if ctype == 'creature':
                                        isCreature = True
                        if isCreature:
                                msg += "-- "
                                for stype in data[0]['subtypes']:
                                        msg += "%s " % stype.title()
                        msg += "\n\n"
                        msg += data[0]['text']
                        msg += "\n"

                        if isCreature:
                                msg += "\n%s/%s" % (data[0]['power'], data[0]['toughness'])
                except:
                        if msg == "":
                                msg += "Couldn't find that card. Check your spelling and try again."
                return msg
        response = requests.get('https://api.deckbrew.com/mtg/cards?name=%s' % (cardn))
        data = response.json()
        picurl = data[0]['editions'][1]['image_url']
        return picurl

def checkcmd(command, chat_id, bot):
        print('Command: %s' % command)
        print('From: %s' % chat_id)
        # Handle actual commands here
        if command == '/based':
                bot.sendMessage(chat_id, 'Based Orlando has heard your plea, and it has been denied.')
        if '/math' in command:
                # Parse because this is dangerous!
                doThis = command[5:]
                doThis = re.sub(r'([A-Z]|[a-z])|[!|,|@|#|$|&|\\|;|<|>|"|\'|_|?|:|=]','',doThis)
                doThis = doThis.replace(" ","")
                # print("Debug: " + doThis)
                try:
                        bot.sendMessage(chat_id, '%.2f' % eval(doThis))
                except:
                        bot.sendMessage(chat_id, "This only accepts mathematical statements.")
        if command == '/trutru':
                pic = open('trutru.jpg', 'rb')
                bot.sendPhoto(chat_id, pic)
        if command == '/test':
                bot.sendMessage(chat_id, "This bot is recieving commands and is able to respond.")
        if '/mtg ' in command:
                cardn = command[5:]
                msg = mtgtext(cardn, True)
                bot.sendMessage(chat_id,msg)
        if '/mtgp' in command:
                cardn = command[6:]
                picurl = mtgtext(cardn, False)
                uid = uuid.uuid4().hex
                uid += ".jpg"
                pic = urllib.request.urlretrieve(picurl, uid)
                pic = open(uid, 'rb')
                bot.sendChatAction(chat_id, 'upload_photo')
                response = bot.sendPhoto(chat_id, pic)
                del pic
                os.remove(uid)
        if '/ping' in command:
                addr = command[6:]
                response = os.system("ping -n 1 " + addr)
                if response == 0:
                        msg = "We could reach %s" % addr
                else:
                        msg = "We could *not* reach %s" % addr
                bot.sendMessage(chat_id, msg, parse_mode='Markdown')
        if '/def' in command:
                word = command[5:]
                msg = word
                msg += "\n"
#               try:
#                       response = requests.get('http://dictionaryapi.net/api/definition/%s' % (word))
#                       data = response.json()
#                       for defin in data:
#                               msg += "*"
#                               msg += defin['PartOfSpeech']
#                               msg += "* - "
#                               for mdefin in defin['Definitions']:
#                                       msg += mdefin
#                                       msg += "\n\n"
#                               #msg += defin['Definitions'][0]
#                               msg += "\n\n"
#               except:
                response = requests.get('http://api.wordnik.com/v4/word.json/%s/definitions?limit=2&includeRelated=false&sourceDictionaries=wiktionary&useCanonical=false&includeTags=false&api_key=%s' % (word,wordnik_api))
                data = response.json()
                for x in data:
                    msg+="\n*"
                    msg+=x['partOfSpeech']
                    msg+="*"
                    msg+=" - _"
                    msg+=x['text']
                    msg+="_\n"

                bot.sendMessage(chat_id,msg, parse_mode='Markdown')
