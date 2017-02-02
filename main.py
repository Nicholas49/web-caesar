import webapp2
import caesar
import cgi

def build_page(textcontent):
    styles = "<style>.numb{width:40px}</style>"
    header = "<head>" + styles + "</head>"
    outpt = header + "<p>Enter a message to encrypt:</p><form method='post'><textarea name='massage'>" + textcontent + "</textarea><p>Rotate by:<input type='number' name='bread' class='numb'></p><input type='submit'/></form>"
    return outpt


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(build_page(""))

    def post(self):
        ms = self.request.get("massage")
        rt = int(self.request.get("bread"))
        enc = caesar.encrypt(ms,rt)
        esc_enc = cgi.escape(enc)
        self.response.write(build_page(esc_enc))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)