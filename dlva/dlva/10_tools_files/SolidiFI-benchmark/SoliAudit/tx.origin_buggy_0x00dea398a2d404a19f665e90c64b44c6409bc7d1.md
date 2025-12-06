# Vulnerability Analysis #
#### 2023-06-05 08:28:40 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string public name``
        - Line 6, 2 ``string public symbol``

* _`X`_ Overflow
    - 100%, SLOAD ADD LT JUMPDEST ISZERO

        - Line 25, 40 ``balanceOf[_to]``

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
