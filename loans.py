
def loans_available():
    try:
        from loan_data import loans
    except:
        print("No loans found.")
        loansfound = False
    else:
        loansfound = True
    finally:
        if loansfound == True:
            print(f"\nThere are {len(loans)} loans available:")
            for index in range(len(loans)):
                loan_name = loans[index]['name']
                loan_amount = loans[index]['principal']
                loan_interest = loans[index]['interest']
                print(f'{index}  |  {loan_name} \t..\t..\t${loan_amount} @ {loan_interest}%')
            loans_available.yes = True
        else:
            loans = []
            loans_available.yes = False
        loans_available.loans = loans
        return

def add_loan():
    loans = loans_available.loans
    loan_yes_no = input("Would you like to add a loan? [Y/N]")
    options = ('y', 'Y', 'yes', 'Yes')
    if loan_yes_no not in options:
        menu()
    print("Ok, let's add a loan. You will need a loan name, principal (amount owed), and yearly interest rate.")
    input("Press any key to continue when ready.")
    name = input("Loan name:")
    principal = float(input("Principal ($): "))
    interest = float(input("Interest (%): "))

    print(f"\n New Loan \n |  Name: {name}\n |  Principal: ${principal}\n |  Interest: {interest}%")
    add_me = input("Is this correct? [Y/N]")
    if add_me not in options:
        name = input("Loan name:")
        principal = float(input("Principal ($): "))
        interest = float(input("Interest (%): "))
    loan_to_add = {}
    loan_to_add['name'] = name
    loan_to_add['principal'] = principal
    loan_to_add['interest'] = interest

    loans.append(loan_to_add)
    f = open('loan_data.py', 'w')
    # f.write(str(loans))
    f.write(f"loans = {str(loans)}")
    f.close()

    print("Loan added successully.")
    menu()

def modify_loan():
    loans = loans_available.loans
    loan_yes_no = input(f"Which loan would you like to modify? [0-{1-length(loans)}]")
    options = enumerate(loans)
    while True:
        try:
            selection = int(input("Enter the number of the loan you want to modify:"))
        except:
            print("That's not an option")
        else:
            try:
                loan = loans[selection]
            except:
                print("That's not an option")
            else:
                loan = loans[selection]
                name = loan['name']
                principal = loan['principal']
                interest = loan['interest']
                print(f"You have selected {name}\nPrincipal  |  ${principal}\nInterest   |  {interest}%")
                break
            break
    print(f"\n 0 | name\n 1 | principal\n 2 | interest\n")
    while True:
        try: 
            selection = int(input(f"What would you like to modify? [0-2]"))
        except:
            print("That's not an option")
        else:
            try:



def make_payment():
    from decimal import Decimal
    loans_available()
    loans = loans_available.loans
    # if len(loans)<10:
    #     print("No loans to pay off!")
    #     menu()
    while True:
        try:
            selection = int(input("Enter the number of the loan you want to pay off:"))
        except:
            print("That's not an option")
        else:
            try:
                loan = loans[selection]
            except:
                print("That's not an option")
            else:
                loan = loans[selection]
                name = loan['name']
                principal = loan['principal']
                interest = loan['interest']
                monthly_interest = interest/1200
                print(f"You have selected {name}\nPrincipal  |  ${principal}\nInterest   |  {interest}%")
                break
        break
    while True:
        try:
            payment = float(input("Enter payment amount ($):"))
        except:
            print("Error. Enter a payment amount in dollars.")
        else:
            payment = float(payment)
            break
    z=0
    while principal > payment:
        # p = principal
        # i = monthly_interest
        equation = principal*monthly_interest+principal-payment
        y = round(equation, 2)
        print(f"{z} ${y}")
        principal = y
        z=z+1
        if z >= 2400:
            break
    if z >= 2400:
        print("Don't hold your breath, buddy.")
        menu()
    print(f'With a payment of ${payment}\nPaid in {z} months')
    menu()

def exit_app():
    print("See ya.")
    exit()

def menu():
    loans_available()
    menu_options = {1:add_loan, 2:make_payment, 3: exit_app}
    if loans_available.yes==False:
        menu_options[1]()
        return
    print(f"\nWhat would you like to do?")
    for i, j in menu_options.items():
        print (f"{i}  |  {j.__name__}")
    while True:
        try:
            menu = int(input(f"Enter the number of your selection (1-{len(menu_options)}): "))
            if menu not in menu_options:
                raise Exception
        except:
            print("That's not an option.")
        else:
            break
    menu_options[menu]()
    # menu_options.get(menu)

menu()