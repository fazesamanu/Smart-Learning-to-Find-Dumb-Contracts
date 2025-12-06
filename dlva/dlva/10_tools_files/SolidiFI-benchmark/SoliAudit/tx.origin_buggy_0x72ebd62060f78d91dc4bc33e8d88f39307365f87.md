# Vulnerability Analysis #
#### 2023-06-05 08:58:24 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 28, 5 ``string public name``
        - Line 29, 5 ``string public symbol``

* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 45, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, SELFDESTRUCT JUMPDEST PUSH PUSH PUSH

        - Line 142, 9 ``selfdestruct(owner)``

