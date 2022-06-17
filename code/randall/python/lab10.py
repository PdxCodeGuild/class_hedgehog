"""dad joke api"""
def get_joke():
    """get a dad joke"""
    import requests
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response.json()['joke']
print(get_joke())