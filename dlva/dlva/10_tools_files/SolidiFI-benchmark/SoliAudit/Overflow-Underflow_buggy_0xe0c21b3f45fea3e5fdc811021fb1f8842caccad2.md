# Vulnerability Analysis #
#### 2023-06-05 08:31:44 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SWAP POP POP JUMP PUSHDEPLOYADDRESS

        - Line 13, 5 ``function sub(uint256 a, uint256 b) internal constant returns(uint256) {
        assert(b <= a);
        return a - b;
    }``

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
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 39, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
