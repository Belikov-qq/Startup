def make_album(name,singer,date,counts = ''):
    album = {'Album name': name,'Date':date}
    if counts:
        album['counts'] = counts
    return album
album_inf = make_album('七里香','Jay Chou','2004',counts=10)
print(album_inf)
album_inf = make_album('叶惠美','Jay Chou','2003')
print(album_inf)
