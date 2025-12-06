# Vulnerability Analysis #
#### 2023-06-05 08:44:19 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, REVERT JUMPDEST POP PUSH JUMP

        - Line 4, 22 ``24 () public payable {
	uin``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, REVERT JUMPDEST POP PUSH JUMP

        - Line 4, 22 ``24 () public payable {
	uin``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 7, 17 ``now``
        - Line 8, 34 ``now``
        - Line 9, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, SELFDESTRUCT JUMPDEST JUMP JUMPDEST PUSH

        - Line 109, 13 ``selfdestruct(feeAddress)``

