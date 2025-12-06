# Vulnerability Analysis #
#### 2023-06-05 08:44:30 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, REVERT JUMPDEST POP PUSH JUMP

        - Line 5, 3 ``      uint gameId,
        ``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 15, 17 ``tx.origin``

* _`X`_ CheckEffects
    - 100%, REVERT JUMPDEST POP PUSH JUMP

        - Line 5, 3 ``      uint gameId,
        ``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, SELFDESTRUCT JUMPDEST JUMP JUMPDEST PUSH

        - Line 102, 13 ``selfdestruct(feeAddress)``

