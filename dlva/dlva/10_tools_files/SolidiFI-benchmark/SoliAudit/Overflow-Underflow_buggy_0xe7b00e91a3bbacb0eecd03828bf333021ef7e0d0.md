# Vulnerability Analysis #
#### 2023-06-05 09:01:44 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SSTORE POP PUSH DUP PUSH

        - Line 33, 9 ``balances[msg.sender] = balances[msg.sender].sub(numTokens)``
        - Line 49, 9 ``balances[owner] = balances[owner].sub(numTokens)``
        - Line 50, 9 ``allowed[owner][msg.sender] = allowed[owner][msg.sender].sub(numTokens)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 58, 7 ``assert(b <= a)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
