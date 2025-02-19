import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8097590355:AAFzrS_c_K45bCAo8J1APHcm5QXoXDJ4L1A")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21003880"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bf157632e77ea8b28ff3e186dc95ab35")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://videshi:videshi@videshi.wtffv.mongodb.net/?retryWrites=true&w=majority&appName=videshi")
