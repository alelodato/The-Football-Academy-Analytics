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
    return weekly_revenue

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
        print(f"Invalid data {e},please try again.\n")
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

def get_last_4_weekly_entries():
    """
    Collects columns of data from weekly worksheet, collecting
    the last 4 entries for each team, so that the monthly total revenue is calulated and updated, then returns the data
    as a list of lists.
    """
    weekly = SHEET.worksheet("weekly")
    
    columns = []
    for ind in range(0, 5):
        column = weekly.col_values(ind)
        columns.append(column[-4:])
    return columns

def calculate_monthly_revenue(weekly_row):
    print("Updating monthly total revenue...\n")




def update_monthly_worksheet(data, worksheet):
    
    monthly_worksheet = SHEET.worksheet("monthly")
    monthly_worksheet

def main():
    """
    Run all program functions
    """
    data = get_weekly_revenue()
    weekly_revenue = [int(num) for num in data]
    update_weekly_worksheet(weekly_revenue, "weekly")
    month_revenue = get_last_4_weekly_entries()

print("Hi! This is the Football Academy Analytics Program.")
main()
