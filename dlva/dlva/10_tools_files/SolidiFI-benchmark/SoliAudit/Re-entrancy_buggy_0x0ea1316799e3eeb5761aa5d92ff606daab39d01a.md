# Vulnerability Analysis #
#### 2023-06-05 08:40:44 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SWAP POP POP JUMP PUSHDEPLOYADDRESS

        - Line 40, 3 ``function add(uint256 a, uint256 b) internal pure returns (uint256 c) {
    c = a + b;
    assert(c >= a);
    return c;
  }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 36, 5 ``assert(b <= a)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 54, 17 ``msg.sender.call.value(_weiToWithdraw)("")``

* __O__ BlockHash
* __O__ SelfDestruct
