import webapp2, caesar

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hello!"
        self.response.write(caesar.encrypt(message, 13))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
