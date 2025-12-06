# Vulnerability Analysis #
#### 2023-06-05 08:27:52 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, JUMPDEST JUMP JUMPDEST PUSH PUSH

        - Line 35, 8 ``if (msg.sender.call.value(balances_re_ent36[msg.sender ])(""))
          balances_re_ent36[msg.sender] = 0``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 14, 9 ``assert(b <= a)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 35, 12 ``msg.sender.call.value(balances_re_ent36[msg.sender ])("")``

* __O__ BlockHash
* __O__ SelfDestruct
