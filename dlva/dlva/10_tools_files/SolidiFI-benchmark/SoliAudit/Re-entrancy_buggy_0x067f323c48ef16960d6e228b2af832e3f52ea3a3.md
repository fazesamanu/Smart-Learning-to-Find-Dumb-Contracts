# Vulnerability Analysis #
#### 2023-06-05 08:36:30 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name``
        - Line 6, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, JUMPDEST JUMP JUMPDEST PUSH PUSH

        - Line 63, 8 ``if (owner == msg.sender) { 
          selfdestruct(owner); 
       }``

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

        - Line 17, 9 ``msg.sender.call.value(transferValue_re_ent39)("")``
        - Line 58, 13 ``spender.receiveApproval(msg.sender, _value, this, _extraData)``

* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, SELFDESTRUCT JUMPDEST JUMP JUMPDEST PUSH

        - Line 64, 11 ``selfdestruct(owner)``

