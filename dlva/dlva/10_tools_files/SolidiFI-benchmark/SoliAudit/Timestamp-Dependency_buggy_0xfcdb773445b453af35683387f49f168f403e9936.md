# Vulnerability Analysis #
#### 2023-06-05 08:53:09 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "Med Chain"``
        - Line 9, 5 ``string public symbol = "MED"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 41, 57 ``_value``
        - Line 42, 44 ``_value``
        - Line 64, 48 ``_value``
        - Line 65, 44 ``_value``
        - Line 66, 70 ``_value``
        - Line 98, 76 ``_addedValue``
        - Line 115, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 41, 36 ``balances[msg.sender]``
        - Line 42, 29 ``balances[_to]``
        - Line 64, 31 ``balances[_from]``
        - Line 65, 29 ``balances[_to]``
        - Line 66, 42 ``allowed[_from][msg.sender]``
        - Line 98, 45 ``allowed[msg.sender][_spender]``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 25, 12 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
