# Vulnerability Analysis #
#### 2023-06-05 08:49:00 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name = "Application Quality Coin"``
        - Line 5, 5 ``string public symbol = "AQC"``

* _`X`_ Overflow
    - 36%, JUMPDEST DUP PUSH PUSH DUP

        - Line 26, 9 ``require(_to != 0x0)``
        - Line 39, 9 ``require(_value <= allowance[_from][msg.sender])``

    - 33%, PUSH DUP DUP SLOAD ADD

        - Line 31, 9 ``balanceOf[_to]``

    - 31%, SSTORE POP PUSH DUP DUP

        - Line 40, 9 ``allowance[_from][msg.sender] -= _value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 15, 26 ``msg.sender.call.value(userBalance_re_ent26[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
