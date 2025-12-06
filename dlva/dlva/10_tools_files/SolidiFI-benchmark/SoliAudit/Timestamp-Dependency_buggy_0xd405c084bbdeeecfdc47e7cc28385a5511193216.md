# Vulnerability Analysis #
#### 2023-06-05 08:34:20 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 72, 5 ``return _name``
        - Line 76, 5 ``return _symbol``

* __O__ Overflow
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

        - Line 115, 17 ``now``
        - Line 116, 34 ``now``
        - Line 117, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
