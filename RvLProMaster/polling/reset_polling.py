def ResetPolling(obj):
    # Event Field
    obj.event_field = ''
    
    # message
    obj.message.From.id = ''
    obj.message.From.first_name = ''
    obj.message.From.last_name = ''
    obj.message.From.username = ''
    obj.message.text = ''
    obj.message.date = ''
    obj.message.message_id = ''
    obj.message.chat.id = ''
    obj.message.chat.title = ''
    obj.message.chat.username = ''
    
    # new_chat_member
    obj.new_chat_participant.message.From.id = ''
    obj.new_chat_participant.message.From.first_name = ''
    obj.new_chat_participant.message.From.last_name = ''
    obj.new_chat_participant.message.From.username = ''
    obj.new_chat_participant.message.chat.id = ''
    obj.new_chat_participant.message.chat.title = ''
    obj.new_chat_participant.message.chat.username = ''
    obj.new_chat_participant.message.new_chat_participant.id = ''
    obj.new_chat_participant.message.new_chat_participant.first_name = ''
    obj.new_chat_participant.message.new_chat_participant.last_name = ''
    obj.new_chat_participant.message.new_chat_participant.username = ''
    
    # left_chat_participant
    obj.left_chat_participant.message.From.id = ''
    obj.left_chat_participant.message.From.first_name = ''
    obj.left_chat_participant.message.From.last_name = ''
    obj.left_chat_participant.message.From.username = ''
    obj.left_chat_participant.message.chat.id = ''
    obj.left_chat_participant.message.chat.title = ''
    obj.left_chat_participant.message.chat.username = ''
    obj.left_chat_participant.message.left_chat_participant.id = ''
    obj.left_chat_participant.message.left_chat_participant.first_name = ''
    obj.left_chat_participant.message.left_chat_participant.last_name = ''
    obj.left_chat_participant.message.left_chat_participant.username = ''
    
    # chat_join_request
    obj.chat_join_request.chat.id = ''
    obj.chat_join_request.chat.title = ''
    obj.chat_join_request.chat.username = ''
    obj.chat_join_request.From.id = ''
    obj.chat_join_request.From.first_name = ''
    obj.chat_join_request.From.last_name = ''
    obj.chat_join_request.From.username = ''
    
    # channel_post
    obj.channel_post.sender_chat.id  = '' 
    obj.channel_post.sender_chat.title = '' 
    obj.channel_post.chat.id = '' 
    obj.channel_post.chat.title = '' 
    obj.channel_post.message_id =  ''
    
    # Callback Query
    obj.callback_query.data = ''
    obj.callback_query.From.id = ''
    obj.callback_query.From.first_name = ''
    obj.callback_query.From.last_name = ''
    obj.callback_query.From.username = ''
    obj.callback_query.message.chat.id = ''
    obj.callback_query.message.chat.title = '' 
    obj.callback_query.message.chat.username = '' 
