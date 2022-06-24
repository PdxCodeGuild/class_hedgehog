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
        print(f"\nFamily excuse: {fam_excuse[0]['excuse']}\n")
    elif user_input == 'Office':
        print(f"\nOffice excuse: {office_excuse[0]['excuse']}\n")
    elif user_input == 'Children':
        print(f"\nKids excuse: {kids_excuse[0]['excuse']}\n")
    elif user_input == 'School':
        print(f"\nSchool excuse: {school_excuse[0]['excuse']}\n")
    elif user_input == 'Party':
        print(f"\nParty excuse: {party_excuse[0]['excuse']}\n")
    else:
        print(f"\nNot an option try again\n")
        


Excuses()