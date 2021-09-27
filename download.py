
import urllib.request

class RequestObject():
    durl = None
    method = "GET"

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
                fl.write(resobj.read())
        else:
            raise URLEmpty("Given URL is empty")
    else:
        raise InvalidParam("Parameter is not a class (RequestObject)")



