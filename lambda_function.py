import json

from cascade import cascade
from factorfiction import factorfiction
from lottery import draw_lottery, plus_1, minus_1, view_entries

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

PUBLIC_KEY = 'a6d6d1e2e1053428e236a69cf7a717fd532fb89a2b6fd575d60362513e4b9b6d'
MODERATOR_ROLE = "940408316906053664"

def lambda_handler(event, context):
	try:
		body = json.loads(event['body'])
				
		signature = event['headers']['x-signature-ed25519']
		timestamp = event['headers']['x-signature-timestamp']

		# validate the interaction

		verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

		# message = timestamp + json.dumps(body, separators=(',', ':'))
		message = timestamp + event['body']

		try:
			verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
		except BadSignatureError:
			return {
				'statusCode': 401,
				'body': json.dumps('invalid request signature')
			}
		
		# handle the interaction

		t = body['type']

		if t == 1:
			return {
				'statusCode': 200,
				'body': json.dumps({
					'type': 1
				})
			}
		elif t == 2:
			return command_handler(body)
		else:
			return {
				'statusCode': 400,
				'body': json.dumps('unhandled request type')
			}
	except:
		raise

def command_handler(body):
	command = body['data']['name']
	if command == 'cascade':
		arg = body['data']['options'][0]['value']
		print(body['member']['user']['global_name'], arg)
		return json.dumps({
			'type': 4,
			'data': {
				'content': cascade(arg),
			}
		})
	elif command == 'factorfiction':
		extra = body['data']['options'][0]['value'] if 'options' in body['data'] else None
		return json.dumps({
			'type': 4,
			'data': {
				'content': factorfiction(extra),
			}
		})
	elif command == 'draw_lottery':
		if MODERATOR_ROLE not in body['member']['roles']:
			return json.dumps({
				'type': 4,
				'data': {
					'content': "You don't have permission to use this command."
				}
			})
		return json.dumps({
			'type': 4,
			'data': {
				'content': draw_lottery(),
			}
		})
	elif command == 'list_lottery_entries':
		if MODERATOR_ROLE not in body['member']['roles']:
			return json.dumps({
				'type': 4,
				'data': {
					'content': "You don't have permission to use this command."
				}
			})
		return json.dumps({
			'type': 4,
			'data': {
				'content': view_entries(),
			}
		})
	elif command == 'plus_1_lottery':
		if MODERATOR_ROLE not in body['member']['roles']:
			return json.dumps({
				'type': 4,
				'data': {
					'content': "You don't have permission to use this command."
				}
			})
		arg = body['data']['options'][0]['value']
		print(body['member']['user']['global_name'], arg)
		return json.dumps({
			'type': 4,
			'data': {
				'content': plus_1(arg),
			}
		})
	elif command == 'minus_1_lottery':
		if MODERATOR_ROLE not in body['member']['roles']:
			return json.dumps({
				'type': 4,
				'data': {
					'content': "You don't have permission to use this command."
				}
			})
		arg = body['data']['options'][0]['value']
		print(body['member']['user']['global_name'], arg)
		return json.dumps({
			'type': 4,
			'data': {
				'content': minus_1(arg),
			}
		})
	else:
		return {
			'statusCode': 400,
			'body': json.dumps('unhandled command')
		}
