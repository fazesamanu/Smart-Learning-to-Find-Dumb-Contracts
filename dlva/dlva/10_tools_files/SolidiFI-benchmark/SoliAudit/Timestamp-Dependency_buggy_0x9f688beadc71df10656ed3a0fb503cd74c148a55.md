# Vulnerability Analysis #
#### 2023-06-05 08:27:09 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 34, 5 ``string public name = "IWC ECOSYSTEM"``
        - Line 35, 5 ``string public symbol = "IWC"``

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

        - Line 44, 12 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
