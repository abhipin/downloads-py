# demonstration

import download

# create a RequestObject
request = download.RequestObject()

#set durl to the url that you want to download
request.duUl = "https://www.google.com"

#call dload() to download
download.dload(request, "test.html")
