# Vulnerability Analysis #
#### 2023-06-05 08:55:48 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = " ETHealth"``
        - Line 8, 5 ``string public symbol = "ETT"``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 26, 13 ``balances[_to]``
        - Line 33, 13 ``balances[_to]``
        - Line 56, 13 ``totalSupply``
        - Line 57, 13 ``balances[owner]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 13, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
