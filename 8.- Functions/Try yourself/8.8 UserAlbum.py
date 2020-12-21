def make_album(artist_name, album_name):
    ''' Almacena un diccionario con el artista y album '''
    albums = {'artist': artist_name.title(), 'album': album_name.title()}

    return albums

while True:
    print("\nIngrese un nombre de artista y album, "
            " o ingrese 'q' para salir del sistema")

    art_name = input("Ingresa nombre del artista: ")
    
    if art_name.lower() == 'q':
        break

    album_name = input("Ingresa nombre del album: ")

    if album_name.lower() == 'q':
        break

    album = make_album(artist_name = art_name, album_name = album_name)

    print (f"\n{album}")


