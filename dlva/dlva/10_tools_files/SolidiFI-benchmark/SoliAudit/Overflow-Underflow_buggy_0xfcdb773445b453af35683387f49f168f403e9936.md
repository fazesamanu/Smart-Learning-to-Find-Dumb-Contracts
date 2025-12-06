# Vulnerability Analysis #
#### 2023-06-05 08:59:45 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "Med Chain"``
        - Line 9, 5 ``string public symbol = "MED"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 38, 57 ``_value``
        - Line 39, 44 ``_value``
        - Line 70, 48 ``_value``
        - Line 71, 44 ``_value``
        - Line 72, 70 ``_value``
        - Line 104, 76 ``_addedValue``
        - Line 121, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, SHA SLOAD TIMESTAMP GT ISZERO

        - Line 50, 23 ``lockTime_intou5[msg.sender]``

* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 38, 36 ``balances[msg.sender]``
        - Line 39, 29 ``balances[_to]``
        - Line 70, 31 ``balances[_from]``
        - Line 71, 29 ``balances[_to]``
        - Line 72, 42 ``allowed[_from][msg.sender]``
        - Line 104, 45 ``allowed[msg.sender][_spender]``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 50, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
