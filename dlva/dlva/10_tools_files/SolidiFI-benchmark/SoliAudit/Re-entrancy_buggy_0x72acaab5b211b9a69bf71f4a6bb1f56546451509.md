# Vulnerability Analysis #
#### 2023-06-05 08:52:58 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 37, 5 ``string public name``
        - Line 38, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, SLOAD SWAP POP DUP PUSH

        - Line 95, 29 ``allowed[_from][msg.sender]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, SHA SLOAD GT ISZERO JUMPDEST

        - Line 84, 38 ``balances[_to]``
        - Line 97, 33 ``balances[_to]``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 45, 12 ``msg.sender.call.value(balances_re_ent29[msg.sender ])("")``

* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, DUP PUSH SUB PUSH DUP

        - Line 84, 69 ``_value``
        - Line 97, 63 ``_value``

