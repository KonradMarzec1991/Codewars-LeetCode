class Router(object):

    def __init__(self):
        self.routes = {}

    def bind(self, url, method, response):
        self.routes[url, method] = response

    def runRequest(self, url, method):
        if (url, method) in self.routes:
            return self.routes[url, method]()
        return 'Error 404: Not Found'
