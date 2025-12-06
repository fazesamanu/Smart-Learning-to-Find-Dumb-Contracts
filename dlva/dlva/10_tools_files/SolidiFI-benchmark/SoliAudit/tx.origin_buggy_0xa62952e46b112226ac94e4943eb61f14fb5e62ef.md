# Vulnerability Analysis #
#### 2023-06-05 08:27:30 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string  public name = "Utopia Credits"``
        - Line 5, 5 ``string  public symbol = "UTOC"``
        - Line 6, 5 ``string  public standard = "DApp Token v1.0"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 30, 9 ``balanceOf[_to]``
        - Line 43, 9 ``balanceOf[_to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 30, 9 ``balanceOf[_to] += _value``
        - Line 43, 9 ``balanceOf[_to] += _value``

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
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
