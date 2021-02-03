def make_album(a_name,s_name,d_date,counts = ''):
    album = {'Album name': a_name,'Singer name': s_name,'Date': d_date}
    if counts:
        album['counts'] = counts
    return album
while True:
    print("\nPlease tell me the album name:")
    print("(Enter 'q' to quit anytime)")

    a_name = input("Album name:")
    if a_name == 'q':
        break

    s_name = input("Singer name:")
    if s_name == 'q':
        break

    d_date = input("Date:")
    if d_date == 'q':
        break

    full_inf = make_album(a_name,s_name,d_date)
    print(full_inf)
