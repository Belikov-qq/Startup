def city_country(city,country):
    f_name = city + ' ' + country
    return f_name.title()
while True:
    print("\nPlease tell me the city name:")
    print("(Enter 'q' to quit.)")

    ci_name = input("City name:")
    if ci_name == 'q':
        break

    co_name = input("Country name:")
    if co_name == 'q':
        break

    full_name = city_country(ci_name,co_name)
    print("\nHello," + full_name + "!")