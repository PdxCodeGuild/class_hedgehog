def main():
    import requests 
    from rich.console import Console
    console = Console()
    track_list ={}
    console.print("[green]Welcome the the lyrical machine! We'll find you're lyrics or won't! Try us to find out[/green]")
    artist = console.input("Please enter an [green]artist[/green]: ")
    title = console.input(f'Please enter a song from [green]{artist}[/green]: ')
    artist = artist.replace(' ', '%20')
    title = title.replace(' ', '%20')
    
    while True:
            
        response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')

        lyrics = response.json()
    
        if 'lyrics' in lyrics:  
            track_list[f"{artist}"] = title  
            print(lyrics['lyrics'])
            re_play = console.input("Would you like to try a different [green]artist[/green] or [green]title[/green] or [red]quit[/red]? :")
        else:
            console.print("You either misspelled the [green]artist[/green], the [green]title[/green] or [bold red]you have no taste in music[bold red]!")
            re_play = input("Would you like to try again? y/n? :")
    
        if re_play.lower() == 'artist':
            artist = console.input('Please enter your new [green]artist[/green]:')
            title = console.input('Please enter your new [green]title[/green]: ')
            track_list[f"{artist}"] = title
            continue
        elif re_play.lower() == 'title':
            title = console.input('Please enter your new [green]title[/green]: ')
            track_list[f"{artist}"] = title
            continue
        elif re_play.lower() == 'y':
            artist = console.input("Please enter an [green]artist[/green]: ")
            title = console.input(f'Please enter a song from [green]{artist}[/green]: ')
            track_list[f"{artist}"] = title
            continue
        elif re_play.lower() == 'n' or 'quit':
            break
    tracklist = console.input("Would you like to print your [green]Track list[/green]? y/n?: ")

    if tracklist == 'y':
        for key, value in track_list.items():
            key = key.replace('%20', ' ')
            value = value.replace('%20', ' ')
            print(key, ':', value)
    else:
        console.print("[bold red]Goodbye![/bold red]")

main()