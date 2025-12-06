# Vulnerability Analysis #
#### 2023-06-05 08:26:31 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "DREP"``
        - Line 6, 5 ``string public symbol = "DREP"``

* _`X`_ Overflow
    - 100%, DUP REVERT JUMPDEST PUSH CALLER

        - Line 19, 9 ``require(!stopped)``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, PUSH CALLER PUSH AND EQ

        - Line 23, 31 ``0x0``

* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH CALLER PUSH AND EQ

        - Line 23, 31 ``0x0``

* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, PUSH CALLER PUSH AND EQ

        - Line 23, 31 ``0x0``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 75, 9 ``msg.sender.call.value(transferValue_re_ent11)("")``

* __O__ BlockHash
* __O__ SelfDestruct
