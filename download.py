
import urllib.request
import http.client as HTTP


class RequestObject():
    isHTTPurl = True
    dUrl = None
    LogErrors = False

def Log(txt):
    fl = open("demofile.txt", "w")
    fl.write(txt)
    fl.close()

# Error classes

class URLEmpty(Exception):
    pass

class InvalidParam(Exception):
    pass

class ConnectionFail(Exception):
    pass

class ImproperResponse(Exception):
    Log(Exception)
    pass

def Download(reqobj, fln, ds=""):
    if isinstance(reqobj, RequestObject):
        if reqobj.dUrl != None:
            rOb = urllib.request.Request(reqobj.dUrl)

            try:
                resobj = urllib.request.urlopen(rOb)
            except HTTP.RemoteDisconnected:
                raise ConnectionFail("Connection was closed by the server.")
            except HTTP.BadStatusLine:
                raise ConnectionFail("Unable to understand response code.")
            except HTTP.LineTooLong:
                raise ImproperResponse("Server returned a extremely large response.")
            
            with open(fln, 'wb') as fl:
                fl.write(resobj.read())
        else:
            raise URLEmpty("Given URL is empty")
    else:
        raise InvalidParam("Parameter is not the class object RequestObject")



