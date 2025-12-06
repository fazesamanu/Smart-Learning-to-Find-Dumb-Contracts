# Vulnerability Analysis #
#### 2023-06-05 09:00:34 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "YTC"``
        - Line 9, 5 ``string public symbol = "YTC"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 38, 57 ``_value``
        - Line 39, 44 ``_value``
        - Line 60, 48 ``_value``
        - Line 61, 44 ``_value``
        - Line 62, 70 ``_value``
        - Line 94, 76 ``_addedValue``
        - Line 111, 59 ``_subtractedValue``
        - Line 132, 46 ``_value``
        - Line 133, 40 ``_value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 38, 36 ``balances[msg.sender]``
        - Line 39, 29 ``balances[_to]``
        - Line 60, 31 ``balances[_from]``
        - Line 61, 29 ``balances[_to]``
        - Line 62, 42 ``allowed[_from][msg.sender]``
        - Line 94, 45 ``allowed[msg.sender][_spender]``
        - Line 132, 30 ``balances[_who]``
        - Line 133, 27 ``totalSupply``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 156, 9 ``admin_address.transfer(address(this).balance)``

* __O__ BlockHash
* __O__ SelfDestruct
