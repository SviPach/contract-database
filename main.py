"""Contract records."""

from class_ES import ContractDatabase
import value_check


DATABASE_FILE = 'company_database.json'


db = ContractDatabase(DATABASE_FILE)

while (True):

    option = input("Choose an option (15 - for help, 99 - to exit): ")

    if value_check.int_positive_check(option) is False:
        continue
    else:
        option = int(option)

    if option == 15:
        print(
            "\t1 - Database length. \n\t"
            "2 - Print contracts from database. \n\t"
            "3 - Find contract by Contract_ID. \n\t"
            "4 - Find contracts by Client_ID. \n\t"
            "5 - Add new contract. \n\t"
            "6 - Delete contract by Contract_ID. \n\t"
            "7 - Update contract by Contract_ID. \n\t"
            "8 - Sort contracts by Contract_ID. \n\t"
            "9 - Sort contracts by Client_ID. \n\t"
            "10 - Sort contracts by Amount. \n\n\t"
            "15 - Help. \n\t"
            "99 - Exit.")
    elif option == 1:
        print("--------------------------------------------------------------")
        db.database_length()
        print("--------------------------------------------------------------")
    elif option == 2:
        print("--------------------------------------------------------------")
        db.print_contracts()
        print("--------------------------------------------------------------")
    elif option == 3:
        print("--------------------------------------------------------------")
        db.find_contract_by_contract_id()
        print("--------------------------------------------------------------")
    elif option == 4:
        print("--------------------------------------------------------------")
        db.find_contracts_by_client_id()
        print("--------------------------------------------------------------")
    elif option == 5:
        print("--------------------------------------------------------------")
        db.add_contract()
        print("--------------------------------------------------------------")
    elif option == 6:
        print("--------------------------------------------------------------")
        db.delete_contract_by_id()
        print("--------------------------------------------------------------")
    elif option == 7:
        print("--------------------------------------------------------------")
        db.update_contract()
        print("--------------------------------------------------------------")
    elif option == 8:
        print("--------------------------------------------------------------")
        db.sort_contracts(1)
        print("--------------------------------------------------------------")
    elif option == 9:
        print("--------------------------------------------------------------")
        db.sort_contracts(2)
        print("--------------------------------------------------------------")
    elif option == 10:
        print("--------------------------------------------------------------")
        db.sort_contracts(3)
        print("--------------------------------------------------------------")
    elif option == 99:
        break
    else:
        print(f"No such as option {option}.")
