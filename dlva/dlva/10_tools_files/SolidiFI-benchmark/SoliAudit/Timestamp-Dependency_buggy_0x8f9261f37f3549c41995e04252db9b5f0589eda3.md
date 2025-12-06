# Vulnerability Analysis #
#### 2023-06-05 08:54:43 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name``
        - Line 5, 5 ``string public symbol``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 27, 9 ``balanceOf[_to]``
        - Line 40, 9 ``balanceOf[_to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 27, 9 ``balanceOf[_to] += _value``
        - Line 40, 9 ``balanceOf[_to] += _value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 19, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
