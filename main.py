import webapp2, caesar
from cgi import escape

def build_page(areamessage="", setnum=0):
    form = """
    <h1>A simple Caesar cypher</h1>
    <form method='post'>
        <textarea name='message' style='height: 100px; width: 400px;'>%s</textarea>
        <br/>
        <label>
            Rotate by:
            <input type='number' name='rotnum' value='%s'>
        </label>
        <br/>
        <input type='submit'/>
    </form>
    <p><strong>A tip!</strong> ROT-13 twice for double the security!</p>
    <p style='font-size: 0.8em;'>Coded by Ada Nakama</p>
    """
    return form % (areamessage, setnum)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = build_page("Please type the text to be encrypted here", 13)
        self.response.write(page)
        
    def post(self):
        rotnum = self.request.get("rotnum")
        if rotnum == "":
            rotnum = 0
            encmessage = "Error: please specify a valid rotation number"
        else:
            rotnum = int(rotnum)
            encmessage = caesar.encrypt(self.request.get("message"), rotnum)
        page = build_page(escape(encmessage), rotnum)
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
