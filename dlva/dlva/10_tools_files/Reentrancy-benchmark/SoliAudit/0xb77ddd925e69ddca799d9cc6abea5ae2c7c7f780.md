# Vulnerability Analysis #
#### 2023-05-29 08:48:27 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, RETURN JUMPDEST PUSH PUSH PUSH

        - Line 8, 5 ``address public chainlink = 0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS STATICCALL

        - Line 10, 16 ``IChainlink(chainlink).latestAnswer()``

* __O__ BlockHash
* __O__ SelfDestruct
