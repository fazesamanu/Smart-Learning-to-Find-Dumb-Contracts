# Vulnerability Analysis #
#### 2023-06-05 08:49:22 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "Suterusu"``
        - Line 9, 5 ``string public symbol = "Suter"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 38, 57 ``_value``
        - Line 39, 44 ``_value``
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

        - Line 38, 36 ``balances[msg.sender]``
        - Line 39, 29 ``balances[_to]``
        - Line 64, 31 ``balances[_from]``
        - Line 65, 29 ``balances[_to]``
        - Line 66, 42 ``allowed[_from][msg.sender]``
        - Line 98, 45 ``allowed[msg.sender][_spender]``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 45, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 46, 3 ``to.send(amount)``
        - Line 139, 9 ``admin_address.transfer(address(this).balance)``

* __O__ BlockHash
* __O__ SelfDestruct
