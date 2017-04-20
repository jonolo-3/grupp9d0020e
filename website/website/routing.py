from channels.routing import route
from sleep.consumers import ws_message, ws_connect, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect, path=r'^/graph/(?P<id>[^/]+)/values/$'),
    route("websocket.receive", ws_message, path=r'^/graph/(?P<id>[^/]+)/values/$'),
    route("websocket.disconnect", ws_disconnect, path=r'^/graph/(?P<id>[^/]+)/values/$')

]
