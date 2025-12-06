# Vulnerability Analysis #
#### 2023-06-05 08:56:47 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 17, 5 ``string public name = "VC Coin"``
        - Line 18, 5 ``string public symbol = "VCC"``

* _`X`_ Overflow
    - 100%, SHA SLOAD ADD GT JUMPDEST

        - Line 33, 47 ``balances[_to]``
        - Line 42, 82 ``balances[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 25, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
