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
    
    def validate_data(values):
        """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
            print(f"Invalid data{e},please try again.\n")
            return False

    return True

def update_weekly_worksheet(data, worksheet):
    """
    Receives a list of integers to be imported into the weekly revenue worksheet,
    and updates it with the data provided
    """
    print("Updating weekly revenue worksheet...\n")
    weekly_worksheet = SHEET.worksheet("weekly")
    weekly_worksheet.append_row(data)
    print("Weekly revenue worksheet updated correctly.\n")
    
