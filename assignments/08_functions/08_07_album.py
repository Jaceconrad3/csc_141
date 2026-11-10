# Jace Conrad
# Chapter 8
# dif 4/10
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs is not None:
        album['songs'] = songs
    return album
album_1 = make_album(' playboi carti', ' die lit')
album_2 = make_album('travis scott', ' Rodeo')
album_3 = make_album('meek mill',' championships',)

print(album_1)
print(album_2)
print(album_3)

album_4 = make_album('drake', 'take care', 12)
print(album_4)