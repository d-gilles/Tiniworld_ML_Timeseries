import pandas as pd
import os
# from colorama import Fore, Style
from tiniworld_core.logic.params import LOCAL_DATA_PATH

# load data from local disk and translate item_name to english
# -----------------------------

def get_data(path: str,
                     columns: list = None,
                     verbose=False) -> pd.DataFrame:
    """
    return the raw dataset from local disk
    """
    path = os.path.join(
        os.path.expanduser(LOCAL_DATA_PATH),
        f"{path}.csv")

    if verbose:
        print("The path is: ", path)
        print(f"Source data from {path}: {'all'} rows ")

    try:
        dtypes = {'docDate': object, 'item_code': object, 'item_name': object, 'qty': int, 'store_code': object, 'store_name': object}
        df = pd.read_csv(
                path,
                dtype=dtypes,
                on_bad_lines='skip')  # read all rows

        if columns is not None:
            df.columns = columns

    except pd.errors.EmptyDataError:

        return None  # end of data


    # VN to EN translation of item_name
    # Happy Day == Members Day (Loyalty program)

    item_name_translation = {
    'Vé cổng phụ huynh đi kèm thu phí': 'Free entrance ticket - accompanied adult',
    'Vé cổng miễn phí ngày thường': 'Free entrance ticket - weekday',
    'Vé cổng miễn phí tiNiPark cuối tuần': 'Free entrance ticket tiNiPark - weekend',
    'Vé cổng ngày thường': 'Entrance ticket - weekday',
    'Vé cổng tiện ích ngày thường': 'Entrance ticket convenience - weekday',
    'Vé cổng miễn phí tiNiPark ngày thường': 'Free entrance ticket tiNiPark - weekday',
    'Vé cổng Happy Day': 'Entrance ticket - Happy Day',
    'Vé cổng tiNiPark ngày thường': 'Entrance ticket tiNiPark - weekday' ,
    'Vé cổng tiện ích tiNiPark cuối tuần': 'Entrance ticket tiNiPark convenience - weekend',
    'TINICARE_Vé cổng phụ huynh đi kèm thu phí': 'TINICARE ticket - accompanied adult',
    'TINICARE_Vé cổng Happy Wednesday': 'TINICARE ticket - Happy Wednesday',
    'Vé cổng tiện ích tiNiPark ngày thường': 'Entrance ticket tiNiPark convenience - weekday',
    'TINICARE_Vé cổng tiện ích ngày thường': 'TINICARE ticket convenience - weekday',
    'TINICARE_Vé cổng ngày thường': 'TINICARE ticket - weekday',
    'TINICARE_Vé cổng Happy Day': 'TINICARE ticket - Happy Day',
    'Vé cổng Happy Day tiNiPark': 'Entrance ticket tiNiPark - Happy Day',
    'TINICARE_Vé cổng tiện ích cuối tuần': 'TINICARE ticket convenience - weekend',
    'Vé cổng miễn phí cuối tuần, lễ tết': 'Free Entrance ticket - weekend/holiday',
    'Vé cổng tiện ích cuối tuần, lễ tết': 'Entrance ticket convenience - weekend/holiday',
    'Vé cổng cuối tuần, ngày lễ': 'Entrance ticket - weekend/holiday',
    'Vé cổng tiNiPark cuối tuần, ngày lễ': 'Entrance ticket tiNiPark - weekend/holiday',
    'Vé cổng tiNiWorld plus': 'Entrance ticket tiNiWorld plus',
    'Vé cổng tiNiWorld cơ bản': 'Entrance ticket tiNiWorld standard',
    'Vé cổng tiNiWorld premium': 'Entrance ticket tiNiWorld premium',
    '"Vé cổng trẻ em dưới 75cm cuối tuần, ngày lễ"': 'Entrance ticket kids < 75cm - weekend/holiday',
    'Vé cổng trẻ em dưới 75cm ngày thường': 'Entrance ticket kids < 75cm - weekday',
    'Vé cổng Happy Day cho bé dưới 75cm': 'Entrance ticket kids < 75cm - Happy Day',
    'Vé cổng trẻ em dưới 75cm cuối tuần, ngày lễ': 'Entrance ticket kids < 75cm - weekend/holiday',
    'Vé cổng tiNi Festival': 'Entrance ticket tiNi Festival'
    }
    def en_translation(value):
        return item_name_translation[value]

    df['item_name_en'] =  df['item_name'].map(en_translation)

    # divides the tickets in adults and kids
    df['Result']=df['item_name_en'].str.contains('adult', regex=False)
    df['Adults']= df['qty']* df['Result']
    df['Kids'] = (df['Result'] == False)* df['qty']

    return df



# Get location Data
def get_location_data_(path: str,
                     columns: list = None,
                     verbose=False) -> pd.DataFrame:
    """
    return the raw dataset from local disk
    """
    path = os.path.join(
        os.path.expanduser(LOCAL_DATA_PATH),
        f"{path}.csv")

    print (path)

    if verbose:
        print("The path is: ", path)
        print(f"Source data from {path}: {'all'} rows ")

    try:
        #dtypes = {'docDate': object, 'item_code': object, 'item_name': object, 'qty': int, 'store_code': object, 'store_name': object}
        df = pd.read_csv(
                path,
                dtype=None)  # read all rows

        if columns is not None:
            df.columns = columns

    except pd.errors.EmptyDataError:

        return None  # end of data

    return df

if __name__ == '__main__':
    print('Nothing to do here. Follow the instructions in the README.md file.')
