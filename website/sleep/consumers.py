from channels import Group
from channels.sessions import channel_session

@channel_session
def ws_connect(message):
    print("Someone connected.")
    path = message['path']                                                      # i.e. /sensor/

    message.channel_session['readSensor'] = 'website'
    Group("values").add(message.reply_channel)                             # Adds user to group for broadcast
    # message.reply_channel.send({                                            # Reply to individual directly
    #    "text": "You're connected to sensor group :) ",
    # })

@channel_session
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print("Received!!" + message['text'])
    #Group("website").send({'text': message['text']})

@channel_session
def ws_disconnect(message):
    print("Someone left us...")
    Group("values").discard(message.reply_channel)
