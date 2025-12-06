# Vulnerability Analysis #
#### 2023-06-05 08:27:35 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "Application Quality Coin"``
        - Line 5, 5 ``string public symbol = "AQC"``

* _`X`_ Overflow
    - 52%, JUMPDEST DUP PUSH PUSH DUP

        - Line 19, 9 ``require(_to != 0x0)``
        - Line 32, 9 ``require(_value <= allowance[_from][msg.sender])``

    - 48%, PUSH DUP DUP SLOAD ADD

        - Line 24, 9 ``balanceOf[_to]``

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
