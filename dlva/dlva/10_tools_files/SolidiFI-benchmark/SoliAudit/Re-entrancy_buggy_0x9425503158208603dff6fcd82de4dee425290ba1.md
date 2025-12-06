# Vulnerability Analysis #
#### 2023-06-05 08:50:01 ####

* _`X`_ Underflow
    - 100%, PUSH DIFFICULTY

        - Line 67, 58 ``uint256``

* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, DIFFICULTY COINBASE TIMESTAMP PUSH SLOAD

        - Line 69, 29 ``block.difficulty``

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

        - Line 69, 63 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
