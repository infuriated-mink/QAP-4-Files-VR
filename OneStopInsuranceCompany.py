# Program Title: Project 1: One Stop Insurance Company
# Program Description: This program allows users to enter and calculate new insurance policy infomration for its customers.
# Written By: Vanessa Rice
# Written on: July 18, 2023

# Imports
import datetime

# define functions
def CalInsurancePremium(NumCars, OptLiability, GlassCoverage, OptLoaner):

    if NumCars == 1:
        Premium = BASIC_PREMIUM
    else:
        AddtCarPremium = (NumCars - 1) * BASIC_PREMIUM
        AddtCarDiscount = AddtCarPremium - (AddtCarPremium * DISCOUNT_RATE_ADDT)
        Premium = BASIC_PREMIUM + AddtCarDiscount

    if OptLiability == "Y":
        Premium += COST_EXTRA_LIABILITY * NumCars
    if GlassCoverage == "Y":
        Premium += COST_GLASS_COVERAGE * NumCars
    if OptLoaner == "Y":
        Premium += COST_LOANER_CAR

    return Premium

def CalTotalCost(InsurancePremium):
    HSTAmount = InsurancePremium * HST_RATE
    TotalCost = InsurancePremium + HSTAmount
    
    return TotalCost

def CalMonthlyPayments(TotalCost):
    TotalCost += PROCESSING_FEE
    MonthlyPayments = TotalCost / 8

    return MonthlyPayments


# Open the defaults file and read the values into variables

f = open('OSICDef.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
DISCOUNT_RATE_ADDT = float(f.readline())
COST_EXTRA_LIABILITY = float(f.readline())
COST_GLASS_COVERAGE = float(f.readline())
COST_LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()



# Main Program
while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
    CusFirstName = input("Enter the customer's first name: ").title()
    if CusFirstName == "":
        print("Error - Customer's first name cannot be blank.")
    elif not set(CusFirstName).issubset(allowed_char):
        print("Error - Customer's first name contains invalid characters.")
    else:
        break
    
while True:
    allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
    CusLastName = input("Enter the customer's last name: ")
    if CusLastName == "":
        print("Error - Customer's last name  cannot be blank.")
    elif not set(CusLastName).issubset(allowed_char):
        print("Error - Customer's last name contains invalid characters.")
    else:
        break

CusStAdd = input("Enter customer's street address: ").title()
CusCity = input("Enter the city: ").title()

valid_provinces = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QB", "SK", "YK"]

while True:
    CusProv = input("Enter the province(XX): ").upper()
    if CusProv not in valid_provinces:
        print("Error - Province is invalid.")
    else:
        break

while True:
    allowed_letters = set("ABCDEFGHIJKLMONPQRSTUVWXYZ")
    allowed_numbers = set("0123456789")
    Postal = input("Enter the postal code (L0L0L0): ").upper()
    if Postal == "":
        print("Error - Postal code cannot be blank.")
    elif len(Postal) != 6:
        print("Error - Postal code must be 6 characters.")
    elif not set(Postal[0]).issubset(allowed_letters):
        print("Error - First character in the postal code must be a letter.")
    elif not set(Postal[2]).issubset(allowed_letters):
        print("Error - Third character in the postal code must be a letter.")
    elif not set(Postal[4]).issubset(allowed_letters):
        print("Error - Fifth character in the postal code must be a letter.")
    elif not set(Postal[1]).issubset(allowed_numbers):
        print("Error - Second character in the postal code must be a number.")
    elif not set(Postal[3]).issubset(allowed_numbers):
        print("Error - Forth character in the postal code must be a number.")
    elif not set(Postal[3]).issubset(allowed_numbers):
        print("Error - Sixth character in the postal code must be a number.")
    else:
        break



while True: 
    CusPhoneNum = input("Enter the phone number (999999999): ")
    if CusPhoneNum == "":
        print("Error - Phone number cannot be blank.")
    elif len(CusPhoneNum) != 10:
        print("Error - Phone number must be 10 digits.")
    elif not CusPhoneNum.isdigit(): 
        print("Error - Phone number must be 10 digits.")
    else:
        break


NumCars = int(input("Enter number of cars being insured: "))
OptLiability = input("Enter Y or N for extra liability up to $1,000,000: ").upper()
GlassCoverage = input("Enter Y or N for glass coverage: ").upper()
OptLoaner = input("Enter Y or N for loaner car: ").upper()

valid_payments = ["Monthly", "Full"]

while True:
    PaymentMethod = input("Enter payment method(Full or Monthy): ").upper()
    if PaymentMethod not in valid_payments:
        print("Error - Province is invalid.")
    else:
        break

# Calculations
InsurancePremium = CalInsurancePremium(NumCars, OptLiability, GlassCoverage, OptLoaner)
TotalCost = CalTotalCost(InsurancePremium)
MonthlyPayments = CalMonthlyPayments(TotalCost)

# Get invoice date and next payment dates
InvoiceDate = datetime.date.today()
NextPaymentDate = InvoiceDate.replace(day=1, month=InvoiceDate.month+1)

# User Outputs
Company = "One Stop Insurance Company"
print("{:>80s}".format(Company))
print()
print(colored("╔══════════════════════════ Customer Information ═══════════════════════╗", "yellow"))
print(colored("║ Name: {} {}".format(first_name, last_name).ljust(60), "yellow") + "║")
print(colored("║ Address: {}".format(address).ljust(60), "yellow") + "║")
print(colored("║ City: {}".format(city).ljust(60), "yellow") + "║")
print(colored("║ Province: {}".format(province).ljust(60), "yellow") + "║")
print(colored("║ Postal Code: {}".format(postal_code).ljust(60), "yellow") + "║")
print(colored("║ Phone Number: {}".format(phone_number).ljust(60), "yellow") + "║")
print(colored("╚════════════════════════════════════════════════════════════════════╝", "yellow"))