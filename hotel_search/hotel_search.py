import json

from tornado import gen
from tornado.httpclient import AsyncHTTPClient


class HotelSearch(object):
    def __init__(self, config):
        self.config = config
        self.providers = self.config['providers'].split(',')
        self.urls = ['http://{}:{}/scrapers/{}'.format(self.config['scraper_hostname'],
                     self.config['scraper_port'], p) for p in self.providers]

    @gen.coroutine
    def fetch_results(self):
        httpclient = AsyncHTTPClient()
        responses = yield [httpclient.fetch(u) for u in self.urls]
        responses = [json.loads(r.body.decode('utf-8', 'ignore')) for r in responses]
        sorted_results = yield self.merge_results(responses)
        raise gen.Return(json.dumps({"results": sorted_results}))

    @gen.coroutine
    def merge_results(self, responses):
        responses = [r['results'] for r in responses]
        responses = [r for provider_list in responses for r in provider_list]
        raise gen.Return(sorted(responses, key=lambda x: x['details']))


#/Users/Prakash/Hipmunk/hotel_search
