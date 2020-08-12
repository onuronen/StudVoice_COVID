import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.db.models import Problem
from src.db.crud import update_table

def process_ticket(short_description, description):

    #append data to database for review
    data = {"title": [short_description], 'description': [description], "score": [0], "isChecked": [False] }

    new_df = pd.DataFrame(data)
    update_table(new_df,Problem)


    

 