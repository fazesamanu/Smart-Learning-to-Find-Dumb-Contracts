# Vulnerability Analysis #
#### 2023-06-05 08:54:14 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SSTORE POP PUSH DUP PUSH

        - Line 52, 9 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 59, 9 ``balances[_to] = balances[_to].add(_value)``

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
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
