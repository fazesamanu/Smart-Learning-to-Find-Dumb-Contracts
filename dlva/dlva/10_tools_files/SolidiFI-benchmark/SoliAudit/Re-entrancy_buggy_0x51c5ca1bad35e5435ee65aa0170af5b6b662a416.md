# Vulnerability Analysis #
#### 2023-06-05 08:46:22 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD PUSH

        - Line 27, 33 ``totalVoting[videoNum]``
        - Line 33, 37 ``totalVoting[videoNum]``
        - Line 41, 33 ``totalVoting[videoNum]``

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

        - Line 9, 25 ``msg.sender.call.value(balances_re_ent1[msg.sender ])("")``

* __O__ BlockHash
* __O__ SelfDestruct
