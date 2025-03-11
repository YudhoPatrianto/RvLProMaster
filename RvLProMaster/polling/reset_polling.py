def ResetPolling(obj):

    # Message Information
    obj.chat_id = ''
    obj.text = ''
    obj.reply_message = ''
    obj.group_title = ''

    # User Information
    obj.first_name = ''
    obj.last_name = ''
    obj.username = ''
    obj.user_id = ''

    # new_chat_participant
    obj.first_name_joined = ''
    obj.last_name_joined = ''
    obj.username_joined = ''
    obj.user_id_joined = ''
    obj.group_title_joined = ''

    # left_chat_member
    obj.first_name_left = ''
    obj.last_name_left = ''
    obj.username_left = ''
    obj.user_id_left = ''
    obj.group_title_left = ''

    # chat_join_request
    obj.first_name_request = ''
    obj.last_name_request = ''
    obj.username_request = ''
    obj.user_id_request = ''
    obj.group_title_request = ''

    # Inline Keyboard/Buttons
    obj.callback_data = ''
    obj.message_id = ''

    # Channel Information
    obj.channel_text = ''
    obj.channel_chat_id = ''
    obj.channel_reply_message = ''
    obj.channel_title = ''