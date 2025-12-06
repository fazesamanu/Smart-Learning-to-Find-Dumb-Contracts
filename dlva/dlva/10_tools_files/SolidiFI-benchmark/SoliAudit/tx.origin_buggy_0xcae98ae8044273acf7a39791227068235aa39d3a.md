# Vulnerability Analysis #
#### 2023-06-05 08:27:57 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "Maxcoin"``
        - Line 5, 5 ``string public symbol = "MAX"``

* _`X`_ Overflow
    - 100%, JUMPI JUMPDEST DUP PUSH SWAP

        - Line 12, 9 ``assert(owner == msg.sender)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 50, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 51, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
