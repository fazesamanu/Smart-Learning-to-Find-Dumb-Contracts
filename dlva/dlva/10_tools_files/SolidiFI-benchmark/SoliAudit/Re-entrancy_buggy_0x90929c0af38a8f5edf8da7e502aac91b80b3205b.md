# Vulnerability Analysis #
#### 2023-06-05 08:45:30 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 37, 5 ``string public name``
        - Line 38, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, SLOAD SWAP POP DUP PUSH

        - Line 97, 29 ``allowed[_from][msg.sender]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, SHA SLOAD GT ISZERO JUMPDEST

        - Line 86, 38 ``balances[_to]``
        - Line 99, 33 ``balances[_to]``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 47, 17 ``msg.sender.call.value(_weiToWithdraw)("")``

* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, DUP PUSH SUB PUSH DUP

        - Line 86, 69 ``_value``
        - Line 99, 63 ``_value``

