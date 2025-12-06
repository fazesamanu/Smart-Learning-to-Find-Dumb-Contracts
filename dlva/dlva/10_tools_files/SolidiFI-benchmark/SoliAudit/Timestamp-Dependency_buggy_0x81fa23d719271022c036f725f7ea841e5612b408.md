# Vulnerability Analysis #
#### 2023-06-05 08:52:25 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "GEN.FINANCE"``
        - Line 6, 5 ``string public symbol = "GEN"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 21, 9 ``balanceOf[to]``
        - Line 43, 9 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 21, 9 ``balanceOf[to] += value``
        - Line 43, 9 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 11, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
