# Vulnerability Analysis #
#### 2023-06-05 08:47:49 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SHA SLOAD ADD GT JUMPDEST

        - Line 40, 18 ``balances[_to]``
        - Line 57, 17 ``balances[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
