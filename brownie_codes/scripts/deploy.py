"""
BROWNIE will automatically load, compile and deploy the smart contracts
"""

"""
BROWNIE CMD COMMANDS:
brownie accounts new "account-name"
brownie accounts list
brownie accounts delete "accounts-name"
brownie run scripts/deploy.py
"""




from brownie import accounts, config, SimpleStorage
import os
def deploy_contract():
    account = accounts[0]
    # account = accounts.load("satyarth-account")
    # account = accounts.add(config["wallets"]["from_key"])

    contract = SimpleStorage.deploy({
        "from": account
    })
    # print(contract)

    transaction = contract.store(15, {"from": account})
    stored_value = contract.retreive()
    print(stored_value)


def main():
    print("HELLO")
    deploy_contract()
