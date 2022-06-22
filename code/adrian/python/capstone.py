import requests



fam_response = requests.get("https://excuser.herokuapp.com/v1/excuse/family")
fam_excuse = fam_response.json()

off_response = requests.get("https://excuser.herokuapp.com/v1/excuse/office")
office_excuse = off_response.json()

kids_response = requests.get("https://excuser.herokuapp.com/v1/excuse/children")
kids_excuse = kids_response.json()

school_response = requests.get("https://excuser.herokuapp.com/v1/excuse/college")
school_excuse = school_response.json()

party_response = requests.get("https://excuser.herokuapp.com/v1/excuse/party")
party_excuse = party_response.json()

response = requests.get("https://excuser.herokuapp.com/v1/excuse")
excuse = response.text


def Excuses():
    print("Welcome to Random Excuse Generator!\n")

    choices = {
        '1': 'Family',
        '2': 'Office',
        '3': 'Children',
        '4': 'School',
        '5': 'Party',
    }


    
    for request, choice in choices.items():
        print(f'{request}. {choice}')

    user_input = input("\nPlease choose one of the following catagories: ")
    user_input = choices.get(user_input)

    if user_input == 'Family':
        print(f"\n{fam_excuse}\n")
    elif user_input == 'Office':
        print(f"\n{office_excuse}\n")
    elif user_input == 'Children':
        print(f"\n{kids_excuse}\n")
    elif user_input == 'School':
        print(f"\n{school_excuse}\n")
    elif user_input == 'Party':
        print(f"\n{party_excuse}\n")
    else:
        print(f"\nNot an option try again\n")
        


Excuses()