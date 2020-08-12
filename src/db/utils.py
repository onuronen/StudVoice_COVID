import pandas as pd
from crud import update_table
from models import Problem

def process_ticket(short_description, description):

    #append data to database for review
    data = {"title": [short_description], 'description': [description], "score": [0], "isChecked": [False] }

    new_df = pd.DataFrame(data)
    update_table(new_df,Problem)


    

 