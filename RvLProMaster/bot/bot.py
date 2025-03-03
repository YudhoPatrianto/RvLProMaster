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
                    'timeout': 10
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
            reply_markup: str | None = None,
            reply_message: int | str | None = None,
        ):
            """Use this method to send text messages

            Args:
                chat_id (int | str | None): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                text (str | None): _description_
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
                'reply_markup': reply_markup,
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

        @staticmethod
        async def sendVideo(
            chat_id: int | str | None = None,
            video: str | None = None,
            caption: str | None = None,
            parse_mode: Literal['HTML', 'Markdown', 'MarkdownV2'] = 'MarkdownV2',
            has_spoiler: bool | None = None,
            supports_streaming: bool | None = None,
            disable_notification: bool | None = None,
            protect_content: bool | None = None,
            reply_message: str | None = None
        ):
            """Use this method to send video files, Telegram clients support MPEG4 videos 

            Args:
                chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                video (str): Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data
                caption (str): Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing
                parse_mode (Literal[&#39;HTML&#39;, &#39;Markdown&#39;, &#39;MarkdownV2&#39;]): Mode for parsing entities in the video caption. Defaults to 'MarkdownV2'.
                has_spoiler (bool): Pass True if the video needs to be covered with a spoiler animation
                supports_streaming (bool): Pass True if the uploaded video is suitable for streaming
                disable_notification (bool): Sends the message silently. Users will receive a notification with no sound.
                protect_content (bool): Protects the contents of the sent message from forwarding and saving
                reply_message (str): Reply Message? Defaults to None.
            """
            async with AsyncClient() as client:
                with open(f"{video}", 'rb') as f:
                    video_binary = {'video': f}
                    payload = {
                        'chat_id': chat_id,
                        'caption': caption,
                        'parse_mode': parse_mode,
                        'supports_streaming': supports_streaming,
                        'disable_notification': disable_notification,
                        'protect_content': protect_content,
                        'has_spoiler': has_spoiler,
                        'reply_to_message_id': reply_message
                    }
                    r = await client.post(f"{endpoint}/sendVideo", data=payload, files=video_binary)
                    r_data = r.json()
                    return r_data
                
        # approveChatJoinRequest
        @staticmethod
        async def approveChatJoinRequest(
            chat_id: int | str | None = None,
            user_id: int | str | None = None
        ):
            async with AsyncClient() as client:
                payload = {
                    'chat_id': chat_id,
                    'user_id': user_id
                }
                r = await client.post(f"{endpoint}/approveChatJoinRequest", json=payload)
                r_data = r.json()
                return r_data

        # declineChatJoinRequest
        @staticmethod
        async def declineChatJoinRequest(
            chat_id: int | str | None = None,
            user_id: int | str | None = None
        ):
            async with AsyncClient() as client:
                payload = {
                    'chat_id': chat_id,
                    'user_id': user_id
                }
                r = await client.post(f"{endpoint}/declineChatJoinRequest", json=payload)
                r_data = r.json()
                return r_data
            
        # sendPhoto
        @staticmethod
        async def sendPhoto(
            chat_id: int | str | None = None,
            photo: str | None = None,
            caption: str | None = None,
            parse_mode: Literal['HTML', 'Markdown', 'MarkdownV2'] = 'MarkdownV2',
            has_spoiler: bool | None = None,
            disable_notification: bool | None = None,
            protect_content: bool | None = None,
            reply_markup: str | None = None,
            reply_message: int | str | None = None
        ):
            """Use this method to send photos

            Args:
                chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
                photo (str | None): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20.
                caption (str | None): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
                parse_mode (Literal[&#39;HTML&#39;, &#39;Markdown&#39;, &#39;MarkdownV2&#39;]): Mode for parsing entities in the photo caption Defaults to 'MarkdownV2'.
                has_spoiler (bool | None): Pass True if the photo needs to be covered with a spoiler animation
                disable_notification (bool | None): Sends the message silently. Users will receive a notification with no sound.
                protect_content (bool | None): Protects the contents of the sent message from forwarding and saving
                reply_markup (str | None): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user
                reply_message (int | str | None): Reply Message?. Defaults to No.

            Returns:
                _type_: _description_
            """
            async with AsyncClient() as client:
                # Photo With Links
                if str(photo).startswith('https://') or str(photo).startswith('http://'):
                    payload = {
                        'chat_id': chat_id,
                        'photo': photo,
                        'caption': caption,
                        'parse_mode': parse_mode,
                        'disable_notification': disable_notification,
                        'protect_content': protect_content,
                        'reply_markup': reply_markup,
                        'reply_to_message_id': reply_message
                    }
                    r = await client.post(f"{endpoint}/sendPhoto", data=payload)
                    r_data = r.json()
                    return r_data
                # Photo With File
                else:
                    payload = {
                        'chat_id': chat_id,
                        'caption': caption,
                        'parse_mode': parse_mode,
                        'disable_notification': disable_notification,
                        'protect_content': protect_content,
                        'has_spoiler': has_spoiler,
                        'reply_to_message_id': reply_message
                    }
                    with open(f'{photo}', 'rb') as read_img:
                        photo_binary = {'photo': read_img}
                        r = await client.post(f"{endpoint}/sendPhoto", data=payload, files=photo_binary)
                        r_data = r.json()
                        return r_data
# create Istance bot
bot = Bot()