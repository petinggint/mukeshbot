
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 24459692 # integer value, dont use ""
    API_HASH = "e5ad49a89732b011de710fd0789da86f"
    TOKEN = "6447190497:AAFBPg29G_aSSr9BsNGrCfaOiMw1_eoCq1Y"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5973260847  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "zonenomercy"  # Your own group for support, do not add the @
    START_IMG = "https://c4.wallpaperflare.com/wallpaper/125/323/619/art-artwork-fantasy-mage-wallpaper-preview.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://manonebillion:iwan12345@znmanagement.zmxccsq.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://wlfcvgiz:J4ZbS4EN4m3Ihwnv1jzUFX-zk_HnroUM@john.db.elephantsql.com/wlfcvgiz"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "ANP310DY837JATU7"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5Q6WJX05N43Y"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="6126083299-fallen-nhfm33mfhn" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5973260847]  # User id of sudo users
    DEV_USERS = [5973260847]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
