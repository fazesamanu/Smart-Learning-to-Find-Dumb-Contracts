# Vulnerability Analysis #
#### 2023-06-05 08:31:22 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 9, 5 ``string public name = "BolvarChainX"``
        - Line 10, 5 ``string public symbol = "BLCX"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 39, 57 ``_value``
        - Line 40, 44 ``_value``
        - Line 69, 48 ``_value``
        - Line 70, 44 ``_value``
        - Line 71, 70 ``_value``
        - Line 103, 76 ``_addedValue``
        - Line 120, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 39, 36 ``balances[msg.sender]``
        - Line 40, 29 ``balances[_to]``
        - Line 69, 31 ``balances[_from]``
        - Line 70, 29 ``balances[_to]``
        - Line 71, 42 ``allowed[_from][msg.sender]``
        - Line 103, 45 ``allowed[msg.sender][_spender]``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 144, 9 ``admin_address.transfer(address(this).balance)``

* __O__ BlockHash
* __O__ SelfDestruct
