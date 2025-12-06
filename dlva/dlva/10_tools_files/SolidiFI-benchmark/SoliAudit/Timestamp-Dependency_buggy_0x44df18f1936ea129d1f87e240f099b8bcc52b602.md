# Vulnerability Analysis #
#### 2023-06-05 08:38:39 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 38, 5 ``string public name``
        - Line 39, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, SLOAD SWAP POP DUP PUSH

        - Line 96, 29 ``allowed[_from][msg.sender]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 45, 6 ``startTime``

* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, SHA SLOAD GT ISZERO JUMPDEST

        - Line 85, 38 ``balances[_to]``
        - Line 98, 33 ``balances[_to]``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 45, 34 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, DUP PUSH SUB PUSH DUP

        - Line 85, 69 ``_value``
        - Line 98, 63 ``_value``

