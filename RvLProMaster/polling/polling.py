# Load Library
from RvLProMaster import endpoint, bot
from .clear_polling import clear_log
from httpx import AsyncClient
import asyncio

@staticmethod
async def polling():
    await clear_log()
    offset = None
    while True:
        in_polling = await bot.Updates.getUpdates(offset)
        if in_polling and 'result' in in_polling:
            for out_polling in in_polling['result']:
                offset = out_polling['update_id'] + 1
                return out_polling
            await asyncio.sleep(1)