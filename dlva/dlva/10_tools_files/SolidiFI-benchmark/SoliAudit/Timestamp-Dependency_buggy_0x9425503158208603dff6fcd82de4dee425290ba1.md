# Vulnerability Analysis #
#### 2023-06-05 08:53:58 ####

* _`X`_ Underflow
    - 100%, PUSH DIFFICULTY

        - Line 63, 58 ``uint256``

* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, DIFFICULTY COINBASE TIMESTAMP PUSH SLOAD

        - Line 65, 29 ``block.difficulty``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, PUSH REVERT JUMPDEST POP PUSH

        - Line 5, 10 `` ``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 18, 34 ``block.timestamp``
        - Line 65, 63 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
