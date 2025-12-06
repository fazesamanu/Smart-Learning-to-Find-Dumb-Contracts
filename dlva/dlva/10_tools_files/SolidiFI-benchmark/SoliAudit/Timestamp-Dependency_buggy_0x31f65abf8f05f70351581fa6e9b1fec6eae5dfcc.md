# Vulnerability Analysis #
#### 2023-06-05 08:32:49 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "GeneralSwap"``
        - Line 6, 5 ``string public symbol = "GENS"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 26, 9 ``balanceOf[to]``
        - Line 48, 9 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 26, 9 ``balanceOf[to] += value``
        - Line 48, 9 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 12, 17 ``now``
        - Line 13, 34 ``now``
        - Line 14, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
