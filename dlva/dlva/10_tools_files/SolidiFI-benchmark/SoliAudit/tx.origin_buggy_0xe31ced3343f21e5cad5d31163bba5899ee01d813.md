# Vulnerability Analysis #
#### 2023-06-05 08:22:59 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 25, 9 ``return _name``
        - Line 31, 9 ``return _symbol``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 70, 58 ``_value``
        - Line 71, 44 ``_value``
        - Line 82, 48 ``_value``
        - Line 83, 44 ``_value``
        - Line 84, 70 ``_value``
        - Line 97, 76 ``_addedValue``
        - Line 106, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 70, 36 ``balances[msg.sender]``
        - Line 71, 29 ``balances[_to]``
        - Line 82, 31 ``balances[_from]``
        - Line 83, 29 ``balances[_to]``
        - Line 84, 42 ``allowed[_from][msg.sender]``
        - Line 97, 45 ``allowed[msg.sender][_spender]``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 12, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 13, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
