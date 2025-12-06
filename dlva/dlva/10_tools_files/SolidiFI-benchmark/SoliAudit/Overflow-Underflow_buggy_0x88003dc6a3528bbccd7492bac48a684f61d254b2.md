# Vulnerability Analysis #
#### 2023-06-05 08:37:35 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 54, 9 ``return _name``
        - Line 60, 9 ``return _symbol``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 77, 64 ``_value``
        - Line 78, 50 ``_value``
        - Line 89, 53 ``_value``
        - Line 90, 50 ``_value``
        - Line 91, 76 ``_value``
        - Line 104, 82 ``_addedValue``
        - Line 113, 63 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 77, 42 ``balances[msg.sender]``
        - Line 78, 35 ``balances[_to]``
        - Line 89, 36 ``balances[_from]``
        - Line 90, 35 ``balances[_to]``
        - Line 91, 48 ``allowed[_from][msg.sender]``
        - Line 104, 51 ``allowed[msg.sender][_spender]``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
