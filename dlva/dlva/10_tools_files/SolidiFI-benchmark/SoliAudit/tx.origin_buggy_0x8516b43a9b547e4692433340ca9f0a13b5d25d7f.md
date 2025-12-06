# Vulnerability Analysis #
#### 2023-06-05 08:22:29 ####

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

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 73, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 74, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
