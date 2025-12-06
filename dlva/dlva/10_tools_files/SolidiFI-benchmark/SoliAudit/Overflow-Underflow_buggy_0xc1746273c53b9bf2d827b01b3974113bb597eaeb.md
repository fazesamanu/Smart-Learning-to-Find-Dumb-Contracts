# Vulnerability Analysis #
#### 2023-06-05 08:56:04 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 3 ``string public standard = 'ERC20'``
        - Line 5, 3 ``string public name``
        - Line 6, 3 ``string public symbol``

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
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
