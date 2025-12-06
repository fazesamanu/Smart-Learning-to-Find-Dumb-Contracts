# Vulnerability Analysis #
#### 2023-06-05 08:28:19 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 28, 5 ``string public name = "HBI Token"``
        - Line 29, 5 ``string public symbol = "HBI"``

* _`X`_ Overflow
    - 100%, JUMPI JUMPDEST PUSH PUSH DUP

        - Line 36, 9 ``assert(0x0 != msg.sender)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 41, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 41, 34 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
