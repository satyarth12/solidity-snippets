from brownie import SimpleStorage, accounts

"""
Tests are seperated in 3 categories:
    # Arrange: Will setup all the required pieces
    # Act: Deploy the contract (if not done in arrange) and interact with contract
    # Assert: assert command for results
"""


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    contract = SimpleStorage.deploy({
        "from": account
    })
    starting_value = contract.retreive()
    excepted = 0
    # Assert
    assert starting_value == excepted


def test_update_storage():
    # Arrange
    account = accounts[0]
    contract = SimpleStorage.deploy({
        "from": account
    })
    # Act
    expected = 15
    updated_ = contract.store(15, {"from": account})
    value_ = contract.retreive()
    # Assert
    assert value_ == expected
