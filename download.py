from os import read
import urllib.request
import http.client as HTTP
import socket
import hashlib
import time
import urllib.error as ErrReq

LOGPATH = None


class RequestObject():
    isHTTPurl = True
    dUrl = None
    LogErrors = False

class ResponseObject():
    pSHA512 = ""
    


def Log(rqob,txt):
    global LOGPATH
    if LOGPATH == None:
        LOGPATH = ""
    if rqob.LogErrors != True:
        return "LogErrors not enabled"
    fl = open(LOGPATH+"log.txt", "a")
    print(LOGPATH+"log.txt")
    fl.write(str(time.time()).split('.')[0] + ": " + txt + "\n")
    fl.close()

# Error classes

class URLEmpty(Exception):
    pass

class InvalidParam(Exception):
    pass

class ConnectionFail(Exception):
    pass

class ImproperResponse(Exception):
    pass

# Functions

def Download(reqobj, fln, ds=""):
    if isinstance(reqobj, RequestObject):
        if reqobj.dUrl != None:
            rOb = urllib.request.Request(reqobj.dUrl)
            # Send request
            try:
                resobj = urllib.request.urlopen(rOb)
            except HTTP.RemoteDisconnected:
                Log(reqobj,"ConnectionFail:RemoteDisconnected > The connection was closed by the server for some unknown reason.")
                raise ConnectionFail("Connection was closed by the server, check log (if enabled) for more information.")
            except HTTP.BadStatusLine:
                Log(reqobj,"ConnectionFail:BadStatusLine > The response code given by server wasn't understood.")
                raise ConnectionFail("Unable to understand response code, check log (if enabled) for more information.")
            except HTTP.LineTooLong:
                Log(reqobj,"ImproperResponse:LineTooLong > Header size exceeded MAXLINE, giving a LTL error.")
                raise ImproperResponse("Server returned a large header response, check log (if enabled) for more information.")
            except ErrReq.URLError:
                Log(reqobj,"ConnectionFail:URLError > Failed to connect to the specified Host. You may not be connected to the internet.")
                raise ConnectionFail("Failed to connect to Host, check log (if enabled) for more information.")
                
            Log(reqobj,"Connection established with " + reqobj.dUrl + ", Host IP: " + socket.gethostbyname(reqobj.dUrl.split('/')[3]))
            readbytes = resobj.read()
            with open(ds+fln, 'wb') as fl:
                fl.write(readbytes)
            rp = ResponseObject()
            rp.pSHA512 = hashlib.sha512(readbytes).hexdigest()
            return rp
        else:
            raise URLEmpty("Given URL is empty")
    else:
        raise InvalidParam("Parameter is not the class object RequestObject")

def SetLogPath(path):
    global LOGPATH
    newstr = path
    print(path)
    if path.endswith("/") != True: 
        newstr = list(path)
        newstr.append('/')
        newstr = ''.join(newstr)
    elif path.endswith("\\") != True and path.endswith("/") != True:
        newstr = list(path)
        newstr.append('\\')
        newstr = ''.join(newstr)
    print(newstr)
    LOGPATH = newstr