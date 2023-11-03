track_list = {'wu%20Tang': 'sound%20the%20rns'}


for key, value in track_list.items():
    key = key.replace('%20', ' ')
    value = value.replace('%20', ' ')
    print(key, value)
   
