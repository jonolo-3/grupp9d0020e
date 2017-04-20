from channels import Group
from channels.sessions import channel_session

@channel_session
def ws_connect(message, id):
    print("Someone connected.")
    path = message['path']

    print(id, "id")                                                  # i.e. /sensor/

    message.channel_session['readSensor'] = 'website'
    Group(id).add(message.reply_channel)                             # Adds user to group for broadcast
    # message.reply_channel.send({                                            # Reply to individual directly
    #    "text": "You're connected to sensor group :) ",
    # })

@channel_session
def ws_message(message, id):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    print(id, "id")
    print("Received!!" + message['text'])
    #Group("website").send({'text': message['text']})

@channel_session
def ws_disconnect(message, id):
    print("Someone left us...")
    print(id, "id")
    Group(id).discard(message.reply_channel)
