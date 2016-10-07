import webapp2


class SimpleApiHandler(webapp2.RequestHandler):
    # create
    def post(self, itemID=None):
        try:
            response = SimpleApiService.create(self.request.body)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # read
    def get(self, itemID=None):
        try:
            if itemID:
                response = SimpleApiService.read(itemID)
            else:
                response = SimpleApiService.readAll()
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # update
    def put(self, itemID):
        try:
            if not itemID:
                raise ApiException(400, 'Bad Request')
            response = SimpleApiService.update(itemID, self.request.body)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)
        return self.response.write(response)

    # delete
    def delete(self, itemID):
        try:
            if not itemID:
                raise ApiException(400, 'Bad Request')
            response = SimpleApiService.delete(itemID)
            return self.response.write(response)
        except ApiException as e:
            self.response.status = e.code
            return self.response.write(e.message)


class SimpleApiService():
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
    ('/_api/simple/?(\d*)', SimpleApiHandler)
], debug=False)
