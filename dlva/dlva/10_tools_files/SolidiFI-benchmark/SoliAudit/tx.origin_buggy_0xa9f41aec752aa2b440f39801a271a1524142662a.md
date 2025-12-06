# Vulnerability Analysis #
#### 2023-06-05 08:52:36 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public symbol``
        - Line 5, 5 ``string public  name``

* _`X`_ Overflow
    - 100%, JUMPDEST PUSH SLOAD PUSH PUSH

        - Line 24, 9 ``require(_value2 > 0)``
        - Line 25, 9 ``require(balances[owner] >= _value2)``

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
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
