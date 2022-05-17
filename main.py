import os

# Method Main
if __name__ == '__main__':
    ContinueP = "S"
    print("Welcome to the SSN Validator")  # Welcome Message

    while ContinueP == "S":
        print("Press 'Enter' to continue...")  # Request to press enter after presenting the welcome message.
        stay = True
        WaitP = input()
        if WaitP != "":
            print("Press 'Enter' to continue...")
            ContinueP = "S"
            os.system("cls")
        else:
            print("Digit 9 digits of Social Security Number: ")  # Validations 9 digits
            SSN = input()
            # If SSN is null
            if not SSN:
                ContinueP = "S"
                os.system("cls")
                print("Please, complete the data entry")
            else:
                if SSN.replace('-', '').isnumeric():  # Replace (-) for moment
                    ListDigit = SSN.split('-', 4)
                    if len(ListDigit[0]) == 3:  # Validation for the first group
                        if int(ListDigit[0]) == 000 or int(ListDigit[0]) == 666 or 900 <= int(ListDigit[0]) <= 999:
                            print("The number is invalid")
                        else:
                            if 1 < int(ListDigit[1]) < 99:
                                if 1 < int(ListDigit[2]) < 9999:
                                    print("The SSN " + SSN + " is aa valid social security number")
                                else:
                                    print("The number of digit can't to be diferent that 4 on the last group")
                            else:
                                print("The number of digit can't be diferent that 2 on the second group")
                    else:
                        print("The number of digit can't be diferent that 3 on the first group")
                else:
                    print("Invalid Entry")

            # Validation Last Entry
        while stay:
            print("Do you want to continue on the program? press (S) else press any key")
            ContinueP = input().upper()

            if not ContinueP:
                print("Need to digit any number")
                stay = True
            elif ContinueP.isnumeric():
                stay = True
            else:
                stay = False
