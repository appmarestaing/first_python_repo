restaurants = []

def get_restaurant():
    answer = input("give me a restaurant")
    return answer

# function that runs the program
def add_restaurants(allow_repeats):
    new_restaurant = get_restaurant()

    while new_restaurant != "stop":
        if allow_repeats == False and new_restaurant in restaurants:
            print('pick different restaurant')
        else:
            restaurants.append(new_restaurant)
        new_restaurant = get_restaurant()

add_restaurants(False)
print(restaurants)
