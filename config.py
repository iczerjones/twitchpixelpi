HOST = "irc.twitch.tv"              # This is Twitchs IRC server
PORT = 6667                         # Twitchs IRC server listens on port 6767
NICK = "twitch_username"            # Twitch username your using for your bot
PASS = "your_oauthtoken" # your Twitch OAuth token
CHAN = "#your_channel"                   # the channel you want the bot to join.
RATE = (20/30) # messages per seccond
BAN_PAT = [
    r"swear",
    r"some_pattern"
]
COMMANDS = [
	[r"!discord", "the official discord: ____"],
	[r"!hibbidy", "Response"]
]

NEO = [
    [r"your_bot_message", "led"] # Message a bot says in your chat for new followers
]

NEO2 = [
    [r"your_bot_message", "led"] # Message a bot says in your chat for new subscribers
]

BLANK = [
    [r"!blank", "led"]
]

NEO3 = [
    [r"!strobe", "led"]
]

NEO4 = [
    [r"!party", "led"]
]
