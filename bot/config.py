from decouple import config

try:
    API_ID = 6362269
    API_HASH = b3ce9b687362bbb5be283659a2292f3b
    BOT_TOKEN = 2084834915:AAF9VqoBXioZSQRQHcl4-Ouik8c0l32ZCYA
    DEV = 1449986020
    OWNER = 1449986020
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -preset ultrafast -c:v libx265 -crf 27 -map 0:v -c:a aac -map 0:a -c:s copy -map 0:s? "{}"',
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
