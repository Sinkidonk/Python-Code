import urllib.request
page = urllib.request.urlopen("https://tobyfox.bandcamp.com/track/dont-forget")

pageText = page.read()

print(pageText)
