
import urllib.request
from html.parser import HTMLParser

class RequestObject():
    durl = None
    method = "GET"


HTMLINDN = 0

class HTMLParse(HTMLParser):
    global HTMLINDN
    def handle_starttag(self, tag, attrs):
        self.HTMLINDN += 1

    def handle_endtag(self, tag):
        self.HTMLINDN -= 1

    def handle_data(self, data):
        print("yes")
        print(('    '*self.HTMLINDN)+str(list(data).insert(0, '<').append('>')))

class ModuleSettings():
    showprg = False

# Errors

class URLEmpty(Exception):
    pass

class InvalidParam(Exception):
    pass

def dload(reqobj, fln):
    if isinstance(reqobj, RequestObject):
        if reqobj.durl != None:
            rOb = urllib.request.Request(reqobj.durl)
            resobj = urllib.request.urlopen(rOb)
            with open(fln, 'wb') as fl:
                resread = resobj.read()
                extension = fln.split('.')[1]
                if extension == "html":
                    print('yes')
                    parser = HTMLParse()
                    parser.feed(str(resobj.read())[17:])
                fl.write(resread)
        else:
            raise URLEmpty("Given URL is empty")
    else:
        raise InvalidParam("Parameter is not a class (RequestObject)")



