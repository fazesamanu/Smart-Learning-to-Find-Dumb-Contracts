# Vulnerability Analysis #
#### 2023-06-05 09:01:01 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 22, 3 ``string public name = "Darkswap"``
        - Line 23, 3 ``string public symbol = "DSWP"``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 52, 3 ``function transfer(address target, uint256 qty, bytes data) external returns (bool) {
    balanceOf[msg.sender] = balanceOf[msg.sender].sub(qty);
    balanceOf[target] = balanceOf[target].add(qty);
    if (isContract(target)) {
      TokenReceiver(target).tokenFallback(target, qty, data);
    }
    emit Transfer(msg.sender, target, qty);
    return true;
  }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 28, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* _`X`_ InlineAssembly
    - 100%, POP PUSH DUP GT SWAP

        - Line 39, 7 ``codeLength := extcodesize(target)``

* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 27, 16 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
