A Discord bot made in Python

About:
* Uses [discord.py](https://github.com/Rapptz/discord.py) for Discord integration
* asyncio/aiohttp for asynchronous programming

Things it does:
* Automatically posts new news on Vindictus to chosen channel
* Keeps track of Vindictus events and sales and posts them on command
    * Tries to automatically parse them (quite broken due to site changes)
    * Manual entering
* WolframAlpha integration
* Notification system (create timed notifications)
* Add reactions on command (from other servers as well)
* Post emojis on command (from others servers as well)
* Some administrative tools (delete messages by masses)
* Add role to member on server join
* Add role on command (not in use)

TODO:
* Some refactoring maybe
* Fix news parsing
* Maybe make the command system use modules
* Move to [discord.py]() rewrite
* Add capability to recognize maintenances
    * Put maintenance status to bot playing status
* Improve configurability

COMMANDS:
* !events
    * Posts currently on-going Vindictus events
* !sales
    * Posts currently on-going Vindictus sales
* !wolframalpha, !wolf, !alpha, !wolfram [query]
    * Asks WolframAlpha your query
* !emote, !animated [emoji name]
    * Posts an emote specified by its name, even from another server (in which the bot is a member)
* !react [msg id] [ch id] [emote name]
    * Reacts to a specific messgage with given emoji. Emoji can be from outside server or animated
* !notify
    * Add a notification for a later date
* !channel [#channel]
    * Specify the channel in which the bot should post Vindictus news
* !delmsg [ch id] [msg id]
    * Delete a specific message. Only for bot owner
* !game [game]
    * Change the bot's "Playing" message. Only for bot owner
