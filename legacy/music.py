import discord
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def on_voice_state_update(self, before, after):
    if self.mh.voice != None:
        ch = self.mh.voice.channel
        server = self.mh.voice.server
        if ch and len(ch.voice_members) == 1 and server.me in ch.voice_members:
            await self.mh.stop()


class MusicHandler():
    def __init__(self, client, message = None):
        self.__base_yt__ = "https://www.youtube.com/watch?v="
        self.message = message
        self.client = client
        self.voice = None
        self.player = None
        self.url = None
        self.play_next = False
        self.music_queue = asyncio.Queue()
        self.volume = 0.2
        if self.message != None:
            self.handle(message)
        self.stopped = False

    def __call__(self):
        if not self.stopped:
            func = asyncio.run_coroutine_threadsafe(self.nextSong(), loop = self.client.loop)
            func.result()
        self.stopped = False

    async def handle(self, message):
        self.message = message
        command_position = 1
        if message.content.lower().split()[command_position] == "play":
            if self.message.content.split()[command_position + 1] == "search":
                self.url = self.__base_yt__ + await youtubeSearch(
                    " ".join(self.message.content.split()[command_position + 2:]))
            elif self.__base_yt__ in self.message.content.split()[-1]:
                self.url = self.message.content.split()[-1]
            await self.play()
        elif (message.content.lower().split()[command_position] == "pause"
              and self.voice != None
              and self.player != None
              and self.voice.is_connected()
              and self.player.is_playing()):
            await self.pause()
        elif (message.content.lower().split()[command_position] == "resume"
              and self.voice != None
              and self.player != None
              and self.voice.is_connected()
              and not self.player.is_playing()):
            await self.resume()
        elif (message.content.lower().split()[command_position] == "stop"):
            await self.stop()
        elif (message.content.lower().split()[command_position] == "volume"
              and self.voice != None
              and self.player != None
              and self.voice.is_connected()):
            try:
                volume = float(message.content.split()[command_position + 1])
                if volume > 1:
                    volume /= 10
                if volume > 1:
                    volume = 1
                if volume < 0:
                    volume = 0
                self.volume = volume
                await self.setVolume(volume)
            except:
                pass
        elif (message.content.lower().split()[command_position] == "next"
              and self.voice != None
              and self.player != None
              and self.voice.is_connected()):
            await self.client.send_message(message.channel, "Moving to next song!")
            await self.nextSong()
        elif (message.content.lower().split()[command_position] == "queue"
              and self.voice != None
              and self.player != None
              and self.voice.is_connected()):
            if message.content.lower().split()[command_position + 1] == "clear":
                self.music_queue = asyncio.Queue()
                await self.client.send_message(message.channel, "Queue cleared!")
            elif message.content.lower().split()[command_position + 1] == "put":
                if message.content.lower().split()[command_position + 2] == "search":
                    url = self.__base_yt__ + await youtubeSearch(
                        " ".join(self.message.content.split()[command_position + 3:]))
                elif self.__base_yt__ in message.contentlower.split()[-1]:
                    url = self.message.content.split()[-1]
                await self.music_queue.put(url)
                await self.client.send_message(message.channel, "Added to queue!")
        elif message.content.lower().split()[command_position] == "help":
            help_message = "Bot music commands:\n\
!music play _Youtube-url_\n\
!music play search _Youtube search query_\n\
!music pause\n\
!music resume\n\
!music stop\n\
!music volume _value (0.0 - 1.0)_\n\
!music queue put _Youtube-url_\n\
!music queue put search _Youtube search query_\n\
!music queue clear\n\
!music next\n\
!music help\n"
            await self.client.send_message(message.channel, help_message)

    async def play(self):
        if self.voice == None:
            for channel in self.message.server.channels:
                if (channel.type == discord.ChannelType.voice
                    and self.message.author in channel.voice_members):
                    self.voice = await self.client.join_voice_channel(channel)
                    break

        if self.url != None and self.voice != None:
            if self.player != None:
                self.stopped = True
                self.player.stop()
            self.player = await self.voice.create_ytdl_player(self.url, after = self)
            self.player.volume = self.volume
            self.player.start()
            await self.client.send_message(self.message.channel, "Now playing: "
                                    + self.player.title)

    async def pause(self):
        self.player.pause()

    async def resume(self):
        self.player.resume()

    async def stop(self):
        if self.player != None:
            self.stopped = True
            self.player.stop()
            self.player = None
        if self.voice != None and self.voice.is_connected():
            await self.voice.disconnect()
        if self.voice != None:
            self.voice = None

    async def setVolume(self, value):
        self.player.volume = value

    async def nextSong(self):
        if not self.music_queue.empty():
            self.url = await self.music_queue.get()
        await self.play()
        self.stopped = False
 

async def youtubeSearch(query):
    params = {"search_query": query}
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.youtube.com/results", params = params) as resp:
            soup = BeautifulSoup(await resp.text(), "html.parser")
            vid_div = soup.find_all("div", class_ = "yt-lockup-video")[0]
            return vid_div.get_attribute_list("data-context-item-id")[0]