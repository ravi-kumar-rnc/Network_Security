import os 
import sys
import json

from dotenv import load_dotenv

import certifi
import pandas as pd
import numpy as np
import pymongo


from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class networkdataextract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    if __name__ == '__main__':
        pass
        

            