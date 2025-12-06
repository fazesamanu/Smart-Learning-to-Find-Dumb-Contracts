# Vulnerability Analysis #
#### 2023-06-05 08:37:02 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 17, 9 ``return part1``
        - Line 20, 9 ``return part2``
        - Line 23, 9 ``return part3``
        - Line 26, 9 ``return hint``
        - Line 29, 9 ``return anotherHint``

* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 33, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
