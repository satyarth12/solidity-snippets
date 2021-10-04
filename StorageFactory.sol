// SPDX-License-Indentifier: MIT

/**
 * @title Storage Factory
 * This file will allow users to deploy their own SimpleStorage contract with their own lists.
 * Eventually StorageFactory will deploy SimpleStorage and interact with it.
 */

pragma solidity >=0.6.0 <0.9.0;

import "./SimpleStorage.sol";

// adding "is" will allow StorageFactory to inherit all the funcs of SimpleStorage
contract StorageFactory is SimpleStorage{
    
    SimpleStorage[] public simpleStorageArray;
    
    function createSimpleStorageContract() public {
        
        // creating object of SimpleStorage contract
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }
    
    /**
     * @dev sfStore value in store() of SimpleStorage.
     * @param _simpleStorageIndex index value of simpleStorageArray which has to be called.
     * @param _simpleStorageNumber value to call on the Store() of simpleStorage contract.
     */
    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber) public {
        
        SimpleStorage stContract = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        stContract.store(_simpleStorageNumber);
    }
    
    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256) {
        return SimpleStorage(address(simpleStorageArray[_simpleStorageIndex])).retreive();
        
    }
} 