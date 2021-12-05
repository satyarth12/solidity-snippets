"""
Function here will read directly from network(eg: rinkeby, mainnet) blockchain and
read values from contract that are already deployed on it.
"""
from brownie import SimpleStorage, accounts, config


def read_contract():
    # brownie knows the abi and address of the contract (in deployments folder)
    # so we won't be needing to manually set that

    contract = SimpleStorage[-1]

    print(contract)
    print(contract.retreive())


def main():
    read_contract()
