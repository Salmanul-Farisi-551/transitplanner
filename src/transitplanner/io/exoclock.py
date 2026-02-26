from .loaders import load_json

def load_exoclock_data():
    url = "https://www.exoclock.space/database/planets_json"
    return  load_json(url)




