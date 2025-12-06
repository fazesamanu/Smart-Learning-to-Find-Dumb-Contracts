# Vulnerability Analysis #
#### 2023-05-29 11:46:28 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SLOAD SWAP POP PUSH PUSH

        - Line 9, 33 ``rewardsForA[recipient]``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, SLOAD SWAP POP PUSH PUSH

        - Line 9, 33 ``rewardsForA[recipient]``

* __O__ TimeDep
* _`X`_ Reentrancy
    - 100%, SUB DUP DUP DUP GAS

        - Line 11, 28 ``recipient.call.value(amountToWithdraw)("")``

* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 11, 28 ``recipient.call.value(amountToWithdraw)("")``

* __O__ BlockHash
* __O__ SelfDestruct
