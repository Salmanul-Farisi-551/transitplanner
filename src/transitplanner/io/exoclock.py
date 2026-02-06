import urllib.request, json

def load_exoclock_data():
    url = "https://www.exoclock.space/database/planets_json"
    return json.loads(urllib.request.urlopen(url).read())
