
import urllib.request

class RequestObject():
    durl = None
    method = "GET"

# Errors

class URLEmpty(Exception):
    pass

class InvalidParam(Exception):
    pass

def dload(reqobj):
    if isinstance(reqobj, RequestObject):
        if reqobj.durl != None:
            rOb = urllib.request.Request(reqobj.durl)
            resobj = urllib.request.urlopen(rOb)
        else:
            raise URLEmpty("Given URL is none")
    else:
        raise InvalidParam("Parameter is not a class (RequestObject)")



