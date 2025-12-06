# Vulnerability Analysis #
#### 2023-06-05 08:58:35 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "ADS"``
        - Line 5, 5 ``string public symbol = "ADS"``

* _`X`_ Overflow
    - 100%, POP DUP JUMP JUMPDEST CALLER

        - Line 4, 5 ``string public name = "ADS"``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP PUSH PUSH

        - Line 22, 9 ``assert(0x0 != msg.sender)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 71, 12 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
