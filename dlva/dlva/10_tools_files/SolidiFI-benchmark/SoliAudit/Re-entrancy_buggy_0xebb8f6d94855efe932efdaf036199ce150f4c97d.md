# Vulnerability Analysis #
#### 2023-06-05 09:01:33 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SSTORE POP PUSH DUP PUSH

        - Line 56, 3 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 65, 3 ``balances[_from] = balances[_from].sub(_value)``
        - Line 66, 3 ``balances[_to] = balances[_to].add(_value)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 17, 5 ``assert(b <= a)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 38, 9 ``msg.sender.call.value(10 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
