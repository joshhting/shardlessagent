import os
import json
import urllib.request
import urllib.parse
import datetime
import math

def get_last_replicate_datetime():
	"""Search the server for the most recent message containing the replicate output.
	Returns a timezone-aware datetime in UTC or None if not found or on error.
	"""
	search_str = "It has now been 0 days since Josh Ting and Nelson Chen were confused for one another. The previous record was "
	try:
		token = os.getenv('DISCORD_TOKEN')
		guild = os.getenv('DISCORD_SERVER')
		# guild = os.getenv('TEST_SERVER')
		if not token or not guild:
			return None

		# Use a content search for a distinctive phrase from the bot output.
		query = urllib.parse.urlencode({
			'content': "It has now been 0 days since Josh Ting and Nelson Chen were confused for one another. The previous record was 13 days.",
			# 'author_type': 'bot',
			'limit': 25
		})
		url = f"https://discord.com/api/v10/guilds/{guild}/messages/search?{query}"
		req = urllib.request.Request(url, headers={
			'Authorization': f'Bot {token}',
			'User-Agent': 'shardlessagent/1.0'
		})
		with urllib.request.urlopen(req, timeout=10) as resp:
			data = json.load(resp)

		msgs = data.get('messages', [])
		# print("data: ", str(data))
		latest = datetime.datetime(2026, 5, 14, tzinfo=datetime.timezone.utc)
		for channel_msgs in msgs:
			for msg in channel_msgs:
				ts = msg.get('timestamp')
				if not ts:
					continue
				try:
					dt = datetime.datetime.fromisoformat(ts.replace('Z', '+00:00'))
				except Exception:
					continue
				if dt > latest:
					latest = dt
		now = datetime.datetime.now(datetime.timezone.utc)
		# ensure both are timezone-aware in UTC
		if latest.tzinfo is None:
			latest = latest.replace(tzinfo=datetime.timezone.utc)
		age = (now - latest).days
		return f"{search_str}{age} days."
	except Exception:
		return None
