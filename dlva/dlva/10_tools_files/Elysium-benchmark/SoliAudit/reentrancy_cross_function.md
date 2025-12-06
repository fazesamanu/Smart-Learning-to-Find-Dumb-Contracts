# Vulnerability Analysis #
#### 2023-05-29 11:46:39 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 8, 13 ``userBalances[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 8, 13 ``userBalances[to] += amount``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* _`X`_ Reentrancy
    - 50%, SUB DUP DUP DUP GAS

        - Line 14, 28 ``msg.sender.call.value(amountToWithdraw)("")``

    - 50%, DUP DUP GAS CALL SWAP

        - Line 14, 28 ``msg.sender.call.value(amountToWithdraw)("")``

* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 14, 28 ``msg.sender.call.value(amountToWithdraw)("")``

* __O__ BlockHash
* __O__ SelfDestruct
