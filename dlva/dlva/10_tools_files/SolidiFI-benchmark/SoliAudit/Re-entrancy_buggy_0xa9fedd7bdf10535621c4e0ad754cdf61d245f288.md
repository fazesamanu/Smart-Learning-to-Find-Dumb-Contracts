# Vulnerability Analysis #
#### 2023-06-05 08:29:39 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name``
        - Line 5, 5 ``string public symbol``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 16, 9 ``counter_re_ent7``
        - Line 31, 9 ``balanceOf[_to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 16, 9 ``counter_re_ent7 += 1``
        - Line 31, 9 ``balanceOf[_to] += _value``

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

        - Line 13, 9 ``msg.sender.call.value(10 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
