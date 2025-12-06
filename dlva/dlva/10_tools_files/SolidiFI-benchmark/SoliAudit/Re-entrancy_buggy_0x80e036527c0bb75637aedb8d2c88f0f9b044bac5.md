# Vulnerability Analysis #
#### 2023-06-05 08:31:33 ####

* _`X`_ Underflow
    - 100%, SLOAD SUB

        - Line 33, 32 ``balances[msg.sender]``
        - Line 47, 27 ``balances[_from]``
        - Line 49, 38 ``allowed[_from][msg.sender]``

* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD PUSH

        - Line 34, 25 ``balances[_to]``
        - Line 48, 25 ``balances[_to]``
        - Line 54, 38 ``allowed[msg.sender][_spender]``

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

        - Line 13, 16 ``msg.sender.call.value(1 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
