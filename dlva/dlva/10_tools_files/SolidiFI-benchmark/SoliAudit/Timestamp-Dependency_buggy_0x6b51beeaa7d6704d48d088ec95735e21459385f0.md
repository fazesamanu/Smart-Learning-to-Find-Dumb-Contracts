# Vulnerability Analysis #
#### 2023-06-05 09:00:07 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "YTC"``
        - Line 9, 5 ``string public symbol = "YTC"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 38, 57 ``_value``
        - Line 39, 44 ``_value``
        - Line 64, 48 ``_value``
        - Line 65, 44 ``_value``
        - Line 66, 70 ``_value``
        - Line 98, 76 ``_addedValue``
        - Line 115, 59 ``_subtractedValue``
        - Line 129, 46 ``_value``
        - Line 130, 40 ``_value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 46, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 46, 34 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
