# Vulnerability Analysis #
#### 2023-06-05 08:34:47 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* _`X`_ CallDepth
    - 100%, DUP PUSH SLOAD CALLVALUE GT

        - Line 53, 5 ``uint256 index``

* _`X`_ TOD
    - 100%, PUSH SLOAD CALLVALUE GT DUP

        - Line 48, 19 ``commissionFee``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
