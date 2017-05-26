from tornado import gen
from datetime import datetime, timedelta
import simplejson as json
import os
from random import randint

class HotelSearch(object):
    def __init__(self,provider, price,location):
        self.provider = provider
        self.price = price
        self.location = hotel_location
@property
    def details(self):
        duration = self.arrive_time - self.depart_time
        return duration.total_seconds() / self.price

    def serialize(self):
        return {
            "provider": self.provider,
            "details": self.details,
            "price": self.price,
            "location": self.hotel_location,
        }


class Scraper(object):

    provider = None

    @gen.coroutine
    def run(self):
        self.results = []

        # wait a bit
        yield gen.sleep(2)

        self.load_fake_results(xrange(1, 20, self.step))
        self.results.sort(key=lambda r: r['ecstasy'], reverse=True)

        raise gen.Return(self.results)



    def load_results(self):
        raise NotImplementedError


    def load_fake_results(self, range_iter):
        now = datetime.utcnow().replace(second=0, microsecond=0)
        for i in range_iter:
            price = 300 - i
            depart_time = now + timedelta(hours=i)
            arrive_time = depart_time + timedelta(hours=1, minutes=i / 20)
            self.add_result(
                price,
                location,
            )

    def add_result(self, price, location):
        result = HotelSearch(
            self.provider,
            price,
            location,
        )
        self.results.append(result)
