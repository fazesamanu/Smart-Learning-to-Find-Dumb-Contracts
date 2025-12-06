# Vulnerability Analysis #
#### 2023-06-05 08:55:21 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "Parametrica"``
        - Line 6, 5 ``string public symbol = "PARAM"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 9 ``balanceOf[to]``
        - Line 42, 9 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 9 ``balanceOf[to] += value``
        - Line 42, 9 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 23, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
