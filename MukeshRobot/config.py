class Config(object):
    LOGGER = True
    API_ID =None 
    API_HASH = ""
    TOKEN = ""  
    OWNER_ID=7353842230
    
    SUPPORT_CHAT = "" 
    START_IMG = ""
    EVENT_LOGS = ()
    MONGO_DB_URI= ""
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [7353842230] 
    DRAGONS = [7353842230]
    DEV_USERS = [7353842230]  
    DEMONS = [7353842230] 
    TIGERS = [7353842230]  
    WOLVES = [7353842230] 

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
