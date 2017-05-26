import os
import sys
import logging
from ConfigParser import ConfigParser

from tornado import gen, ioloop, web

from flight_search import FlightSearch

log = logging.getLogger('hotels-search')
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
log.setLevel(logging.DEBUG)

CONFIG = ConfigParser()
CONFIG.read('./providers.cfg')
CONFIG = dict(CONFIG.items('DEFAULT'))


class FlightSearchHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        fs = FlightSearch(CONFIG)
        list_of_results = yield fs.fetch_results()
        self.write(str(list_of_results))


ROUTES = [(r"/hotel/search", FlightSearchHandler)]


def run():
    port = CONFIG['port']
    app = web.Application(ROUTES, debug=True)
    app.listen(port)
    log.info("Started server at port {}".format(port))
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
