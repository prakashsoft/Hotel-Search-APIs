from hotel_search.scrapers.common import Scraper


class OrbitzScraper(Scraper):
    provider = "Orbitz"
    def load_results(self):
        self.load_fake_results(xrange(1, 500, 4))
