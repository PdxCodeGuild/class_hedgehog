def main():
    import requests 
    print("Welcome the the lyrical machine! We'll find you're lyrics or won't! Try us to find out")
    artist = input("Please enter an artist: ")
    title = input(f'Please enter a song from {artist}: ')
    artist = artist.replace(' ', '%20')
    title = title.replace(' ', '%20')
    
    while True:
            
        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')

        lyrics = response.json()

        if 'lyrics' in lyrics:    
            print(lyrics['lyrics'])
            re_play = input("Would you like to try a different artist or title or quit? :")
        else:
            print("You either misspelt the artist, the title or you have no taste in music!")
            re_play = input("Would you like to try again? y/n? :")
    
        if re_play.lower() == 'artist':
            artist = input('Please enter your new artist:')
            title = input('Please enter your new title: ')
            continue
        elif re_play.lower() == 'title':
            title = input('Please enter your new title: ')
            continue
        elif re_play.lower() == 'n' or 'quit':
            break
        else:
            continue




main()