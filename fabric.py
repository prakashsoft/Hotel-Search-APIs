import time
from fabric.api import local, settings, prefix


SERVICES = ['scraper.scraperapi', 'hotel_search.hotel_search_service']

def start(srv):
    with prefix('source ./env/bin/activate'):
        local('which python2')
        local('python2 -m %s &' % srv)

def stop(srv):
    with settings(warn_only=True):
        local("kill -9 `ps -ax | grep -v grep | grep %s | awk '{print $1}'`" % srv)

def stop_services():
    for srv in SERVICES:
        stop(srv)

def start_services():
    for srv in SERVICES:
        start(srv)

def test():
    start_services()
    time.sleep(1)  # Waiting for services to complete start
    local('. ./env/bin/activate; python2 -m tests.scraperapi_test')
    stop_services()

def setup():
    local('virtualenv -p `which python2` env')
    local('. ./env/bin/activate; pip install -r requirements.txt')

def cleanup():
    local('rm -rf ./env')
    local("find . -name '*.pyc' -delete")
