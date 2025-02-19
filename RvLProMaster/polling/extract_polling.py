from .polling import polling
from json import dumps
from typing import Optional, Literal
from functools import wraps
import asyncio

class telegram_types:
    def __init__(self):
        self.resetValues()
    
    def resetValues(self):
        self.chat_id = ''
        self.text = ''
        self.reply_message = ''
        
        # User Information
        self.first_name = ''
        self.last_name = ''
        self.username = ''
        self.user_id = ''
        
    # Save Polling 
    def savePolling(self, out_polling):
        if 'message' in out_polling:
            with open('message.json', 'w') as f:
                f.write(dumps(out_polling, indent=2))
        elif 'channel_post' in out_polling:
            with open('channel.json', 'w') as f:
                f.write(dumps(out_polling, indent=2))

    async def RunBOT(self, save_polling: bool = False):
        while True:
            try:
                out_polling = await polling()
                # Group
                if 'message' in out_polling:
                    self.chat_id = out_polling['message']['chat'].get('id','')
                    self.text = out_polling['message'].get('text','')
                    self.reply_message = out_polling['message'].get('message_id', '')
                    
                    # User Information
                    self.first_name = out_polling['message']['from'].get('first_name','')
                    self.last_name = out_polling['message']['from'].get('last_name','')
                    self.username = out_polling['message']['from'].get('username','')
                    self.user_id = out_polling['message']['from'].get('id','')
                    
                    # Save Polling
                    if save_polling == True:
                        self.savePolling(out_polling)
                    else:
                        pass
                elif 'channel_post' in out_polling:
                    # Save Polling
                    if save_polling == True:
                        self.savePolling(out_polling)
                    else:
                        pass
                return self
            except:
                pass

types = telegram_types()

def RunBOT(always_run: bool = True):
    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            if always_run == True:
                print(f"Detected Parameters always_run\nStatus: {always_run} (Always Running)\nRunning BOT")
                while True:
                    await types.RunBOT()
                    await asyncio.sleep(1)
                    await func(*args, **kwargs)
            elif always_run == False:
                print(f"Detected Parameters always_run\nStatus: {always_run} (Only Run Once)\nRunning BOT")
                await types.RunBOT()
                await asyncio.sleep(1)
                await func(*args, **kwargs)
            else:
                print(f"Please Spesify always_run parameter\nIf Set To True BOT Will Receive The Latest Polls Continuously (Real Time) And Send Any Response Method Only Once\nIf Set To False BOT Will Receive Latest Poll Once And Send Any Response Method Only Once Then Bot Will Stop")
        return wrapped
    return wrapper