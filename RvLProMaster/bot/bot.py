from httpx import AsyncClient
from RvLProMaster import endpoint
from typing import Literal

class Bot:
    """The main class for the bot.
    """
    class Updates:
        """The Bots Update
        """
        @staticmethod
        async def getUpdates(offset=None):
            async with AsyncClient() as client:
                payload = {
                    'offset': offset,
                    'timeout': 20
                }
                r = await client.get(f"{endpoint}/getUpdates", params=payload)
                r_data = r.json()
                return r_data
            
    class Methods:
        """The Bots Methods
        """
        @staticmethod
        async def sendMessage(
            chat_id: int | str | None = None,
            text: str | None = None,
            parse_mode: Literal['HTML', 'Markdown', 'MarkdownV2'] = 'MarkdownV2',
            disable_notification: bool | None = None,
            protect_content: bool | None = None,
            reply_message: int | str | None = None,
        ):
            """Use this method to send text messages

            Args:
                chat_id (int | str | None): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                text (str | None): _description_. Defaults to None.
                parse_mode (Literal[&#39;HTML&#39;, &#39;Markdown&#39;, &#39;MarkdownV2&#39;]): Mode for parsing entities in the message text, Default MarkdownV2
                disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
                protect_content (bool): Protects the contents of the sent message from forwarding and saving.
                reply_message (int | str): Reply Message? Defaults to None.
            """
            payload = {
                'chat_id': chat_id,
                'text': text,
                'parse_mode': parse_mode,
                'disable_notification': disable_notification,
                'protect_content': protect_content,
                'reply_to_message_id': reply_message
            }
            async  with AsyncClient() as client:
                r = await client.post(f"{endpoint}/sendMessage", data=payload)
                r_data = r.json()
                return r_data
        
        @staticmethod
        async def getMe():
            async with AsyncClient() as client:
                r = await client.get(f"{endpoint}/getMe")
                r_data = r.json()
                return r_data
        
        @staticmethod
        async def editMessageText(
            chat_id: int | str | None = None,
            message_id: int | str | None = None,
            text: str | None = None,
            parse_mode: Literal['HTML', 'Markdown', 'MarkdownV2'] = 'MarkdownV2',
            reply_message: int | str | None = None
        ):
            """Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.

            Args:
                chat_id (int | str | None): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                message_id (int | str | None): Required if inline_message_id is not specified. Identifier of the message to edit
                text (str | None): 	New text of the message, 1-4096 characters after entities parsing
                parse_mode (Literal[&#39;HTML&#39;, &#39;Markdown&#39;, &#39;MarkdownV2&#39;]): Mode for parsing entities in the message text.
                reply_message (int | str | None): Reply Message? Defaults to None.

            Returns:
                _type_: _description_
            """
            async with AsyncClient() as client:
                payload = {
                    'chat_id': chat_id,
                    'message_id': message_id,
                    'text': text,
                    'parse_mode': parse_mode,
                    'reply_to_message_id': reply_message
                }
                r = await client.post(f"{endpoint}/editMessageText", json=payload)
                r_data = r.json()
                return r_data
        
        @staticmethod
        async def deleteMessage(
            chat_id: int | str | None = None,
            message_id: int | str | None = None 
        ):
            async with AsyncClient() as client:
                payload = {
                    'chat_id': chat_id,
                    'message_id': message_id
                }
                r = await client.post(f"{endpoint}/deleteMessage", json=payload)
                r_data = r.json()
                return r_data
# create Istance bot
bot = Bot()