# Vulnerability Analysis #
#### 2023-06-05 08:45:57 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "OCX"``
        - Line 5, 5 ``string public symbol = "OCX"``

* _`X`_ Overflow
    - 100%, DUP REVERT JUMPDEST PUSH CALLER

        - Line 25, 9 ``require(_value >= 100000000)``

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
