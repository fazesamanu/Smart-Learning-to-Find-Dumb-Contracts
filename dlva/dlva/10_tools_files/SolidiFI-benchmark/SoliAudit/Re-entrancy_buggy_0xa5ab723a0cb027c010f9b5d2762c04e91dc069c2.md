# Vulnerability Analysis #
#### 2023-06-05 08:54:38 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "CUM"``
        - Line 6, 5 ``string public symbol = "CUM"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 9 ``balanceOf[to]``
        - Line 43, 9 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 9 ``balanceOf[to] += value``
        - Line 43, 9 ``balanceOf[to] += value``

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

        - Line 23, 12 ``msg.sender.call.value(balances_re_ent29[msg.sender ])("")``

* __O__ BlockHash
* __O__ SelfDestruct
