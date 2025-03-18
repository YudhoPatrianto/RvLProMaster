import json

class inlineKeyboard:
    class InlineButton:
        @staticmethod
        def Add(text, callback_data=None, url=None):
            """This function creates a button for the inline keyboard.

            Args:
                text (str): The text that will be displayed on the button.
                callback_data (str): The data that will be sent to the bot when the button is clicked. Defaults to None.
                url (str): The URL that will be opened when the button is clicked. Defaults to None.
            """
            if callback_data and url:
                raise ValueError("A button can only have either callback_data or a URL, not both.")
            
            button = {'text': text}
            if callback_data:
                button['callback_data'] = callback_data
            elif url:
                button['url'] = url
            return button

    @staticmethod
    def CreateKeyboard(*rows):
        """This function creates an inline keyboard.
        """
        keyboard = {'inline_keyboard': [list(row) for row in rows]}
        return json.dumps(keyboard)

# Create Inline Keyboard
InlineKeyboard = inlineKeyboard()