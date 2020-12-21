def make_album(artist_name, album_name, number_songs = None):

    albums = {'artist': artist_name.title(), 'album': album_name.title()}

    if number_songs:
        albums['qty_songs'] = number_songs

    return albums

album1 = make_album(artist_name = 'metallica', album_name = 'metallica')
album2 = make_album(artist_name = 'red hot chilli peppers', album_name = 'californication')
album3 = make_album(artist_name = 'r.e.m', album_name = 'out of time', number_songs = 9)
album4 = make_album(artist_name = 'the police', album_name = 'greatest hits', number_songs= 12)

print (f"{album1}\n{album2}\n{album3}\n{album4}\n")


