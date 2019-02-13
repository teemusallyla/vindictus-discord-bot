import string

async def discoParty(message, client):
    msg = message.content.lower()
    newmsg = ""
    to_return = None
    for letter in msg:
        if not letter in string.punctuation:
            newmsg += letter
        elif letter in string.punctuation:
            newmsg += " "
    newmsg.replace("  ", " ")
    if "you say disco" in newmsg:
        to_return = "Disco, Disco!"
    elif "i say disco" in newmsg and not "you say party" in newmsg:
        to_return = "I say Party!"
    elif ("i say disco" in newmsg and "you say party" in newmsg
          and newmsg.split(" ").count("disco") > 1):
        to_return = "Party, " * (newmsg.split(" ").count("disco") - 2) + "Party!"
    elif not "i say disco" in newmsg and "disco" in newmsg.split():
        to_return =  "Party, " * (newmsg.split(" ").count("disco") - 1) + "Party!"
    if not to_return == None:
        await client.send_typing(message.channel)
        await client.send_message(message.channel, to_return)