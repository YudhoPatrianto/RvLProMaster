import json
from .polling import polling
from .reset_polling import ResetPolling
from json import dumps
from typing import Optional, Literal
from functools import wraps
import asyncio

class telegram_types:
    def __init__(self):
        # Event Field
        self.event_field = ''
        # Reset Polling
        ResetPolling(self)
        # Message
        self.message = self.Message()
        # Chat Join Request
        self.chat_join_request = self.ChatJoinRequest()
        # New Chat Member
        self.new_chat_participant = self.NewChatParticipant()
        # Left Chat Participant
        self.left_chat_participant = self.LeftChatParticipant()
        # Channel
        self.channel_post = self.Channel()
        # Callback Data
        self.callback_query = self.CallbackQuery()

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
                    # [message][from]
                    self.message.From.id = out_polling['message']['from'].get('id','')
                    self.message.From.first_name = out_polling['message']['from'].get('first_name','')
                    self.message.From.last_name = out_polling['message']['from'].get('last_name','')
                    self.message.From.username = out_polling['message']['from'].get('username','')
                    
                    # [message]
                    self.message.text = out_polling['message'].get('text','')
                    self.message.date = out_polling['message'].get('date','')
                    self.message.message_id = out_polling['message'].get('message_id','')
                    
                    # [message][chat]
                    self.message.chat.id = out_polling['message']['chat'].get('id','')
                    self.message.chat.title = out_polling['message']['chat'].get('title','')
                    self.message.chat.username = out_polling['message']['chat'].get('username','')
                    
                    # UserJoined [new_chat_participant]
                    if 'new_chat_participant' in out_polling['message']:
                        # Event Field
                        self.event_field = 'new_chat_participant'
                        
                        # From
                        self.new_chat_participant.message.From.id = out_polling['message']['from'].get('id','')
                        self.new_chat_participant.message.From.first_name = out_polling['message']['from'].get('first_name','')
                        self.new_chat_participant.message.From.last_name = out_polling['message']['from'].get('last_name','')
                        self.new_chat_participant.message.From.username = out_polling['message']['from'].get('username','')
                        
                        # Groups
                        self.new_chat_participant.message.chat.id = out_polling['message']['chat'].get('id','')
                        self.new_chat_participant.message.chat.title = out_polling['message']['chat'].get('title','')
                        self.new_chat_participant.message.chat.username = out_polling['message']['chat'].get('username','')
                        
                        # New Chat Participant
                        self.new_chat_participant.message.new_chat_participant.id = out_polling['message']['new_chat_participant'].get('id','')
                        self.new_chat_participant.message.new_chat_participant.first_name = out_polling['message']['new_chat_participant'].get('first_name','')
                        self.new_chat_participant.message.new_chat_participant.last_name = out_polling['message']['new_chat_participant'].get('last_name','')
                        self.new_chat_participant.message.new_chat_participant.username = out_polling['message']['new_chat_participant'].get('username','')
                        
                    # Left User [left_chat_participant]
                    elif 'left_chat_participant' in out_polling['message']:
                        # Event Field
                        self.event_field = 'left_chat_participant'

                        
                # Chat Join Request [chat_join_request]
                elif 'chat_join_request' in out_polling:
                    # Event Field
                    self.event_field = 'chat_join_request'
                    
                    # ["chat_join_request"]["chat"]
                    self.chat_join_request.chat.id = out_polling["chat_join_request"]["chat"].get('id','')
                    self.chat_join_request.chat.title = out_polling["chat_join_request"]["chat"].get('title','')
                    self.chat_join_request.chat.username = out_polling["chat_join_request"]["chat"].get('username','')
                    
                    # ["chat_join_request"]["from"]
                    self.chat_join_request.From.id = out_polling["chat_join_request"]["from"].get('id','')
                    self.chat_join_request.From.first_name = out_polling["chat_join_request"]["from"].get('first_name','')
                    self.chat_join_request.From.last_name = out_polling["chat_join_request"]["from"].get('last_name','')
                    self.chat_join_request.From.username = out_polling["chat_join_request"]["from"].get('username','')
                    
                    
                # Channel [channel_post]
                elif 'channel_post' in out_polling:
                    # Event Field
                    self.event_field = 'channel_post'
                    
                    # Sender Chat
                    self.channel_post.sender_chat.id  = out_polling['channel_post']['sender_chat'].get('id','')
                    self.channel_post.sender_chat.title = out_polling['channel_post']['sender_chat'].get('title','')
                    
                    # Chat
                    self.channel_post.chat.id = out_polling['channel_post']['chat'].get('id','')
                    self.channel_post.chat.title = out_polling['channel_post']['chat'].get('title','')
                    
                    # channel_post
                    self.channel_post.message_id = out_polling['channel_post'].get('message_id','')
                    self.channel_post.text = out_polling['channel_post'].get('text','')
                
                # Callback Query [callback_query]
                elif 'callback_query' in out_polling:
                    self.callback_query.data = out_polling['callback_query'].get('data','') # ["callback_query"]["data"]
                    
                    # From [callback_query][from]
                    self.callback_query.From.id = out_polling['callback_query']['from'].get('id','') # ["callback_query"]["from"]["id"]
                    self.callback_query.From.first_name = out_polling['callback_query']['from'].get('first_name','') # ["callback_query"]["from"]["first_name"]
                    self.callback_query.From.last_name = out_polling['callback_query']['from'].get('last_name','') # ["callback_query"]["from"]["last_name"]
                    self.callback_query.From.username = out_polling['callback_query']['from'].get('username','') # ["callback_query"]["from"]["username"]
                    
                    # Chat [callback_query][message][chat]
                    self.callback_query.message.chat.id = out_polling['callback_query']['message']['chat'].get('id','')
                    self.callback_query.message.chat.title = out_polling['callback_query']['message']['chat'].get('title','')
                    self.callback_query.message.chat.username = out_polling['callback_query']['message']['chat'].get('username','')
                    
                return self
            except:
                pass

    # types: message
    class Message:
        def __init__(self) -> None:
            # Create Istance
            self.From = self._from() # ["message"]["from"]
            self.chat = self.Chat() # ["message"]["chat"]
            
            # message
            self.text = ''
            self.date = ''
            self.message_id = ''

        # ["message"]["from"]
        class _from:
            def __init__(self) -> None:
                self.id = ''
                self.first_name = ''
                self.last_name = ''
                self.username = ''
        # ["message"]["chat"]
        class Chat:
            def __init__(self) -> None:
                self.id = ''
                self.title = ''
                self.username = ''
                
    # types: chat_join_request
    class ChatJoinRequest:
        def __init__(self) -> None:
            # Create Istance
            self.From = self._from() # ["chat_join_request"]["from"]
            self.chat = self.Chat() # ["chat_join_request"]["chat"]
        # ["message"]["from"]
        class _from:
            def __init__(self) -> None:
                self.id = ''
                self.first_name = ''
                self.last_name = ''
                self.username = ''
        # ["message"]["chat"]
        class Chat:
            def __init__(self) -> None:
                self.id = ''
                self.title = ''
                self.username = ''
                
    # types: new_chat_participant
    class NewChatParticipant:
        def __init__(self) -> None:
            self.message = self.Message()
        
        # ["message"]
        class Message:
            def __init__(self) -> None:
                self.From = self._from() # ["message"]["from"]
                self.chat = self.Chat() # ["message"]["chat"]
                self.new_chat_participant = self._new_chat_participant() # ["message"]["new_chat_participant"]
            
            # ["message"]["from"]
            class _from:
                def __init__(self) -> None:
                    self.id = ''
                    self.first_name = ''
                    self.last_name = ''
                    self.username = ''
            # ["message"]["chat"]
            class Chat:
                def __init__(self) -> None:
                    self.id = ''
                    self.title = ''
                    self.username = ''
            
            class _new_chat_participant:
                def __init__(self) -> None:
                    self.id = ''
                    self.first_name = ''
                    self.last_name = ''
                    self.username = ''
                    
    # types: left_chat_participant
    class LeftChatParticipant:
        def __init__(self) -> None:
            # Create Istance
            self.message = self.Message() # ["left_chat_participant"]

        class Message:
            def __init__(self) -> None:
                self.From = self._from() # ["left_chat_participant"]["from"]
                self.chat = self.Chat() # ["left_chat_participant"]["chat"]
                self.left_chat_participant = self._left_chat_participant() # ["left_chat_participant"]

            # ["message"]["from"]
            class _from:
                def __init__(self) -> None:
                    self.id = ''
                    self.first_name = ''
                    self.last_name = ''
                    self.username = ''
            # ["message"]["chat"]
            class Chat:
                def __init__(self) -> None:
                    self.id = ''
                    self.title = ''
                    self.username = ''
                    
            class _left_chat_participant:
                def __init__(self) -> None:
                    self.id = ''
                    self.first_name = ''
                    self.last_name = ''
                    self.username = ''
    
    # types: channel_post                    
    class Channel:
        def __init__(self) -> None:
            self.sender_chat = self.SenderChat()
            self.chat = self.Chat()
            
            # Information
            self.message_id = ''
            self.text = ''
        
        # Sender Chat [channel_post][sender_chat]
        class SenderChat:
            def __init__(self) -> None:
                self.id = ''
                self.title = ''
        
        # Chat [channel_post][chat]        
        class Chat:
            def __init__(self) -> None:
                self.id = ''
                self.title = ''
                
    # Callback Data
    class CallbackQuery:
        def __init__(self) -> None:
            # Create Istance
            self.From = self._from() # ["callback_query"]["from"]
            self.message = self.Message() # ["callback_query"]["message"]["chat"]
            self.data = ''
            
            
        class _from:
            def __init__(self) -> None:
                self.id = ''
                self.first_name = ''
                self.last_name = ''
                self.username = ''
                
        class Message:
            def __init__(self) -> None:
                self.chat = self.Chat() # ["callback_query"]["message"]["chat"]
            # ["message"]["chat"]
            class Chat:
                def __init__(self) -> None:
                    self.id = ''
                    self.title = ''
                    self.username = ''

    def EventWatcher(self, EventSelector: Literal['UserRequest', 'UserJoined', 'UserLeft', 'Channel']) -> bool:
        self.message.text = ''
        # User Request To Join
        if EventSelector == "UserRequest" and self.event_field == 'chat_join_request':
            self.event_field = ''
            self.message.text = ''
            return True
        # User Joined 
        elif EventSelector == "UserJoined" and self.event_field == 'new_chat_participant':
            self.event_field = ''
            self.message.text = ''
            return True
        # User Left
        elif EventSelector == "UserLeft" and self.event_field == 'left_chat_participant':
            self.event_field = ''
            self.message.text = ''
            return True
        # Channel
        elif EventSelector == "Channel" and self.event_field == 'channel_post':
            self.event_field = ''
            self.message.text = ''
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