# Vulnerability Analysis #
#### 2023-06-05 08:59:29 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "Art coin"``
        - Line 9, 5 ``string public symbol = "ARTC"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 38, 57 ``_value``
        - Line 39, 44 ``_value``
        - Line 63, 48 ``_value``
        - Line 64, 44 ``_value``
        - Line 65, 70 ``_value``
        - Line 97, 76 ``_addedValue``
        - Line 114, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 38, 36 ``balances[msg.sender]``
        - Line 39, 29 ``balances[_to]``
        - Line 63, 31 ``balances[_from]``
        - Line 64, 29 ``balances[_to]``
        - Line 65, 42 ``allowed[_from][msg.sender]``
        - Line 97, 45 ``allowed[msg.sender][_spender]``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 45, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
