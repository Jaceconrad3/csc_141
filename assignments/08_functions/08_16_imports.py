# Jace Conrad
# Chapter 8
# Dif 6/10 files aren't working. Code is working though. 
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['basketball', 'jordans', 'football gloves']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# This is the code from python to import modules and functions from other files.
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *