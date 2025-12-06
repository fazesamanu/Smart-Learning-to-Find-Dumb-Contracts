# Vulnerability Analysis #
#### 2023-06-05 09:01:22 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 25, 9 ``balances[_to]``
        - Line 36, 9 ``balances[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 52, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
