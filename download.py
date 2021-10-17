
import urllib.request


class RequestObject():
    dUrl = None


# Errors

class URLEmpty(Exception):
    pass

class InvalidParam(Exception):
    pass

def Download(reqobj, fln):
    if isinstance(reqobj, RequestObject):
        if reqobj.durl != None:
            rOb = urllib.request.Request(reqobj.durl)
            resobj = urllib.request.urlopen(rOb)
            with open(fln, 'wb') as fl:
                fl.write(resobj.read())
        else:
            raise URLEmpty("Given URL is empty")
    else:
        raise InvalidParam("Parameter is not the class object RequestObject")



