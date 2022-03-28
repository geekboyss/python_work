def city_country(name, country):
    full_name = name + ", " + country
    return full_name.title()

ret = city_country('santiago', 'Chile')

print(ret)
