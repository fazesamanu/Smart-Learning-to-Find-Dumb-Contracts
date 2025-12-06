# Vulnerability Analysis #
#### 2023-06-05 08:58:46 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 20, 1 ``string public symbol``
        - Line 21, 1 ``string public name``

* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD PUSH

        - Line 37, 16 ``holders[_to]``
        - Line 50, 16 ``holders[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP PUSH PUSH

        - Line 35, 1 ``assert(_val <= holders[msg.sender])``
        - Line 46, 1 ``assert(_val <= holders[_from])``
        - Line 48, 1 ``assert(_val <= approach[_from][msg.sender])``

* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
