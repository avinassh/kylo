import os
import json
import random

from tornado import web, ioloop, log
from tornado.options import parse_command_line
from tornado.options import define, options
from sockjs.tornado import SockJSRouter, SockJSConnection

from inference import find_best_match
from settings import STATIC_DIR

logger = log.logging.getLogger("tornado.general")

define('port', default='9999', help='HTTP listening port', type=str)


class DemoHandler(web.RequestHandler):

    def get(self):
        self.render(os.path.join(STATIC_DIR, 'index.html'))


class SockConnection(SockJSConnection):
    def on_message(self, msg):
        # we are expecting a json message:
        # {"question": "question text"}
        try:
            request = json.loads(msg)
            text = request['question']
        except(ValueError, KeyError):
            return
        match = find_best_match(text=text)
        # we get accuracy value like `0.9274999499320984`
        # so we multiply by 100 to get `92.74999499320984`
        # then we set the float to two decimal points to get `92.74`
        accuracy = float("{0:.2f}".format(match['cos_sim'] * 100))
        answer = random.choice(match['best_match'])
        logger.info('question: {}, answer: {}, accuracy: {}'.format(
            text, answer, accuracy))
        reply = "{} \n(accuracy: {})".format(answer, accuracy)
        response = {'bot_reply': reply, 'answer': answer, 'accuracy': accuracy}
        self.send(response)

    def on_open(self, info):
        logger.info('new connection opened')
        self.send('hello!')

    def on_close(self):
        logger.info('closing the connection')


if __name__ == '__main__':
    parse_command_line()
    port = options.port
    logger.info('starting the server at {}'.format(port))
    handlers = [(r'/demo', DemoHandler),
                (r'/(.*)', web.StaticFileHandler, {'path': STATIC_DIR})]
    EchoRouter = SockJSRouter(SockConnection, '/socks')
    EchoRouter.urls.extend(handlers)
    app = web.Application(EchoRouter.urls, debug=True)
    app.listen(port)
    ioloop.IOLoop.instance().start()
