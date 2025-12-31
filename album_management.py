class album:
    def __init__(self ,album_name ,number_of_songs ,album_artist ):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
    def __repr__(self):
        return repr((self.album_name, self.number_of_songs, self.album_artist))

albums1 = [
    album('counting stars', '12', 'lucy sprag'),
    album('christmas hits', '29', 'multiple artists'),
    album('tangerine skies', '10', 'declan j'),
    album('lighthouse', '11', 'take that'),
    album('workout mix', '18', 'dj x')
]

albums_sorted_song_number = sorted(albums1, key=lambda album: album.number_of_songs)
print(f"the ablums1 list by number of songs is as follows:{albums_sorted_song_number}")
temp = albums_sorted_song_number[0]
albums_sorted_song_number[0] = albums_sorted_song_number[1]
albums_sorted_song_number[1] = temp
print(f"swapping index 0 and 1 of the albums1 list we get:{albums_sorted_song_number}")


albums2 = [
    album('football anthems', '22', 'football dj'),
    album('mediation mix', '21', 'david thorn'),
    album('balance', '15', 'coldplay'),
    album('candy', '23', 'robbie williams'),
    album('red', '33', 'taylor swift')
]

albums2.extend(albums1)
print(f"Combining the list albums1 and 2 we get: {albums2}")

additional_albums = [
    album('dark side of the moon','9', 'pink floyd'),
    album('oops!... i did it again','16', 'britney spears')
]

albums2.extend(additional_albums)
print(f" Combining the two addtional albums to album 2 we get: {albums2}")

albums_sorted_album_name = sorted(albums2, key=lambda album: album.album_name)
print("\n")
print(f"The ablums2 list sorted by album name is as follows:{albums_sorted_album_name}")

for index, a in enumerate(albums_sorted_album_name):
    if a.album_name == 'dark side of the moon':
        print(f" The index of 'dark side of the moon' album is: {index}")
        break