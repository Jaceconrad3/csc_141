# Jace Conrad
# Chapter 8
# dif 3/10
def make_sandwich(*items):
    print("\nMaking my favorite sandwiches with the following ingredients:")
    for item in items:
        print(f"- {item}")

make_sandwich('salami', 'pepperoni', 'provolone', 'lettuce', 'tomato', 'oil and vinegar')

make_sandwich('peanut butter', 'jelly')

make_sandwich('bacon', 'lettuce', 'tomato', 'mayo')