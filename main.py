import webapp2, caesar

form = """
    <form>
        <textarea>hello butts</textarea>
        <br/>
        <input type='submit'/>
    </form>
    """

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
