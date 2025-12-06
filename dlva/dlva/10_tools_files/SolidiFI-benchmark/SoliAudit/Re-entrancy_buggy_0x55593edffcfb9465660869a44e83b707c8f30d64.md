# Vulnerability Analysis #
#### 2023-06-05 08:54:20 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, SSTORE POP PUSH DUP PUSH

        - Line 57, 9 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 64, 9 ``balances[_to] = balances[_to].add(_value)``

    - 48%, PUSH SHA SLOAD PUSH SWAP

        - Line 57, 32 ``balances[msg.sender]``
        - Line 58, 25 ``balances[_to]``
        - Line 64, 25 ``balances[_to]``
        - Line 65, 27 ``balances[_from]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 14, 9 ``assert(b <= a)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 37, 16 ``msg.sender.call.value(userBalance_re_ent12[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
