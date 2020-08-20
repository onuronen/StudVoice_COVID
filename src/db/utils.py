import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
#from src.db.crud import update_table,fetch_rows
#from src.db.models import Problem

def process_ticket(short_description, description):

    #append data to database for review
    data = {"title": [short_description], 'description': [description]}

    new_df = pd.DataFrame(data)
    update_table(new_df,Problem)


def extract_unchecked_tickets():
    #extract unchecked tickets and save in a csv file for review.
    df = fetch_rows(Problem)

    if df.empty:
        return
    
    df = df.loc[df['isChecked'] == False]
    df.to_csv('unchecked_problems.csv', index=False)


def import_updated_tickets(csv_file):
    df = pd.read_csv(csv_file)
    update_table(df,Approved_Problem)

 