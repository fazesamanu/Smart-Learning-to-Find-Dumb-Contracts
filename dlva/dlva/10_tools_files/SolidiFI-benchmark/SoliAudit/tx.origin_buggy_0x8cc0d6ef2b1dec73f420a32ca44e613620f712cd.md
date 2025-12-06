# Vulnerability Analysis #
#### 2023-06-05 08:32:27 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 3 ``string public name = "LOL Token"``
        - Line 5, 3 ``string public symbol = "LOL"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 33, 58 ``_value``
        - Line 34, 44 ``_value``
        - Line 41, 44 ``_value``
        - Line 42, 48 ``_value``
        - Line 43, 54 ``_value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 20, 5 ``assert(b <= a)``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 15, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 16, 3 ``to.send(amount)``

* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, SELFDESTRUCT JUMPDEST PUSH DUP SLOAD

        - Line 72, 2 ``selfdestruct(_creator)``

