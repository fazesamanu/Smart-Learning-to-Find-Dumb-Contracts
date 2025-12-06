# Vulnerability Analysis #
#### 2023-06-05 08:23:14 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 14, 2 ``string public symbol``

* _`X`_ Overflow
    - 100%, SWAP POP POP JUMP PUSHDEPLOYADDRESS

        - Line 6, 2 ``function sub(uint256 a, uint256 b) internal constant returns (uint256) { assert(b <= a); return a - b; }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 6, 75 ``assert(b <= a)``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 16, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 17, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
