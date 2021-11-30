from solcx import compile_standard, install_solc
import json
from web3 import Web3

import os
from dotenv import load_dotenv

load_dotenv()


def compile(contract):
    contract_name = contract

    with open("../contracts/" + contract_name) as file:
        simple_storage_file = file.read()

    install_solc("0.6.0")
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {contract_name: {
                "content": simple_storage_file
            }},
            "settings": {
                "outputSelection": {
                    "*": {
                        "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                    }}
            },
        },
        solc_version="0.6.0"

    )

    # print(compile_standard)
    content_var = compiled_sol.get("contracts").get(
        contract_name).get(contract_name.split(".")[0])

    abi = content_var.get("abi")
    bytecode = content_var.get("evm")["bytecode"]["object"]

    '''
    Storing the Contract Address and Abi into a json file
    '''
    # file_name = contract_name.split(".")[0] + "compiled" + ".json"
    # with open("../compiled_code/" + file_name, "w") as outfile:
    #     json.dump(compiled_sol, outfile, indent=4)

    return abi, bytecode


# compile(contract_name="SimpleStorage.sol")

def deploy_contract(abi_, bytecode_):
    """Connection with ganache and deploying on it
    """

    ganache_url = "HTTP://127.0.0.1:7545"
    web3_ = Web3(Web3.HTTPProvider(ganache_url))
    print(web3_.isConnected())

    chain_id = 1337
    address = os.getenv("ADDRESS")
    private_key = os.getenv("PRIVATE_KEY")

    contract_object = web3_.eth.contract(abi=abi_, bytecode=bytecode_)

    # Get the latest transaction on blockchain for nonce
    nonce = web3_.eth.get_transaction_count(address)

    # Building the transaction
    txn_build = contract_object.constructor().buildTransaction({
        'from': address,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3_.toWei('50', 'gwei')
    })

    # Signing the txn_build
    signed_txn = web3_.eth.account.sign_transaction(txn_build, private_key)

    # Send the signed txn to blockchain
    txn_hash = web3_.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Txn receipt of the deployed contract
    txn_receipt = web3_.eth.wait_for_transaction_receipt(txn_hash)
    print("Contract Deployed At:", txn_receipt['contractAddress'])


abi, bytecode = compile(contract="SimpleStorage.sol")
deploy_contract(abi_=abi, bytecode_=bytecode)
