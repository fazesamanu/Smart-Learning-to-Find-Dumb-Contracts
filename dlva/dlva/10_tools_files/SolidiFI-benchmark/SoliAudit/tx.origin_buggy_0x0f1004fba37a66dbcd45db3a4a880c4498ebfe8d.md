# Vulnerability Analysis #
#### 2023-06-05 08:59:13 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "Natterix"``
        - Line 6, 5 ``string public symbol = "NRX"``

* _`X`_ Overflow
    - 100%, JUMPI JUMPDEST DUP PUSH SWAP

        - Line 19, 9 ``assert(owner == msg.sender)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP PUSH PUSH

        - Line 27, 9 ``assert(0x0 != msg.sender)``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 81, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 82, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
