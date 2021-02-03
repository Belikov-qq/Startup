magician = ['liqifeng', 'zhangruibing', 'zhangtianyi', 'fuyuhan']
newmagician = []


def make_great(liebiao):
    while liebiao:
        c_magician = liebiao.pop()
        n_magician = "the Great " + str(c_magician)
        newmagician.append(n_magician)


make_great(magician)


def show_magicians(liebiao1,liebiao2):
    for name in liebiao2:
        print(name + " is his name.")
    for name in liebiao1:
        print(name + " has already been changed!")




show_magicians(newmagician,magician[:])
