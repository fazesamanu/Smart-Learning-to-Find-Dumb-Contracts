# Vulnerability Analysis #
#### 2023-06-05 08:28:29 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 51, 13 ``balances[_to]``
        - Line 67, 13 ``balances[_to]``
        - Line 91, 9 ``_totalBurned``
        - Line 101, 9 ``_totalBurned``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
