import falcon

from resources.message_v1 import MessageV1
from resources.message_v2 import MessageV2

app = falcon.App()

app.add_route('/api/v1/message', MessageV1())
app.add_route('/api/v2/message', MessageV2())