# Vulnerability Analysis #
#### 2023-06-05 08:31:39 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "Please Read This Contract"``
        - Line 5, 5 ``string public symbol = "READ-THIS"``

* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD PUSH

        - Line 40, 28 ``balances[receiver]``
        - Line 47, 30 ``balances[msg.sender]``

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

        - Line 17, 17 ``msg.sender.call.value(_weiToWithdraw)("")``

* __O__ BlockHash
* __O__ SelfDestruct
