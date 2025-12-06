# Vulnerability Analysis #
#### 2023-06-05 08:53:14 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 55, 9 ``return _name``
        - Line 61, 9 ``return _symbol``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 78, 64 ``_value``
        - Line 79, 50 ``_value``
        - Line 90, 53 ``_value``
        - Line 91, 50 ``_value``
        - Line 92, 76 ``_value``
        - Line 105, 82 ``_addedValue``
        - Line 114, 63 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SLOAD DUP PUSH JUMP JUMPDEST

        - Line 78, 42 ``balances[msg.sender]``
        - Line 79, 35 ``balances[_to]``
        - Line 90, 36 ``balances[_from]``
        - Line 91, 35 ``balances[_to]``
        - Line 92, 48 ``allowed[_from][msg.sender]``
        - Line 105, 51 ``allowed[msg.sender][_spender]``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 123, 16 ``msg.sender.call.value(userBalance_re_ent19[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
