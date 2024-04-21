"""Database contracts class."""

import os
import json
from value_check import int_positive_check, float_check, date_check


class ContractDatabase:
    """Manages contract records in the database."""

    def __init__(self, file_path):
        """Open an existing .json file or create a new one."""
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def add_contract(self,
                     Client_Name=None,
                     Contract_ID=None,
                     Client_ID=None,
                     Start_Date=None,
                     End_Date=None,
                     Amount=None):
        """
        Add a new contract.

        Parameters:
        - Client_Name - client's name.
        - Contract_ID - contract's ID.
        - Client_ID - client's ID.
        - Start_Date - contract's start date.
        - End_Date - contarct's expiring date.
        - Amount - amount paid by client.

        Creates a new contract in .json file.
        """
        contracts = self._read_contracts()

        if not Client_Name:
            Client_Name = str(input("Enter Client_Name:"))

        if not Contract_ID:
            Contract_ID = input("Enter Contract_ID:")

        if int_positive_check(Contract_ID) is False:
            return False
        else:
            Contract_ID = int(Contract_ID)

        for i in range(len(contracts)):
            if contracts[i].get("Contract_ID") == Contract_ID:
                print(
                    f"Contract with Contract_ID = {Contract_ID}"
                    "already exists."
                    "Can't add new contract."
                    )
                return False

        if not Client_ID:
            Client_ID = input("Enter Client_ID:")

        if int_positive_check(Client_ID) is False:
            return False
        else:
            Client_ID = int(Client_ID)

        if not Start_Date:
            Start_Date = input("Enter Start_Date (dd-mm-yyyy):")

        if date_check(Start_Date) is False:
            return False

        if not End_Date:
            End_Date = input("Enter End_Date (dd-mm-yyyy):")

        if date_check(End_Date) is False:
            return False

        if not Amount:
            Amount = input("Enter Amount:")

        if float_check(Amount) is False:
            return False
        else:
            Amount = int(Amount)

        new_contract = {
            'Client_Name': Client_Name,
            'Contract_ID': Contract_ID,
            'Client_ID': Client_ID,
            'Start_Date': Start_Date,
            'End_Date': End_Date,
            'Amount': Amount
        }
        contracts.append(new_contract)

        self._write_contracts(contracts)

        print("New contract was successfully added.")

        return True

    def delete_contract_by_id(self, Contract_ID=None):
        """
        Delete an existing contract.

        Parameters:
        Contract_ID - contract's ID to delete.

        Deletes an existing contract in .json file by its Contract_ID.
        """
        contracts = self._read_contracts()

        if not Contract_ID:
            Contract_ID = input("Enter Contract_ID to delete:")

        if int_positive_check(Contract_ID) is False:
            return False
        else:
            Contract_ID = int(Contract_ID)

        if len(contracts) == 0:
            print("You have 0 contracts in your database!")
            return False

        for i in range(len(contracts)):
            if contracts[i].get("Contract_ID") == Contract_ID:
                contracts.pop(i)
                print(
                    f"Contract with Contract_ID = {Contract_ID} "
                    "successfully deleted."
                    )
                break
            elif (i+1 == len(contracts)):
                print(f"No contract with Contract_ID = {Contract_ID} found.")
                return False

        self._write_contracts(contracts)

        return True

    def update_contract(self,
                        Contract_ID=None,
                        Client_Name_new=None,
                        Contract_ID_new=None,
                        Client_ID_new=None,
                        Start_Date_new=None,
                        End_Date_new=None,
                        Amount_new=None):
        """
        Update an existing contract.

        Parameters:
        - Contract_ID - contract's ID to update.
        - Client_Name_new - new client's name.
        - Contract_ID_new - new contract's ID.
        - Client_ID_new - new client's ID.
        - Start_Date_new - new contract's start date.
        - End_Date_new - new contract's expiration date.
        - Amount_new - new client's paid amount.

        Updates info of an existing contract in .json file by its Contract_ID.
        """
        contracts = self._read_contracts()

        automated = False
        if not Contract_ID:
            Contract_ID = input("Enter Contract_ID to update:")
        elif (Client_Name_new or Contract_ID_new or
              Client_ID_new or Start_Date_new or End_Date_new or Amount_new):
            automated = True

        if int_positive_check(Contract_ID) is False:
            return False
        else:
            Contract_ID = int(Contract_ID)

        if self.find_contract_by_contract_id(Contract_ID) is False:
            return False

        for i in range(len(contracts)):
            if contracts[i].get('Contract_ID') == Contract_ID:
                updated_contract = contracts[i]
                break

        if automated:
            if Client_Name_new:
                updated_contract['Client_Name'] = Client_Name_new
            if Contract_ID_new:
                if int_positive_check(Contract_ID_new) is False:
                    return False
                else:
                    Contract_ID_new = int(Contract_ID_new)

                for j in range(len(contracts)):
                    if contracts[j].get("Contract_ID") == Contract_ID_new:
                        print(
                            "Can't assign this Contract_ID "
                            "because a contract with this Contract_ID "
                            "already exists."
                            )
                        return False

                updated_contract['Contract_ID'] = Contract_ID_new
            if Client_ID_new:
                if int_positive_check(Client_ID_new) is False:
                    return False
                else:
                    Client_ID_new = int(Client_ID_new)

                updated_contract['Client_ID'] = Client_ID_new
            if Start_Date_new:
                if date_check(Start_Date_new) is False:
                    return False

                updated_contract['Start_Date'] = Start_Date_new
            if End_Date_new:
                if date_check(End_Date_new) is False:
                    return False

                updated_contract['End_Date'] = End_Date_new
            if Amount_new:
                if float_check(Amount_new) is False:
                    return False
                else:
                    Amount_new = int(Amount_new)

                updated_contract['Amount'] = Amount_new

            contracts[i] = updated_contract
        else:
            while (True):
                choice = input(
                            "What do you want to update"
                            "(You can choose more than 1 option):\n\t"
                            "1 - Client_Name \n\t"
                            "2 - Contract_ID \n\t"
                            "3 - Client_iD \n\t"
                            "4 - Start_Date \n\t"
                            "5 - End_Date \n\t"
                            "6 - Amount\n\t"
                            "9 - Nothing else. \n"
                            "Your choice:"
                            )
                if int_positive_check(choice) is False:
                    continue
                else:
                    choice = int(choice)

                if choice == 1:
                    Client_Name_new = input("Enter Client_Name: ")

                    updated_contract['Client_Name'] = Client_Name_new
                elif choice == 2:
                    Contract_ID_new = input("Enter Contract_ID:")

                    if int_positive_check(Contract_ID_new) is False:
                        return False
                    else:
                        Contract_ID_new = int(Contract_ID_new)

                    for j in range(len(contracts)):
                        if contracts[j].get("Contract_ID") == Contract_ID_new:
                            print(
                                "Can't assign this Contract_ID "
                                "because a contract with this Contract_ID "
                                "already exists."
                                )
                            return False

                    updated_contract['Contract_ID'] = Contract_ID_new
                elif choice == 3:
                    Client_ID_new = input("Enter Client_ID:")
                    if int_positive_check(Client_ID_new) is False:
                        return False
                    else:
                        Client_ID_new = int(Client_ID_new)

                    updated_contract['Client_ID'] = Client_ID_new
                elif choice == 4:
                    Start_Date_new = input("Enter Start_Date (dd-mm-yyyy):")
                    if date_check(Start_Date_new) is False:
                        return False

                    updated_contract['Start_Date'] = Start_Date_new
                elif choice == 5:
                    End_Date_new = input("Enter Start_Date (dd-mm-yyyy):")
                    if date_check(End_Date_new) is False:
                        return False

                    updated_contract['Start_Date'] = End_Date_new
                elif choice == 6:
                    Amount_new = input("Enter Amount:")
                    if float_check(Amount_new) is False:
                        return False
                    else:
                        Amount_new = int(Amount_new)

                    updated_contract['Amount'] = Amount_new
                elif choice == 9:
                    contracts[i] = updated_contract
                    break
                else:
                    print(f"No such as option {choice}.")

        self._write_contracts(contracts)
        print(f"Contract (Contract_ID = {Contract_ID}) successfully updated.")

        return True

    def find_contract_by_contract_id(self, Contract_ID=None):
        """
        Find an existing contract by Contract_ID.

        Parameters:
        - Contract_ID - contract's ID to find.

        Finds an existing contract in .json file by its Contract_ID.
        """
        contracts = self._read_contracts()

        if not Contract_ID:
            Contract_ID = input("Enter Contract_ID:")

        if int_positive_check(Contract_ID) is False:
            return False
        else:
            Contract_ID = int(Contract_ID)

        if len(contracts) == 0:
            print("You have 0 contracts in your database!")
            return False

        for i in range(len(contracts)):
            if contracts[i].get("Contract_ID") == Contract_ID:
                print(f"Contract with Contract_ID = {Contract_ID}:")
                print(contracts[i])
                return True
            elif (i+1 == len(contracts)):
                print(f"No contract with Contract_ID = {Contract_ID} found.")
                return False

    def find_contracts_by_client_id(self, Client_ID=None):
        """
        Find an existing contracts by Client_ID.

        Parameters:
        - Client_ID - client's ID to find his contracts.

        Finds some client's existing contracts in .json file by his Client_ID.
        """
        contracts = self._read_contracts()

        if not Client_ID:
            Client_ID = input("Enter Client_ID:")

        if int_positive_check(Client_ID) is False:
            return False
        else:
            Client_ID = int(Client_ID)

        if len(contracts) == 0:
            print("You have 0 contracts in your database!")
            return False

        found_len = 0
        print(f"Contracts with Client_ID = {Client_ID}:")
        for i in range(len(contracts)):
            if contracts[i].get("Client_ID") == Client_ID:
                print(contracts[i])
                found_len += 1
            elif (i+1 == len(contracts)):
                if found_len == 0:
                    print(f"No contracts with Client_ID = {Client_ID} found.")
                    return False

        return True, found_len

    def sort_contracts(self, operation, ascending=None):
        """
        Sort contracts.

        Parameters:
        - operation - sort by [1-3], where:
            - 1 - by Contract_ID.
            - 2 - by Client_ID.
            - 3 - by Amount.
        - ascending - type of sort [1,2], where:
            - 1 - ascending.
            - 2 - descending.

        Sorts contracts from .json file.
        """
        contracts = self._read_contracts()

        if not ascending:
            ascending = input("Enter sort type "
                              "(1 - ascending, 2 - descending):"
                              )

        if int_positive_check(ascending) is False:
            return False
        else:
            ascending = int(ascending)

        if ascending not in [1, 2]:
            print(f"No such as option {ascending}.")
            return False

        if operation not in [1, 2, 3]:
            print(f"No such as operation {operation}.")
            return False

        if operation == 1:
            if ascending == 1:
                for i in range(len(contracts)):
                    for j in range(len(contracts)-i-1):
                        if (
                            contracts[j].get("Contract_ID") >
                            contracts[j+1].get("Contract_ID")
                        ):
                            temp = contracts[j]
                            contracts[j] = contracts[j+1]
                            contracts[j+1] = temp
            else:
                for i in range(len(contracts)):
                    for j in range(len(contracts)-i-1):
                        if (
                            contracts[j].get("Contract_ID") <
                            contracts[j+1].get("Contract_ID")
                        ):
                            temp = contracts[j]
                            contracts[j] = contracts[j+1]
                            contracts[j+1] = temp
        elif operation == 2:
            if ascending == 1:
                for i in range(len(contracts)):
                    for j in range(len(contracts)-i-1):
                        if (
                            contracts[j].get("Client_ID") >
                            contracts[j+1].get("Client_ID")
                        ):
                            temp = contracts[j]
                            contracts[j] = contracts[j+1]
                            contracts[j+1] = temp
            else:
                for i in range(len(contracts)):
                    for j in range(len(contracts)-i-1):
                        if (
                            contracts[j].get("Client_ID") <
                            contracts[j+1].get("Client_ID")
                        ):
                            temp = contracts[j]
                            contracts[j] = contracts[j+1]
                            contracts[j+1] = temp
        elif operation == 3:
            if ascending == 1:
                for i in range(len(contracts)):
                    for j in range(len(contracts)-i-1):
                        if (
                            contracts[j].get("Amount") >
                            contracts[j+1].get("Amount")
                        ):
                            temp = contracts[j]
                            contracts[j] = contracts[j+1]
                            contracts[j+1] = temp
            else:
                for i in range(len(contracts)):
                    for j in range(len(contracts)-i-1):
                        if (
                            contracts[j].get("Amount") <
                            contracts[j+1].get("Amount")
                        ):
                            temp = contracts[j]
                            contracts[j] = contracts[j+1]
                            contracts[j+1] = temp

        for i in range(len(contracts)):
            print(contracts[i])

        return True

    def database_length(self):
        """
        Calculate database's length.

        Printing a count of contracts in .json file.
        """
        contracts = self._read_contracts()
        print(f"Database length - {len(contracts)} contracts.")

        return len(contracts)

    def print_contracts(self, option=None):
        """
        Print contracts from .json file.

        Parameters:
        - option - method of printing the database [1,2], where:
            - 1 - using "for" cycle.
            - 2 - using "file(read())".

        Prints all contracts from .json file.
        """
        contracts = self._read_contracts()
        if len(contracts) == 0:
            print("You have 0 contracts in your database!")
            return False

        if not option:
            option = input(
                        "Choose a method to print your database "
                        "(1 - using cycle \"for\", 2 - using \"file(read())\":"
                        )

        if int_positive_check(option) is False:
            return False
        else:
            option = int(option)

        if option == 1:
            for i in range(len(contracts)):
                print(contracts[i])
        elif option == 2:
            with open(self.file_path, 'r') as file:
                print(file.read())
        else:
            print(f"No such as option {option}.")
            return False

        return True

    def _read_contracts(self):
        """
        Read contracts from .json file.

        Reads all contracts from .json file.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _write_contracts(self, contracts):
        """
        Write contracts to .json file.

        Parameters:
        - contracts - list of contracts.

        Writes updated contracts to .json file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(contracts, file, indent=4)
