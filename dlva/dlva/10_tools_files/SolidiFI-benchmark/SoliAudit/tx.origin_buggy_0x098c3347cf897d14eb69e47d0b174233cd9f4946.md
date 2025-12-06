# Vulnerability Analysis #
#### 2023-06-05 08:41:41 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 14, 8 ``return datas[_id].company``
        - Line 17, 8 ``return datas[_id].valid_date``

* _`X`_ Overflow
    - 100%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 9, 5 ``function save(uint256 _id, string _company, string _valid_date) public{
        datas[_id].company = _company;
        datas[_id].valid_date = _valid_date;
    }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 20, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
