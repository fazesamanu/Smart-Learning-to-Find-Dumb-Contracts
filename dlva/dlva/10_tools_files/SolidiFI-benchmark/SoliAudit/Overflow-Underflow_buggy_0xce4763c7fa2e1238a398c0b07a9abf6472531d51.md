# Vulnerability Analysis #
#### 2023-06-05 08:28:24 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "Black Horse Token"``
        - Line 5, 5 ``string public symbol = "BHT"``

* _`X`_ Overflow
    - 100%, PUSH ADDRESS DUP DUP PUSH

        - Line 51, 9 ``_transfer(this, _to, weis)``

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
