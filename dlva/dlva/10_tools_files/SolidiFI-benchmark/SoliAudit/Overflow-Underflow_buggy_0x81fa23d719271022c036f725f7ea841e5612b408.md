# Vulnerability Analysis #
#### 2023-06-05 08:45:52 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "GEN.FINANCE"``
        - Line 6, 5 ``string public symbol = "GEN"``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 17, 9 ``balanceOf[to]``
        - Line 24, 9 ``lockTime_intou29[msg.sender]``
        - Line 48, 9 ``balanceOf[to]``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, SHA SLOAD TIMESTAMP GT ISZERO

        - Line 27, 23 ``lockTime_intou29[msg.sender]``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 27, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
