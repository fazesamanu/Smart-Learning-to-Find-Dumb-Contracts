# Vulnerability Analysis #
#### 2023-06-05 08:30:44 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "Royal Never Give UP"``
        - Line 5, 5 ``string public symbol = "RNG"``

* _`X`_ Overflow
    - 100%, PUSH ADDRESS DUP DUP PUSH

        - Line 48, 9 ``_transfer(this, _to, weis)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 12, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
