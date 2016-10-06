import webapp2
from google.appengine.api import users


class ApiHandler(webapp2.RequestHandler):
    # create
    def post(self, itemID=None):
        try:
            response = ApiService.create(self.request.body)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # read
    def get(self, itemID=None):
        try:
            if itemID:
                response = ApiService.read(itemID)
            else:
                response = ApiService.readAll()
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # update
    def put(self, itemID):
        try:
            if not itemID:
                raise ApiException(400, 'Bad Request')
            response = ApiService.update(itemID, self.request.body)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # delete
    def delete(self, itemID):
        try:
            if not itemID:
                raise ApiException(400, 'Bad Request')
            response = ApiService.delete(itemID)
            return self.response.write(response)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)


class ApiService():
    # create
    @staticmethod
    def create(objectData):
        return 'create ok'

    # read all
    @staticmethod
    def readAll():
        return 'read all ok'

    # read
    @staticmethod
    def read(objectID):
        return 'read ok'

    # update
    @staticmethod
    def update(objectID, objectData):
        return 'update ok'

    # delete
    @staticmethod
    def delete(objectID):
        return 'delete ok'


class ApiException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


app = webapp2.WSGIApplication([
    ('/_api/objects/?(\d*)', ApiHandler)
], debug=False)
