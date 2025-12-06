# Vulnerability Analysis #
#### 2023-06-05 08:26:42 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SWAP POP POP JUMP PUSHDEPLOYADDRESS

        - Line 89, 5 ``function allowance(address _owner, address _spender) constant returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 95, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 94, 16 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
