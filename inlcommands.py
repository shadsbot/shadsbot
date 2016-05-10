from telepot.namedtuple import InlineQueryResultArticle
from telepot.namedtuple import InlineQueryResultPhoto
import telepot.async
import asyncio
import telepot

def checkinlcmd(msg,bot):
	chat_id = msg['chat']['id']
	command = msg['text']

	query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')

	answer = [{'type':'article',
					'id':chat_id,
					'title':"Fresh From Shadsbot:",
					'message_text': 'Placeholder!'}]

	answerer = telepot.async.helper.Answerer(bot)
	answerer.answer(msg, "compute_answer")
	# bot.answerInlineQuery(query_id, answer)