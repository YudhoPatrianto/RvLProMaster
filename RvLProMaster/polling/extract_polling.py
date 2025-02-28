from .polling import polling
from json import dumps
from typing import Optional, Literal
from functools import wraps
import asyncio

class telegram_types:
    def __init__(self):
        self.resetValues()
    
    def resetValues(self):
        # Event Field
        self.event_field = ''

        # Message Information
        self.chat_id = ''
        self.text = ''
        self.reply_message = ''
        
        # User Information
        self.first_name = ''
        self.last_name = ''
        self.username = ''
        self.user_id = ''
        
        # new_chat_participant
        self.first_name_joined = ''
        self.last_name_joined = ''
        self.username_joined = ''
        self.user_id_joined = ''
        
        # left_chat_member
        self.first_name_left = ''
        self.last_name_left = ''
        self.username_left = ''
        self.user_id_left = ''
        
        # chat_join_request
        self.first_name_request = ''
        self.last_name_request = ''
        self.username_request = ''
        self.user_id_request = ''
        
    # Save Polling 
    def savePolling(self, out_polling):
        if 'message' in out_polling:
            with open('message.json', 'w') as f:
                f.write(dumps(out_polling, indent=2))
        elif 'channel_post' in out_polling:
            with open('channel.json', 'w') as f:
                f.write(dumps(out_polling, indent=2))

    async def ExtractPolling(self, save_polling: bool = False):
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
                    
                    # new_chat_participant (UserJoined)
                    if 'new_chat_participant' in out_polling['message']:
                        self.event_field = 'new_chat_participant'
                        self.first_name_joined = out_polling['message']['new_chat_participant'].get('first_name','')
                        self.last_name_joined = out_polling['message']['new_chat_participant'].get('last_name','')
                        self.username_joined = out_polling['message']['new_chat_participant'].get('username','')
                        self.user_id_joined = out_polling['message']['new_chat_participant'].get('id','')
                    
                    # left_chat_member (UserLeft)
                    elif 'left_chat_participant' in out_polling['message']:
                        self.event_field = 'left_chat_participant'
                        self.first_name_left = out_polling['message']['left_chat_participant'].get('first_name','')
                        self.last_name_left = out_polling['message']['left_chat_participant'].get('last_name','')
                        self.username_left = out_polling['message']['left_chat_participant'].get('username','')
                        self.user_id_left = out_polling['message']['left_chat_participant'].get('id','')
                        
                elif 'chat_join_request' in out_polling:
                    self.event_field = 'chat_join_request'
                    
                    # User Information
                    self.first_name_request = out_polling['chat_join_request']['from'].get('first_name','')
                    self.last_name_request = out_polling['chat_join_request']['from'].get('last_name','')
                    self.username_request = out_polling['chat_join_request']['from'].get('username','')
                    self.user_id_request = out_polling['chat_join_request']['from'].get('id','')
                return self
            except:
                pass
            
    def EventWatcher(self, EventSelector: Literal['UserRequest', 'UserJoined', 'UserLeft']) -> bool:
        # User Request To Join
        if self.event_field == "chat_join_request":
            self.event_field =  None
            if EventSelector == 'UserRequest':
                self.event_field = None
                return True
        # User Joined Into Chat
        if self.event_field == "new_chat_participant":
            self.event_field =  None
            if EventSelector == 'UserJoined':
                self.event_field = None
                return True
        # User Joined Into Chat
        if self.event_field == "left_chat_participant":
            self.event_field =  None
            if EventSelector == 'UserLeft':
                self.event_field = None
                return True
        return False

types = telegram_types()

def RunBOT(always_run: bool = True, save_polling: bool = False):
    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            if always_run == True:
                if save_polling == True: # Save Polling 
                    print(f"Detected Parameters always_run\nStatus: {always_run} (Always Running)\nSave Polling: {save_polling} (Saved Polling)\nRunning BOT")
                    while True:
                        await types.ExtractPolling(save_polling=True)
                        await asyncio.sleep(1)
                        await func(*args, **kwargs)
                elif save_polling == False:
                    print(f"Detected Parameters always_run\nStatus: {always_run} (Only Run Once)\nSave Polling: {save_polling} (Not Save Polling)\nRunning BOT")
                    while True:
                        await types.ExtractPolling(save_polling=False) # Not Save Polling
                        await asyncio.sleep(1)
                        await func(*args, **kwargs)
            elif always_run == False:
                if save_polling == True:
                    print(f"Detected Parameters always_run\nStatus: {always_run} (Always Running)\nSave Polling: {save_polling} (Saved Polling)\nRunning BOT")
                    await types.ExtractPolling(save_polling=True) # Save Polling 
                    await asyncio.sleep(1)
                    await func(*args, **kwargs)
                elif save_polling == False:
                    print(f"Detected Parameters always_run\nStatus: {always_run} (Only Run Once)\nSave Polling: {save_polling} (Not Save Polling)\nRunning BOT")
                    await types.ExtractPolling(save_polling=False) # Not Save Polling
                    await asyncio.sleep(1)
                    await func(*args, **kwargs)
            else:
                print(f"Please Spesify always_run parameter\nIf Set To True BOT Will Receive The Latest Polls Continuously (Real Time) And Send Any Response Method Only Once\nIf Set To False BOT Will Receive Latest Poll Once And Send Any Response Method Only Once Then Bot Will Stop")
        return wrapped
    return wrapper