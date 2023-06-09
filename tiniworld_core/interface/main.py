from colorama import Fore, Style
from tiniworld_core.data_sources.local_disk import get_data
from tiniworld_core.logic.data import Tiniworld

def preprocess():
    """
    Preprocess the dataset by chunks fitting in memory.
    parameters:
    - source_type: 'train' or 'val'
    """

    print("\n⭐️ Use case: preprocess")

    data_ = get_data("ticket-sales")

    # print message if data is none
    if data_ is None:
        print(Fore.BLUE + "\nNo data in latest chunk..." + Style.RESET_ALL)

    print("Shape of the data frame: ", data_.shape)

    return None

# KHD: 06.12.2022
def train_single_store():
    tini = Tiniworld()
    tini.cv_and_save_all_models(all_over=False)

def train_consolidated_stores():
    tini = Tiniworld()
    tini.cv_and_save_all_models(all_over=True)

if __name__ == '__main__':
    preprocess() #test get data
