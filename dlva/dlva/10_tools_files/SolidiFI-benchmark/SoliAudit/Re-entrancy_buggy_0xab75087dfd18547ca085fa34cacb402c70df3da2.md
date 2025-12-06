# Vulnerability Analysis #
#### 2023-06-05 08:31:06 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 59, 5 ``string public name``
        - Line 61, 5 ``string public symbol``

* __O__ Overflow
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
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 128, 16 ``msg.sender.call.value(userBalance_re_ent19[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
