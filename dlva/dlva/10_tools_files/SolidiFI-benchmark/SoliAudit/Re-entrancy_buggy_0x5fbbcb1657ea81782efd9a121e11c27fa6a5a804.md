# Vulnerability Analysis #
#### 2023-06-05 08:49:55 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name``
        - Line 5, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, SLOAD ADD LT ISZERO JUMPDEST

        - Line 25, 52 ``balanceOf[_to]``

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
