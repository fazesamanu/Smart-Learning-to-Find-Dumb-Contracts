# Vulnerability Analysis #
#### 2023-06-05 08:36:46 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 16, 5 ``string public name = "Vehicle Mounted Mining"``
        - Line 17, 5 ``string public symbol = "VM"``

* _`X`_ Overflow
    - 100%, LOG DUP PUSH AND PUSH

        - Line 99, 8 ``Mint(_to, _amount)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, DUP SWAP POP PUSH SLOAD

        - Line 80, 30 ``_value``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 50, 26 ``msg.sender.call.value(userBalance_re_ent33[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
