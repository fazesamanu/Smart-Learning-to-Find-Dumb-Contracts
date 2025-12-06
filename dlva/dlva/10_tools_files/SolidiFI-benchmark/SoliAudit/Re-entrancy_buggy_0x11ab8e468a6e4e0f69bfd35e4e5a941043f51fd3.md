# Vulnerability Analysis #
#### 2023-06-05 08:42:25 ####

* __O__ Underflow
* _`X`_ Overflow
    - 54%, SLOAD SWAP POP PUSH PUSH

        - Line 54, 21 ``indexToAddress[msg.sender]``
        - Line 79, 21 ``indexToAddress[msg.sender]``
        - Line 101, 20 ``passwordToAddress[msg.sender][_index]``
        - Line 114, 19 ``totalFee``

    - 46%, DUP MSTORE POP PUSH PUSH

        - Line 53, 32 ``Transfer(msg.sender, msg.value)``
        - Line 78, 32 ``Transfer(msg.sender, msg.value)``

* __O__ Multisig
* _`X`_ CallDepth
    - 100%, DUP PUSH SLOAD CALLVALUE GT

        - Line 54, 5 ``uint256 index``

* _`X`_ TOD
    - 100%, PUSH SLOAD CALLVALUE GT DUP

        - Line 49, 19 ``commissionFee``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, PUSH REVERT JUMPDEST POP CALLER

        - Line 4, 23 ``;``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
