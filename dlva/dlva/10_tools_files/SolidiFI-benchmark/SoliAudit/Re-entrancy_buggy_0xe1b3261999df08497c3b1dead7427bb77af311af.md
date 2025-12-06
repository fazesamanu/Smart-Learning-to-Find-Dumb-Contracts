# Vulnerability Analysis #
#### 2023-06-05 08:27:41 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 25, 9 ``balances[_to]``
        - Line 36, 9 ``balances[_to]``
        - Line 56, 9 ``counter_re_ent7``

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

        - Line 53, 9 ``msg.sender.call.value(10 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
