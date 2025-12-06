# Vulnerability Analysis #
#### 2023-06-05 08:51:53 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 33, 5 ``string public name``
        - Line 34, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, SSTORE POP PUSH DUP PUSH

        - Line 60, 9 ``balanceOf[_from] = balanceOf[_from].sub(_value)``
        - Line 79, 9 ``balanceOf[msg.sender] = balanceOf[msg.sender].sub(_value)``
        - Line 87, 9 ``balanceOf[_from] = balanceOf[_from].sub(_value)``
        - Line 88, 9 ``allowance[_from][msg.sender] = allowance[_from][msg.sender].sub(_value)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP PUSH SLOAD PUSH SWAP

        - Line 80, 39 ``_value``
        - Line 89, 39 ``_value``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 46, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
