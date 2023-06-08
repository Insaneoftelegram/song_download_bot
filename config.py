import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "17150103"))
    API_HASH = os.environ.get("API_HASH", "54cf8742804b5ffaa10df2b53ef91fe2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6297344590:AAFbBHK9PioaIS0sZnH0jR4a4Sp7859Rt_4")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2a35fca576aa49de77c98.jpg")
    OWNER = os.environ.get("OWNER", "Insane_of_telegram") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
