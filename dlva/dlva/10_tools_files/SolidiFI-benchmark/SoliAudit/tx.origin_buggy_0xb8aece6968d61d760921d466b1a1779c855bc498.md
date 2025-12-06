# Vulnerability Analysis #
#### 2023-06-05 08:44:03 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 33, 5 ``string public name``
        - Line 34, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, SSTORE POP PUSH DUP PUSH

        - Line 53, 9 ``balanceOf[_from] = balanceOf[_from].sub(_value)``
        - Line 72, 9 ``balanceOf[msg.sender] = balanceOf[msg.sender].sub(_value)``
        - Line 80, 9 ``balanceOf[_from] = balanceOf[_from].sub(_value)``
        - Line 81, 9 ``allowance[_from][msg.sender] = allowance[_from][msg.sender].sub(_value)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP PUSH SLOAD PUSH SWAP

        - Line 73, 39 ``_value``
        - Line 82, 39 ``_value``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 41, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
