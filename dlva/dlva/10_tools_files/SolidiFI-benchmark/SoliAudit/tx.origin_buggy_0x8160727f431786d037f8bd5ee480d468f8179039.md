# Vulnerability Analysis #
#### 2023-06-05 08:24:49 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 6, 5 ``string public name``
        - Line 7, 5 ``string public symbol``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 33, 9 ``balanceOf[_to]``
        - Line 76, 9 ``balanceOf[msg.sender]``
        - Line 77, 9 ``totalSupply``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 33, 9 ``balanceOf[_to] += _value``
        - Line 76, 9 ``balanceOf[msg.sender] += _value``
        - Line 77, 9 ``totalSupply += _value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 16, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 17, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
