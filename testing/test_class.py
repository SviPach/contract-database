"""Class test."""
from class_ES import ContractDatabase


TEST_DATABASE_FILE = 'testing/test_company_database.json'
db = ContractDatabase(TEST_DATABASE_FILE)


def test_add_contract():
    """Test function arr_contract()."""
    assert db.add_contract("Test Client 1", "123", "456",
                           "01-01-2020", "01-01-2022", "1000") is True
    assert db.add_contract(Client_Name="Test Client 2", Contract_ID="124",
                           Client_ID="456", Start_Date="01-01-2020",
                           End_Date="01-01-2022", Amount="1000") is True
    assert db.add_contract("Test Client 3", "123", "789",
                           "01-01-2020", "01-01-2022", "1000") is False

    assert db.add_contract("Test Client 4", "ten", "789",
                           "01-01-2020", "01-01-2022", "1000") is False
    assert db.add_contract("Test Client 4", "-10", "789",
                           "01-01-2020", "01-01-2022", "1000") is False
    assert db.add_contract("Test Client 5", "123", "zero",
                           "01-01-2020", "01-01-2022", "1000") is False
    assert db.add_contract("Test Client 5", "123", "-10",
                           "01-01-2020", "01-01-2022", "1000") is False
    assert db.add_contract("Test Client 6", "123", "789",
                           "01-01-2020", "01-01-2022", "zero") is False
    assert db.add_contract("Test Client 6", "123", "789",
                           "01-01-2020", "01-01-2022", "-10") is False

    assert db.add_contract("Test Client 7", "123", "789",
                           "32-01-2020", "01-01-2022", "1000") is False
    assert db.add_contract("Test Client 8", "123", "789",
                           "01-01-2020", "32-01-2022", "1000") is False


def test_delete_contract_by_id():
    """Test function delete_contract_by_id()."""
    assert db.delete_contract_by_id("123") is True
    assert db.delete_contract_by_id("124") is True
    assert db.delete_contract_by_id("2222") is False
    assert db.delete_contract_by_id("s") is False


def test_update_contract():
    """Test function update_contract()."""
    db.add_contract("Test Client 1", "111", "456",
                    "01-01-2020", "01-01-2022", "1000")
    db.add_contract("Test Client 2", "222", "456",
                    "01-01-2020", "01-01-2022", "1000")

    assert db.update_contract(Contract_ID="111",
                              Client_Name_new="abc") is True
    assert db.update_contract(Contract_ID="111",
                              Contract_ID_new="112") is True
    assert db.update_contract(Contract_ID="112",
                              Client_ID_new="457") is True
    assert db.update_contract(Contract_ID="112",
                              Start_Date_new="02-01-2020") is True
    assert db.update_contract(Contract_ID="112",
                              End_Date_new="02-01-2022") is True
    assert db.update_contract(Contract_ID="112",
                              Amount_new="555") is True

    assert db.update_contract(Contract_ID="112",
                              Contract_ID_new="222") is False

    assert db.update_contract(Contract_ID="0",
                              Client_Name_new="abc") is False
    assert db.update_contract(Contract_ID="12",
                              Client_Name_new="abc") is False
    assert db.update_contract(Contract_ID="zero",
                              Client_Name_new="abc") is False

    assert db.update_contract(Contract_ID="112",
                              Contract_ID_new="ten") is False
    assert db.update_contract(Contract_ID="112",
                              Contract_ID_new="-1") is False

    assert db.update_contract(Contract_ID="112",
                              Client_ID_new="ten") is False
    assert db.update_contract(Contract_ID="112",
                              Client_ID_new="-1") is False

    assert db.update_contract(Contract_ID="112",
                              Start_Date_new="32-01-2020") is False
    assert db.update_contract(Contract_ID="112",
                              Start_Date_new="2020-01-32") is False

    db.delete_contract_by_id("112")
    db.delete_contract_by_id("222")


def test_find_contract_by_contract_id():
    """Test function find_contract_by_contract_id()."""
    db.add_contract("Test Client", "123", "456",
                    "01-01-2020", "01-01-2022", "1000")

    assert db.find_contract_by_contract_id("123") is True
    assert db.find_contract_by_contract_id("111") is False

    db.delete_contract_by_id("123")


def test_find_contracts_by_client_id():
    """Test function find_contracts_by_client_id()."""
    db.add_contract("Test Client 1", "123", "555",
                    "01-01-2020", "01-01-2022", "1000")
    db.add_contract("Test Client 1", "456", "555",
                    "01-01-2020", "01-01-2022", "1000")
    db.add_contract("Test Client 2", "789", "444",
                    "01-01-2020", "01-01-2022", "1000")

    assert db.find_contracts_by_client_id("555") == (True, 2)
    assert db.find_contracts_by_client_id("444") == (True, 1)

    assert db.find_contracts_by_client_id("333") is False

    db.delete_contract_by_id("123")
    db.delete_contract_by_id("456")
    db.delete_contract_by_id("789")


def test_sort_contracts():
    """Test function sort_contracts()."""
    db.add_contract("Test Client 1", "1", "2",
                    "01-01-2020", "01-01-2022", "3")
    db.add_contract("Test Client 2", "2", "3",
                    "01-01-2020", "01-01-2022", "4")
    db.add_contract("Test Client 3", "3", "4",
                    "01-01-2020", "01-01-2022", "1")
    db.add_contract("Test Client 4", "4", "1",
                    "01-01-2020", "01-01-2022", "2")

    assert db.sort_contracts(operation=1, ascending="1") is True
    assert db.sort_contracts(1, "2") is True
    assert db.sort_contracts(2, "1") is True
    assert db.sort_contracts(2, "2") is True
    assert db.sort_contracts(3, "1") is True
    assert db.sort_contracts(3, "2") is True

    assert db.sort_contracts(3, "-1") is False
    assert db.sort_contracts(3, "one") is False
    assert db.sort_contracts(3, "3") is False

    assert db.sort_contracts(4, "1") is False
    assert db.sort_contracts("3", "1") is False

    db.delete_contract_by_id("1")
    db.delete_contract_by_id("2")
    db.delete_contract_by_id("3")
    db.delete_contract_by_id("4")


def test_database_length():
    """Test function database_length()."""
    db.add_contract("Test Client 1", "1", "1",
                    "01-01-2020", "01-01-2022", "100")
    db.add_contract("Test Client 2", "2", "2",
                    "01-01-2020", "01-01-2022", "100")
    db.add_contract("Test Client 3", "3", "3",
                    "01-01-2020", "01-01-2022", "100")

    assert db.database_length() == 3
    assert db.database_length() != 4

    db.delete_contract_by_id("1")
    db.delete_contract_by_id("2")
    db.delete_contract_by_id("3")

    assert db.database_length() == 0


def test_print_contracts():
    """Test function print_contracts()."""
    db.add_contract("Test Client 1", "1", "1",
                    "01-01-2020", "01-01-2022", "100")
    db.add_contract("Test Client 2", "2", "2",
                    "01-01-2020", "01-01-2022", "100")

    assert db.print_contracts(1) is True
    assert db.print_contracts(2) is True

    assert db.print_contracts(3) is False

    db.delete_contract_by_id("1")
    db.delete_contract_by_id("2")

    assert db.print_contracts(1) is False
    assert db.print_contracts(2) is False
