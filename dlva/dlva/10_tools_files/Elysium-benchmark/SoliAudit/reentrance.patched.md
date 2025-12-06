# Vulnerability Analysis #
#### 2023-05-29 11:46:18 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 7, 5 ``balances[_to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 7, 5 ``balances[_to] += msg.value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* _`X`_ Reentrancy
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 15, 10 ``msg.sender.call``

* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 15, 10 ``msg.sender.call.value(_amount)()``

* __O__ BlockHash
* __O__ SelfDestruct
