import urllib.request, json

def load_json(url):
    return json.loads(urllib.request.urlopen(url).read())
