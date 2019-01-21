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
* Play music from Youtube (probably going to be removed)
* Sings [Disco, Disco! Party, Party!](https://www.youtube.com/watch?v=vrphLUWZv3Q) with you

TODO:
* Some refactoring maybe
* Fix news parsing
* Maybe make the command system use modules
* Move to [discord.py]() rewrite
* Add capability to recognize maintenances
    * Put maintenance status to bot playing status
* Remove discoparty thing
* Remove music playing capabilities (there are better things for this)
* Put WolframAlpha integration into a command instead of mention
* Improve configurability
