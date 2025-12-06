# Vulnerability Analysis #
#### 2023-06-05 08:43:20 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "DREP"``
        - Line 5, 5 ``string public symbol = "DREP"``

* _`X`_ Overflow
    - 100%, DUP REVERT JUMPDEST PUSH CALLER

        - Line 18, 9 ``require(!stopped)``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, PUSH CALLER PUSH AND EQ

        - Line 22, 31 ``0x0``

* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH CALLER PUSH AND EQ

        - Line 22, 31 ``0x0``

* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, PUSH CALLER PUSH AND EQ

        - Line 22, 31 ``0x0``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
