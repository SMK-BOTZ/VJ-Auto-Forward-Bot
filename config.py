from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "28ba253a514409ad88fe84902590b6c0")
      API_ID = int(getenv("API_ID", "26862233"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6555905604:AAF12TggABfXe-JZYle0VSB4HF29sY92oB8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002072368970:-1002115170197").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
