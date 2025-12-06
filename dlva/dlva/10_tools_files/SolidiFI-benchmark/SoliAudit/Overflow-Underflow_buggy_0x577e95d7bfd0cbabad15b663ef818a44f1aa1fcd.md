# Vulnerability Analysis #
#### 2023-06-05 08:41:17 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 21, 1 ``string public symbol``
        - Line 22, 1 ``string public name``

* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD PUSH

        - Line 44, 16 ``holders[_to]``
        - Line 57, 16 ``holders[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP PUSH PUSH

        - Line 42, 1 ``assert(_val <= holders[msg.sender])``
        - Line 53, 1 ``assert(_val <= holders[_from])``
        - Line 55, 1 ``assert(_val <= approach[_from][msg.sender])``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
