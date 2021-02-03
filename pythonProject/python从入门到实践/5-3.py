alien_color = "black"
if alien_color == "black":
    print("Conguatulation!,you've got 5 points!")


if alien_color == "black":
    print("You've got 5 points for killing the alien!")
else:
    print("You've got 10 points!")

old_users = ["liqifeng","zty","zzz","lll"]
new_users = ["zzz","lll","lzlz"]
for name in new_users:
    if name in old_users:
        print("Sorry,your name is not available!")
    else:
        print("You could use this name!")