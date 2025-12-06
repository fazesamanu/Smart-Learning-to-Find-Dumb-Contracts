# Vulnerability Analysis #
#### 2023-06-05 08:42:31 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 25, 7 ``balances[_to]``
        - Line 36, 13 ``balances[_to]``

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
