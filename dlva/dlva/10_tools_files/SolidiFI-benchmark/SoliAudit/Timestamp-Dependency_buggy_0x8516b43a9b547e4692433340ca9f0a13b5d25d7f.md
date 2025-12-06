# Vulnerability Analysis #
#### 2023-06-05 08:56:52 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "TheInternetCoin"``
        - Line 5, 5 ``string public symbol = "INT"``

* _`X`_ Overflow
    - 100%, POP DUP JUMP JUMPDEST CALLER

        - Line 4, 5 ``string public name = "TheInternetCoin"``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP PUSH PUSH

        - Line 14, 9 ``assert(owner == msg.sender)``
        - Line 22, 9 ``assert(0x0 != msg.sender)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 73, 16 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
