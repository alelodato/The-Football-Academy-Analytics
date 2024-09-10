import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the_football_academy_analytics')

weekly = SHEET.worksheet('weekly')

data = weekly.get_all_values()

print(data)

def get_weekly_revenue():
    """
    Gets the weekly revenue of the 3 teams of the academy
    """

    while True:
        print("Please enter last week revenue for the 3 teams of the academy.")
        print("Enter 3 values, separated by commas.")
        print("Example: 1500, 1700, 2000.")

        data_str = input("Enter your data here:\n")

        weekly_revenue = data_str.split(",")

        if validate_data(weekly_revenue):
            print("Data inserted is valid.")
            break
        return weekly_data
    
    
    
