import webapp2
from google.appengine.api import users

# app.yaml enforces that there will be a logged in

class SimpleUserApiHandler(webapp2.RequestHandler):
    # create
    def post(self, itemID=None):
        try:
            user = users.get_current_user()
            response = SimpleUserApiService.create(user, self.request.body)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # read
    def get(self, itemID=None):
        try:
            user = users.get_current_user()
            if itemID:
                response = SimpleUserApiService.read(user, itemID)
            else:
                response = SimpleUserApiService.readAll(user)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # update
    def put(self, itemID):
        try:
            user = users.get_current_user()
            if not itemID:
                raise ApiException(400, 'Bad Request')
            response = SimpleUserApiService.update(user, itemID, self.request.body)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # delete
    def delete(self, itemID):
        try:
            user = users.get_current_user()
            if not itemID:
                raise ApiException(400, 'Bad Request')
            response = SimpleUserApiService.delete(user, itemID)
            return self.response.write(response)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)


class SimpleUserApiService():
    # create
    @staticmethod
    def create(user, objectData):
        return 'create ok'

    # read all
    @staticmethod
    def readAll(user):
        return 'read all ok'

    # read
    @staticmethod
    def read(user, objectID):
        return 'read ok'

    # update
    @staticmethod
    def update(user, objectID, objectData):
        return 'update ok'

    # delete
    @staticmethod
    def delete(user, objectID):
        return 'delete ok'


class ApiException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message


app = webapp2.WSGIApplication([
    ('/_api/simpleUser/?(\d*)', SimpleUserApiHandler)
], debug=False)
