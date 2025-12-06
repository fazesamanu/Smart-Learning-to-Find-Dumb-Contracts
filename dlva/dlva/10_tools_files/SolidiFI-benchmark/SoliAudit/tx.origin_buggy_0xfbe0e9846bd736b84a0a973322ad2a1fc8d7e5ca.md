# Vulnerability Analysis #
#### 2023-06-05 08:50:50 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SWAP POP POP JUMP PUSHDEPLOYADDRESS

        - Line 31, 3 ``function add(uint256 a, uint256 b) internal pure returns (uint256) {
    uint256 c = a + b;
    assert(c >= a);
    return c;
  }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP GT JUMPDEST ISZERO ISZERO

        - Line 57, 16 ``_value``
        - Line 68, 16 ``_value``

* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 85, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 86, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
