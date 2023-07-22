# Program Title: Project 1: One Stop Insurance Company
# Program Description: This program allows users to enter and calculate new insurance policy infomration for its customers.
# Written By: Vanessa Rice
# Written on: July 18, 2023

# Imports/
import datetime
from termcolor import colored


# define functions

def CalMonthlyPayments(TotalCost):
    TotalCost += PROCESSING_FEE
    MonthlyPayments = TotalCost / 8

    return MonthlyPayments

def format_phone_number(phone_number):
    # Remove any non-numeric characters (e.g., spaces, dashes) from the input phone number
    digits = ''.join(filter(str.isdigit, CusPhoneNum))

    # Format the phone number into (XXX) XXX-XXXX using concatenation
    formatted_number = "(" + digits[:3] + ") " + digits[3:6] + "-" + digits[6:]

    return formatted_number

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
    CusFirstName = input("Enter the customer first name (END to quit): ").title()
    if CusFirstName == "End":
        break

    CusLastName = input("Enter the customer's last name: ").title()
    CusStAdd = input("Enter customer's street address: ").title()
    CusCity = input("Enter the city: ").title()

    valid_provinces = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QB", "SK", "YT"]

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
        PaymentMethod = input("Enter payment method(Full or Monthly): ").title()
        if PaymentMethod not in valid_payments:
            print("Error - Payment method is invalid.")
        else:
            break
    print()
# Calculations


    if NumCars == 1:
        Premium = BASIC_PREMIUM
    else:
        AddtCarPremium = (NumCars - 1) * BASIC_PREMIUM
        AddtCarDiscount = AddtCarPremium - (AddtCarPremium * DISCOUNT_RATE_ADDT)
        Premium = BASIC_PREMIUM + AddtCarDiscount
        AddtCarDiscountDsp = "${:,.2f}".format(AddtCarDiscount)

    if OptLiability == "Y":
        OptLiabilityCost = COST_EXTRA_LIABILITY * NumCars
    else:
        OptLiabilityCost = 0
    if GlassCoverage == "Y":
        GlassCoverageCost = COST_GLASS_COVERAGE * NumCars
    else:
        GlassCoverageCost = 0
    if OptLoaner == "Y":
        OptLoanerCost = COST_LOANER_CAR * NumCars
    else:
        OptLoanerCost = 0

    TotalExtra = OptLoanerCost + OptLiabilityCost + GlassCoverageCost

    Subtotal = Premium + TotalExtra

    HSTAmount = Subtotal * HST_RATE

    TotalCost = Subtotal + HSTAmount

    MonthlyPayments = CalMonthlyPayments(TotalCost)


# Get invoice date and next payment dates
    InvoiceDate = datetime.date.today()
    NextPaymentDate = InvoiceDate.replace(day=1, month=InvoiceDate.month + 1)

# formatting
    PremiumDsp = "${:,.2f}".format(Premium)
    OptLiabilityCostDsp = "${:,.2f}".format(OptLiabilityCost)
    GlassCoverageCostDsp = "${:,.2f}".format(GlassCoverageCost)
    OptLoanerCostDsp = "${:,.2f}".format(OptLoanerCost)
    SubtotalDsp = "{:,.2f}".format(Subtotal)
    HSTAmountDsp = "${:,.2f}".format(HSTAmount)
    TotalExtraDsp = "${:,.2f}".format(TotalExtra)
    TotalCostDsp = "${:,.2f}".format(TotalCost)
    MonthlyPaymentsDsp = "${:,.2f}".format(MonthlyPayments)
    CusPhoneNumDsp = format_phone_number(CusPhoneNum)
    Company = "One Stop Insurance Company"
    CustName = CusFirstName + " " + CusLastName

