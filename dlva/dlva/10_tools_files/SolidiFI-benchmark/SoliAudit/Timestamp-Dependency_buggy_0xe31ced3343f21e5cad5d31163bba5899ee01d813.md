# Vulnerability Analysis #
#### 2023-06-05 08:34:15 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 31, 9 ``return _name``
        - Line 37, 9 ``return _symbol``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 76, 58 ``_value``
        - Line 77, 44 ``_value``
        - Line 88, 48 ``_value``
        - Line 89, 44 ``_value``
        - Line 90, 70 ``_value``
        - Line 103, 76 ``_addedValue``
        - Line 112, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 76, 36 ``balances[msg.sender]``
        - Line 77, 29 ``balances[_to]``
        - Line 88, 31 ``balances[_from]``
        - Line 89, 29 ``balances[_to]``
        - Line 90, 42 ``allowed[_from][msg.sender]``
        - Line 103, 45 ``allowed[msg.sender][_spender]``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 13, 17 ``now``
        - Line 14, 33 ``now``
        - Line 15, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
