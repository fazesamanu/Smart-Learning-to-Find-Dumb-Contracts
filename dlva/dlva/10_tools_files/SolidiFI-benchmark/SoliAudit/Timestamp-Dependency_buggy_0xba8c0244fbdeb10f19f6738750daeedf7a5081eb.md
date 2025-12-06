# Vulnerability Analysis #
#### 2023-06-05 08:56:42 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "Suterusu"``
        - Line 9, 5 ``string public symbol = "Suter"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 42, 57 ``_value``
        - Line 43, 44 ``_value``
        - Line 65, 48 ``_value``
        - Line 66, 44 ``_value``
        - Line 67, 70 ``_value``
        - Line 99, 76 ``_addedValue``
        - Line 116, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 26, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 26, 34 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
