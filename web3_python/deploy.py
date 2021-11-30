from solcx import compile_standard, install_solc
import json

with open('../contracts/SimpleStorage.sol') as file:
    simple_storage_file = file.read()

install_solc("0.6.0")

contract_name = "SimpleStorage.sol"

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
abi = compiled_sol.get("contracts").get(
    contract_name).get(contract_name.split(".")[0]).get("abi")


'''
Storing the Contract Address and Abi into a json file
'''
file_name = contract_name.split(".")[0] + "_abis" + ".json"
with open("../abi/" + file_name, "w") as outfile:
    json.dump(abi, outfile, indent=4)
