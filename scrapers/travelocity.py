from hotel_search.scrapers.common import Scraper


class TravelocityScraper(Scraper):

    provider = "Travelocity"
    def load_results(self):
        self.load_fake_results(xrange(1, 500, 3))
