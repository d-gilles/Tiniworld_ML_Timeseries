"""
tiniworld model package params
load and validate the environment variables in the `.env`
"""
import os

LOCAL_DATA_PATH='raw_data'
LOCAL_MODEL_PATH='model'
THRESHOLD = os.environ.get('THRESHOLD', 3500)
