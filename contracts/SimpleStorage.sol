// SPDX-License-Indentifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    
    // this will get initialized to zero
    uint256 favoriteNumber;
    
    string public contractName;
    
    struct People {
        uint256 favoriteNumber;
        string name;
    }
    
    People[] public person;
    mapping(string => uint256) public nameToFaveNumber;
    
    constructor () public {
        contractName = "Simple Storage Contract";
    }
    
    function store(uint256 _favoriteNumber) public {
        
        favoriteNumber = _favoriteNumber;
    }
    
    // view reads the state of the blockchain
    // hence read doesn't need txn
    function retreive() public view returns(uint256){
        return favoriteNumber;
    }
    
    
    function addPerson(uint256 _favoriteNumber, string memory _name) public{
        person.push(
            People(
                _favoriteNumber,
                _name
            ));
        
        nameToFaveNumber[_name] = _favoriteNumber;
    }
        
   
}