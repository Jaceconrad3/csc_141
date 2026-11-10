# Jace Conrad
# Chapter 8
# Dif 4/10
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('honda', 'civic', color='blue', year=2016)
print(car)