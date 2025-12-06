# Vulnerability Analysis #
#### 2023-05-29 09:11:40 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH SLOAD SWAP POP SWAP

        - Line 15, 16 ``A``
        - Line 18, 16 ``B``
        - Line 21, 16 ``lifeCoin``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* _`X`_ TimeDep
    - 100%, DUP JUMP JUMPDEST PUSH SLOAD

        - Line 4, 3 ``uint256 public FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968``
        - Line 7, 3 ``uint256 public B``
        - Line 8, 3 ``uint256 public C``

* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP JUMP JUMPDEST PUSH SLOAD

        - Line 4, 3 ``uint256 public FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968``
        - Line 7, 3 ``uint256 public B``
        - Line 8, 3 ``uint256 public C``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
