"""
BROWNIE will automatically load, compile and deploy the smart contracts
"""


from brownie import accounts, config, SimpleStorage, network
import os


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def deploy_contract():
    account = get_account()
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
