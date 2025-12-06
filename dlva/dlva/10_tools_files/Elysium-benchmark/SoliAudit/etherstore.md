# Vulnerability Analysis #
#### 2023-05-29 11:45:49 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD TIMESTAMP

        - Line 14, 24 ``lastWithdrawTime[msg.sender]``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, SLOAD DUP JUMP JUMPDEST CALLVALUE

        - Line 5, 5 ``uint256 public withdrawalLimit = 1 ether``

* _`X`_ TimeDep
    - 100%, ADD TIMESTAMP LT ISZERO ISZERO

        - Line 14, 24 ``lastWithdrawTime[msg.sender] + 1 weeks``

* _`X`_ Reentrancy
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 15, 17 ``msg.sender.call``

* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, AND DUP PUSH MLOAD PUSH

        - Line 15, 17 ``msg.sender.call``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 14, 17 ``now``
        - Line 17, 40 ``now``

* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 15, 17 ``msg.sender.call.value(_weiToWithdraw)()``

* __O__ BlockHash
* __O__ SelfDestruct
