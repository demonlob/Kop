from logging import basicConfig, INFO, FileHandler, StreamHandler, getLogger, ERROR, Logger

basicConfig(
    level=INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        FileHandler("log.txt"),
        StreamHandler(),
    ],
)

getLogger("httpx").setLevel(ERROR)
getLogger("pyrogram").setLevel(ERROR)
getLogger("pytgcalls").setLevel(ERROR)


def LOGGER(name: str) -> Logger:
    return getLogger(name)