#User outputs

    print("{:^78s}".format(Company))
    print()
    print(colored("╔══════════════════════════ Customer Information ═══════════════════════╗", "yellow"))
    print(colored("║ Name: {:>63s}".format(CustName).ljust(60), "yellow") + " " + "║")
    print(colored("║ Address: {:>60s}".format(CusStAdd).ljust(60), "yellow") + " " + "║")
    print(colored("║ City: {:>63s}".format(CusCity).ljust(60), "yellow") + " " + "║")
    print(colored("║ Province: {:>59s}".format(CusProv).ljust(60), "yellow") + " " + "║")
    print(colored("║ Postal Code: {:>56s}".format(Postal).ljust(60), "yellow") + " " + "║")
    print(colored("║ Phone Number: {:>55s}".format(CusPhoneNumDsp).ljust(60), "yellow") + " " + "║")
    print(colored("║ Policy Number: {:>54d}".format(NEXT_POLICY_NUM).ljust(60), "yellow") + " " + "║")
    print(colored("╚═══════════════════════════════════════════════════════════════════════╝", "yellow"))
    print()
    print(colored("════════════════════════ Insurance Policy Breakdown ═════════════════════", "yellow"))
    print("   Number of Cars on Policy: {:>41d}".format(NumCars))
    if OptLiability == "Y":
        OptLiability = "Yes"
    else:
        OptLiability = "No"
    print("   Extra Liability: {:>50s}".format(OptLiability))
    if GlassCoverage == "Y":
        GlassCoverage = "Yes"
    else:
        GlassCoverage = "No"
    print("   Optional Glass Protection: {:>40s}".format(GlassCoverage))

    if OptLoaner == "Y":
        OptLoaner = "Yes"
    else:
        OptLoaner = "No"

    print("   Optional Loaner Car: {:>46s}".format(OptLoaner))
    print("   Payment Option: {:>51s}".format(PaymentMethod))
    print(colored("═════════════════════════ Policy Cost Breakdown ═════════════════════════", "yellow"))
    print("   Insurance Premium: {:>48s}".format(PremiumDsp))

    if NumCars > 1:
        print("   Discount for Additional Cars: {:>37s}".format(AddtCarDiscountDsp))


    if OptLiability == "Yes":
        print("   Optional Liability Cost: {:>42s}".format(OptLiabilityCostDsp))

    if GlassCoverage == "Yes":
        print("   Optional Glass Coverage Cost: {:>37s}".format(GlassCoverageCostDsp))

    if OptLoaner == "Yes":
        print("   Optional Loaner Car Cost: {:>41s}".format(OptLoanerCostDsp))

    print(colored("═══════════════════════════ Policy Cost Totals ══════════════════════════", "yellow"))
    if OptLiability == "Yes" or GlassCoverage == "Yes" or OptLoaner == "Yes":
        print("   Total Extra Costs: {:>48s}".format(TotalExtraDsp))


    print("   Subtotal: {:>57s}".format(SubtotalDsp))
    print("   HST: {:>62s}".format(HSTAmountDsp))
    print("   Total: {:>60s}".format(TotalCostDsp))

    if PaymentMethod == "Monthly":
        print("   Monthly Payments: {:>49s}".format(MonthlyPaymentsDsp))

    print("═════════════════════════════════════════════════════════════════════════")
    print("   Invoice Date : {}".format(InvoiceDate), "            Next Payment Date: {}".format(NextPaymentDate))



   # Write the values to a file for future reference.
    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POLICY_NUM}, ")
    f.write(f"{InvoiceDate}, ")
    f.write(f"{CusFirstName}, ")
    f.write(f"{CusLastName}, ")
    f.write(f"{CusStAdd}, ")
    f.write(f"{CusCity}, ")
    f.write(f"{CusProv}, ")
    f.write(f"{Postal}, ")
    f.write(f"{CusPhoneNum}, ")
    f.write(f"{NumCars}, ")
    f.write(f"{OptLiability}, ")
    f.write(f"{GlassCoverage}, ")
    f.write(f"{OptLoaner}, ")
    f.write(f"{PaymentMethod}, ")
    f.write(f"{TotalCost}\n")
    f.close()
    print()
    print("Policy information processed and saved...")

# Update any default values based on the processing requirements
    NEXT_POLICY_NUM += 1

# Housekeeping
    f = open('OSICDef.dat', 'w')
    f.write(f"{NEXT_POLICY_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{DISCOUNT_RATE_ADDT}\n")
    f.write(f"{COST_EXTRA_LIABILITY}\n")
    f.write(f"{COST_GLASS_COVERAGE}\n")
    f.write(f"{COST_LOANER_CAR}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESSING_FEE}\n")
    f.close()
    print()