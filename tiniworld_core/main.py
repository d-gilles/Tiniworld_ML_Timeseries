from tiniworld_core.logic.data import Tiniworld

tini = Tiniworld()

'''
This is the main file to run the project.
It loads the data, trains the models and saves them.
'''

# 01.12.2022
# Does a cross validation for all the models and saves them (each location separately):
tini.cv_and_save_all_models()

# 02.12.2022
# fit a model for the entire business (all locations together,
# to see the performance and trend of the whole business)
# tini.cv_and_save_all_models(all_over=True)


# Gives back the number of locations and the names of the locations
# Due to the threshold of at least 2300 data points, some locations are not included
store_dataset = tini.get_stores_ds_alltime()
print("Number of of locations: ", len(store_dataset))
print("Locations available: ", store_dataset.keys() )
