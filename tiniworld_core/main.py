from logic.data import Tiniworld
tini = Tiniworld()

'''
This is the main file to run the project.
It loads the data, trains the models and saves them.
'''

# Does a cross validation for all the models and saves them (each location separately):
tini.cv_and_save_all_models()

# Gives back the number of locations and the names of the locations
# Due to the threshold of at least 2300 data points, some locations are not included
store_dataset = tini.get_stores_ds_alltime()
print("Number of of locations: ", len(store_dataset))
print("Locations available: ", list(store_dataset.keys()) )
