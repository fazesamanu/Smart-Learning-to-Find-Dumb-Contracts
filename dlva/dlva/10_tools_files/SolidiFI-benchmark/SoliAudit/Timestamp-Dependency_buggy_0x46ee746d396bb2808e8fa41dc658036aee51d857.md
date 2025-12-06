# Vulnerability Analysis #
#### 2023-06-05 08:37:45 ####

* __O__ Underflow
* _`X`_ Overflow
    - 35%, PUSH DUP DUP SLOAD ADD

        - Line 49, 13 ``balances[msg.sender]``
        - Line 53, 13 ``balances[leaders[index]]``
        - Line 54, 13 ``balances[owner]``

    - 33%, SLOAD ADD SWAP POP POP

        - Line 49, 13 ``balances[msg.sender] += buyins[index]``
        - Line 53, 13 ``balances[leaders[index]] += (buyins[index] * 95 / 100)``
        - Line 54, 13 ``balances[owner] += (buyins[index] * 5 / 100)``

    - 32%, ADD SWAP POP POP DUP

        - Line 49, 13 ``balances[msg.sender] += buyins[index]``
        - Line 53, 13 ``balances[leaders[index]] += (buyins[index] * 95 / 100)``
        - Line 54, 13 ``balances[owner] += (buyins[index] * 5 / 100)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 11, 17 ``now``
        - Line 12, 34 ``now``
        - Line 13, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
