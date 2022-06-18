def main():
    import requests 
    print("Welcome the the lyrical machine! We'll find you're lyrics or won't! Try us to find out")
    
    while True:
        artist = input("Please enter an artist: ")
        title = input(f'Please enter a song from {artist}: ')
        artist = artist.replace(' ', '%20')
        title = title.replace(' ', '%20')

        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')

        lyrics = response.json()

        if 'lyrics' in lyrics:    
            print(lyrics['lyrics'])
            re_play = input("Would you like to try a different artist and title? y/n? :")
        else:
            print("You either misspelt the artist, the title or you have no taste in music!")
            re_play = input("Would you like to try again? y/n? :")
    
        if re_play.lower() == 'n':
            break

main()