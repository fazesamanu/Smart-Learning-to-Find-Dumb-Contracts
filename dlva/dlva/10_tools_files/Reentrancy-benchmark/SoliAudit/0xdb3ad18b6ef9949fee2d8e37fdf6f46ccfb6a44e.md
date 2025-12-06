# Vulnerability Analysis #
#### 2023-05-29 09:11:09 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, JUMPDEST PUSH JUMPDEST DUP PUSH

        - Line 26, 39 ``token == ETH ? HYDRO_ETH : token``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS STATICCALL

        - Line 26, 16 ``Hydro(HYDRO).balanceOf(token == ETH ? HYDRO_ETH : token, account)``

* __O__ BlockHash
* __O__ SelfDestruct
