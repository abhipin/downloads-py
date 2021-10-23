# demonstration

import download

# create a Request object
request = download.Request()

#set download url to the url that you want to download
request.dUrl = "https://winproc.github.io/me.github.io"
request.LogErrors = True

#call download() to download
res = download.Download(request, "test.html")

# hashes
print(res.pSHA512)
print(res.pSHA1)
print(res.pSHA224)
print(res.pSHA256)
