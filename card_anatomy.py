# num = random.randint(0000, 9999)
# account_identifier = random.randint(0, 9)
# check_sum = random.randint(0, 9)
"""
import random

class CardAnatomy:

    def __init__(self):
        self.date_base = {}
        self.user_balance = 0

    def main(self):
        command = int(input("1. Create an account\n2. Log into account\n0. Exit\n"))
        #print(" ")
        return self.check_command(command)

    def check_command(self, command):
        if command == 1:
            return self.create()
        elif command == 2:
            return self.login()

    def create(self):
        random.seed(0)
        user_card = (4000000000000000 + int('{:10d}'.format(random.randrange(0000000000, 9999999999))))
        user_pin_card = '{:04d}'.format(random.randrange(0000, 9999))
        if user_card not in self.date_base:
            self.date_base[user_card] = user_pin_card
            print(f"Your card has been created\nYour card number:\n{user_card}\nEnter your PIN:\n{user_pin_card}")
            #print(" ")
            self.main()
        else:
            self.main()

    def login(self):
        check_card_number = int(input("Enter your card number:\n>"))
        pin_code_check = input("Enter your PIN:\n")
        if self.date_base[check_card_number] == pin_code_check:
            #print(" ")
            print("You have successfully logged in!")
            #print(" ")
            self.card_actions()
        elif self.date_base[check_card_number] == pin_code_check:
            self.main()
        else:
            print("Bye!")


    def card_actions(self):
        select_after_authorization = int(input("1. Balance\n2. Log out\n0. Exit\n"))
        if select_after_authorization == 1:
            print(self.user_balance)
            self.card_actions()
        elif select_after_authorization == 2:
            self.main()
        elif select_after_authorization == 0:
            print("Bye!")



ron = CardAnatomy()
#print(ron.main())



"""

"""


"""









import random


def main_func():
    random.seed(0)

    user_card = int(4000000000000000 + int('{:10d}'.format(random.randrange(0000000000, 9999999999))))
    user_pin_card = '{:04d}'.format(random.randrange(0000, 9999))
    user_balance = 0

    user_data = []


    exit_from_main_cycle = False

    while not exit_from_main_cycle:
        inp_user = int(input("1. Create an account\n2. Log into account\n0. Exit\n"))
        print(" ")

        if inp_user == 1:
            if not user_data:
                print(f"Your card has been created\nYour card number:\n{user_card}\nEnter your PIN:\n{user_pin_card}")
                user_data.append([int(user_card), user_pin_card])
                print(" ")

        elif inp_user == 2:

            if len(user_data) != 0:

                loop_exit_condition = False

                while not loop_exit_condition:
                    check_card_number = int(input("Enter your card number:\n"))
                    pin_code_check = input("Enter your PIN:\n")

                    if check_card_number == user_data[0][0] and pin_code_check == user_data[0][1]:
                        print(" ")
                        print("You have successfully logged in!\n")

                        while not loop_exit_condition:

                            select_after_authorization = int(input("1. Balance\n2. Log out\n0. Exit\n"))
                            print(" ")

                            if select_after_authorization == 1:
                                print(f"Balance: {user_balance}\n")
                                continue
                            elif select_after_authorization == 2:
                                loop_exit_condition = True
                                print("You have successfully logged out!")
                                print(" ")
                            elif select_after_authorization == 0:
                                loop_exit_condition = True
                                exit_from_main_cycle = True

                    else:
                        print("Wrong card number or PIN!")
                        continue
            else:
                continue

        elif inp_user == 0:
            print("Bye!")
            break



if __name__=="__main__":
    print(main_func())