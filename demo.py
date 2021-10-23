# demonstration

import download

# create a RequestObject
request = download.RequestObject()

#set download url to the url that you want to download
request.dUrl = "https://winproc.github.io/me.github.io"
request.LogErrors = True

#call download() to download
res = download.Download(request, "test.html")
print(res.pSHA512)
