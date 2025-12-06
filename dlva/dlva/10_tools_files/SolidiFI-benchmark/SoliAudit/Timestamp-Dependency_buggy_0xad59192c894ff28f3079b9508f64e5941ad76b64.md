# Vulnerability Analysis #
#### 2023-06-05 08:22:39 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SHA SLOAD ADD GT JUMPDEST

        - Line 25, 63 ``balances[_to]``
        - Line 35, 99 ``balances[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 56, 17 ``now``
        - Line 57, 34 ``now``
        - Line 58, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
