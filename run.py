import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style


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
    Gets the monthly revenue of the under 8 team of the academy, for the respective 3 tariffs or payment plans.
    """

    while True:
        print("Please enter last month revenue for the under 8 team, including all 3 payment plans.")
        print("Enter 3 values, separated by commas.")
        print("Example: 1500, 1700, 2000.")

        data_str = input("Enter your data here:\n")

        under8_revenue = data_str.split(",")

        if validate_data(under8_revenue):
            print(Fore.GREEN + "Valid data entered." + Fore.RESET)
            break
    return under8_revenue

def get_under11_revenue():
    """
    Gets the monthly revenue of the under 11 team of the academy, for the respective 3 tariffs or payment plans.
    """

    while True:
        print("Please enter last month revenue for the under 11 team, including all 3 payment plans.")
        print("Enter 3 values, separated by commas.")
        print("Example: 1500, 1700, 2000.")

        data_str = input("Enter your data here:\n")

        under11_revenue = data_str.split(",")

        if validate_data(under11_revenue):
            print(Fore.GREEN + "Valid data entered." + Fore.RESET)
            break
    return under11_revenue

def get_under13_revenue():
    """
    Gets the monthly revenue of the under 13 team of the academy, for the respective 3 tariffs or payment plans.
    """

    while True:
        print("Please enter last month revenue for the under 13 team, include all 3 payment plans.")
        print("Enter 3 values, separated by commas.")
        print("Example: 1500, 1700, 2000.")

        data_str = input("Enter your data here:\n")

        under13_revenue = data_str.split(",")

        if validate_data(under13_revenue):
            print(Fore.GREEN + "Valid data entered." + Fore.RESET)
            break
    return under13_revenue

def calculate_total_revenue():
    print("Calculating total monthly revenue...\n")
    under8 = SHEET.worksheet("u8s").get_all_values()
    under8_row = under8[-1]
    under11 = SHEET.worksheet("u11s").get_all_values()
    under11_row = under11[-1]
    under13 = SHEET.worksheet("u13s").get_all_values()
    under13_row = under13[-1]

    total_revenue = []
    for under8, under11, under13 in zip(under8_row, under11_row, under13_row):
        total = int(under8) + int(under11) + int(under13)
        total_revenue.append(total)

    return total_revenue

def calculate_difference():
    print("Calculating difference with last month revenue...\n")
    total_month = SHEET.worksheet("total revenue").get_all_values()
    total_row = total_month[-1]
    previous_month = SHEET.worksheet("previous").get_all_values()
    previous_row = previous_month[-1]

    revenue_difference = []
    for total_month, previous_month in zip(total_row, previous_row):
        difference = int(total_month) - int(previous_month)
        revenue_difference.append(difference)
    return revenue_difference

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
               Fore.RED + f"Exactly 3 values required, you provided {len(values)}, please try again" + Fore.RESET
            )
    except ValueError as e:
            print(Fore.RED + f"Invalid data {e},please try again.\n" + Fore.RESET)
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
    print(Fore.GREEN + f"{worksheet} worksheet updated correctly" + Fore.RESET)

def main():
    """
    Run all program functions
    """
    data = get_under8_revenue()
    under8_revenue = [int(num) for num in data]
    update_worksheet(under8_revenue, "u8s")
    data = get_under11_revenue()
    under11_revenue = [int(num) for num in data]
    update_worksheet(under11_revenue, "u11s")
    data = get_under13_revenue()
    under13_revenue = [int(num) for num in data]
    update_worksheet(under13_revenue, "u13s")
    total_revenue_data = calculate_total_revenue()
    update_worksheet(total_revenue_data, "total revenue")
    revenue_difference_data = calculate_difference()
    update_worksheet(revenue_difference_data, "difference")
    update_worksheet(total_revenue_data, "previous")

print(Fore.WHITE + Back.GREEN + "HI! THIS IS THE FOOTBALL ACADEMY ANALYTICS PROGRAM." + Back.RESET)
main()
print(Fore.WHITE + Back.GREEN + "WORKSHEETS UPDATED CORRECTLY! THANK YOU" + Back.RESET)
