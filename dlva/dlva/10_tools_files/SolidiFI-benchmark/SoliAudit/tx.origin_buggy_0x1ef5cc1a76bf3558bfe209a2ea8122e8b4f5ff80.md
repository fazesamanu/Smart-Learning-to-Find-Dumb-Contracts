# Vulnerability Analysis #
#### 2023-06-05 08:58:02 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 13, 9 ``return usernames[_user]``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 15, 5 ``function checkDupe(string _userName) public constant returns (int) {
        return dedupeList[_userName];
    }``
        - Line 18, 5 ``function createUsername(string _userName) external returns (bool) {
        require(bytes(usernames[msg.sender]).length == 0);
        require(dedupeList[_userName] == 0);
        require(bytes(_userName).length >= 3 && bytes(_userName).length <= 16);
        usernames[msg.sender] = _userName;
        dedupeList[_userName] = 1;
        NewUsername(msg.sender, _userName);
        return true;
    }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 7, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
