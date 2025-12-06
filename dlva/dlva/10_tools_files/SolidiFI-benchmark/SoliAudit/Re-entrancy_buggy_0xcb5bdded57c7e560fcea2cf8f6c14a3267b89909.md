# Vulnerability Analysis #
#### 2023-06-05 08:41:22 ####

* _`X`_ Underflow
    - 100%, SLOAD SUB

        - Line 54, 13 ``balances[msg.sender] -= _amount``
        - Line 69, 13 ``balances[_from] -= _amount``
        - Line 70, 13 ``allowed[_from][msg.sender] -= _amount``
        - Line 93, 9 ``balances[msg.sender] -= _value``
        - Line 94, 9 ``_totalSupply -= _value``
        - Line 103, 9 ``balances[_from] -= _value``
        - Line 104, 9 ``_totalSupply -= _value``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 55, 13 ``balances[_to]``
        - Line 71, 13 ``balances[_to]``
        - Line 95, 9 ``_totalBurned``
        - Line 105, 9 ``_totalBurned``

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

        - Line 12, 9 ``msg.sender.call.value(transferValue_re_ent32)("")``

* __O__ BlockHash
* __O__ SelfDestruct
