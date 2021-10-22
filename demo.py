# demonstration

import download

# create a RequestObject
request = download.RequestObject()

#set durl to the url that you want to download
request.dUrl = "https://www.google.com"
request.LogErrors = True

#call dload() to download
download.Download(request, "test.html")
