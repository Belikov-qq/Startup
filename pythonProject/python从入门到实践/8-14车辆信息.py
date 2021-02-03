def make_car(brand,id,size,**car_info):
    info = {}
    info['Car brand'] = brand
    info['Car ID'] = id
    info['car size'] = size
    for key, value in car_info.items():
        info[key] = value
    return info
car_infomation = make_car('audi','Q7','2.5',car_color = 'blue',car_weight = '1.4t')
print(car_infomation)