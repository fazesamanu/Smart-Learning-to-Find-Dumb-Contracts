# Vulnerability Analysis #
#### 2023-05-29 08:50:09 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH ADD SWAP SWAP POP

        - Line 22, 9 ``contentCount++``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, PUSH AND SELFDESTRUCT JUMPDEST PUSH

        - Line 19, 9 ``selfdestruct(owner)``

