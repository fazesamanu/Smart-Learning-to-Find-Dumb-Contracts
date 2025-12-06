# Vulnerability Analysis #
#### 2023-06-05 08:43:52 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 18, 5 ``string public name``
        - Line 20, 5 ``string public symbol``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 32, 9 ``balances[_to]``
        - Line 39, 9 ``balances[_to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 32, 9 ``balances[_to] += _value``
        - Line 39, 9 ``balances[_to] += _value``

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

        - Line 10, 16 ``msg.sender.call.value(1 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
