# Vulnerability Analysis #
#### 2023-05-29 11:45:39 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, POP POP JUMP JUMPDEST CALLVALUE

        - Line 15, 3 ``userBalances[msg.sender] = 0``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* _`X`_ Reentrancy
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 14, 9 ``msg.sender.call``

* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 14, 9 ``msg.sender.call``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 14, 9 ``msg.sender.call.value(amountToWithdraw)()``

* __O__ BlockHash
* __O__ SelfDestruct
