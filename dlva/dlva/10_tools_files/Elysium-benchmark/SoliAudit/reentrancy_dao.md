# Vulnerability Analysis #
#### 2023-05-29 11:46:51 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 17, 9 ``credit[msg.sender]``
        - Line 18, 9 ``balance``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* _`X`_ Reentrancy
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 11, 31 ``msg.sender.call``

* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 11, 31 ``msg.sender.call``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 11, 31 ``msg.sender.call.value(oCredit)()``

* __O__ BlockHash
* __O__ SelfDestruct
