# Vulnerability Analysis #
#### 2023-06-05 08:32:38 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name = "dmaToken"``
        - Line 9, 5 ``string public symbol = "DMA"``

* _`X`_ Overflow
    - 100%, DUP PUSH JUMP JUMPDEST PUSH

        - Line 38, 57 ``_value``
        - Line 39, 44 ``_value``
        - Line 68, 48 ``_value``
        - Line 69, 44 ``_value``
        - Line 70, 70 ``_value``
        - Line 102, 76 ``_addedValue``
        - Line 119, 59 ``_subtractedValue``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 143, 9 ``admin_address.transfer(address(this).balance)``

* __O__ BlockHash
* __O__ SelfDestruct
