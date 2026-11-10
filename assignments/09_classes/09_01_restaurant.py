class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, location, price_range):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.price_range = price_range 

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name},")
        print(f"the price is ${self.price_range},")

    def can_you_take_a_date(self):
        if self.price_range < 50:
            print("You can't take a gold digger on this date!")
        else:
            print("You can take a gold digger on this date!")


jace_restaurant = Restaurant("Wingstop", "Chicken Wings", "Reading", 20)
jace_restaurant.can_you_take_a_date()