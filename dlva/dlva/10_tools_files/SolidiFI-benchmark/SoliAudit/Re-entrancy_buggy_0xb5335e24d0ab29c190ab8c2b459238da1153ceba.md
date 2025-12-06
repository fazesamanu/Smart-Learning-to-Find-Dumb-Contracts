# Vulnerability Analysis #
#### 2023-06-05 08:43:09 ####

* _`X`_ Underflow
    - 100%, SLOAD SUB

        - Line 35, 5 ``balanceOf[msg.sender] -= _value``
        - Line 39, 5 ``currentSupply -= _value``
        - Line 59, 5 ``allowance[_from][msg.sender] -= _value``
        - Line 72, 5 ``balanceOf[_from] -= _value + burnPerTransaction``
        - Line 78, 5 ``currentSupply -= burnPerTransaction``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 37, 5 ``balanceOf[0x0]``
        - Line 74, 5 ``balanceOf[_to]``
        - Line 76, 5 ``balanceOf[0x0]``

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

        - Line 92, 9 ``msg.sender.call.value(transferValue_re_ent11)("")``

* __O__ BlockHash
* __O__ SelfDestruct
