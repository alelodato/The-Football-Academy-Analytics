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

u8s = SHEET.worksheet('u8s')

data = u8s.get_all_values()

def get_under8_revenue():
    """
    Gets the monthly revenue of the under 8 team of the academy, for the respective 3 tariffs and payment plans.
    """

    while True:
        print("Please enter last month revenue for the under 8 team, include all 3 packs.")
        print("Enter 3 values, separated by commas.")
        print("Example: 1500, 1700, 2000.")

        data_str = input("Enter your data here:\n")

        weekly_revenue = data_str.split(",")

        if validate_data(under8_revenue):
            print("Data inserted is valid.")
            break
    return under8_revenue

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

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be imported into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated correctly")

def main():
    """
    Run all program functions
    """
    u8_data = get_under8_revenue()
    under8_revenue = [int(num) for num in data]
    update_worksheet(under8_revenue, "u8s")
    u11_data = get_under11_revenue()
    under11_revenue = [int(num) for num in data]
    update_worksheet(under11_revenue, "u11s")
    u13_data = get_under13_revenue()
    under13_revenue = [int(num) for num in data]
    update_worksheet(under13_revenue, "u13s")

print("Hi! This is the Football Academy Analytics Program.")
main()
