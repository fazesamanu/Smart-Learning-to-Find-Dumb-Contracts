# Vulnerability Analysis #
#### 2023-06-05 08:57:52 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 16, 5 ``string public name = "Vehicle Mounted Mining"``
        - Line 17, 5 ``string public symbol = "VM"``

* _`X`_ Overflow
    - 100%, LOG DUP PUSH AND PUSH

        - Line 93, 8 ``Mint(_to, _amount)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP PUSH SLOAD PUSH SWAP

        - Line 79, 39 ``burnAmount``
        - Line 80, 35 ``burnAmount``
        - Line 91, 33 ``_amount``

* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, DUP SWAP POP PUSH SLOAD

        - Line 74, 30 ``_value``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 45, 12 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
