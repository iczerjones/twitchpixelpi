Simple Twitch IRC bot to control a NeoPixel strip with commands.

config.py needs to be edited as follows:

```
HOST = "irc.twitch.tv"              # This is Twitchs IRC server
PORT = 6667                         # Twitchs IRC server listens on port 6767
NICK = "twitch_username"            # Twitch username your using for your bot
PASS = "your_oauthtoken" # your Twitch OAuth token
CHAN = "#your_channel"                   # the channel you want the bot to join.
```
NICK is the twitch username the bot would be using (all letters in lowercase).  

PASS is the oauth token for the twitch account the bot would be using. Sign into a web browser with the bot's account,  
    and go here: https://twitchapps.com/tmi/ you need the whole oauth including the "oauth:"  

CHAN is the Twitch streamer account you want the bot to read and respond to (again, all letters in lowercase).  