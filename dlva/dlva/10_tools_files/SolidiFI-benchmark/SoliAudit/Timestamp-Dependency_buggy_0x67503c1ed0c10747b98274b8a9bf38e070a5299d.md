# Vulnerability Analysis #
#### 2023-06-05 09:00:39 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public symbol = ""``
        - Line 5, 5 ``string public name = ""``

* _`X`_ Overflow
    - 100%, SHA SLOAD ADD GT JUMPDEST

        - Line 34, 16 ``balances[_to]``
        - Line 51, 16 ``balances[_to]``

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
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
