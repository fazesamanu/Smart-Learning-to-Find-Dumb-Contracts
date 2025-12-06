# Vulnerability Analysis #
#### 2023-06-05 08:47:06 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, SSTORE POP PUSH DUP PUSH

        - Line 58, 9 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 65, 9 ``balances[_to] = balances[_to].add(_value)``

    - 48%, PUSH SHA SLOAD PUSH SWAP

        - Line 58, 32 ``balances[msg.sender]``
        - Line 59, 25 ``balances[_to]``
        - Line 65, 25 ``balances[_to]``
        - Line 66, 27 ``balances[_from]``

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
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 39, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
