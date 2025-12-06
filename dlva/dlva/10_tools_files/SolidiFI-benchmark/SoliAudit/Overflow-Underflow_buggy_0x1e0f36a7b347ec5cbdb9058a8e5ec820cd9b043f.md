# Vulnerability Analysis #
#### 2023-06-05 09:01:27 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "GiGi"``
        - Line 5, 5 ``string public symbol = "GG"``

* _`X`_ Overflow
    - 100%, PUSH ADDRESS DUP DUP PUSH

        - Line 53, 9 ``_transfer(this, _to, weis)``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, SHA SLOAD TIMESTAMP GT ISZERO

        - Line 17, 23 ``lockTime_intou37[msg.sender]``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 17, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
