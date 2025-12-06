# Vulnerability Analysis #
#### 2023-06-05 08:43:25 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 22, 3 ``string public name = "Darkswap"``
        - Line 23, 3 ``string public symbol = "DSWP"``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 50, 3 ``function transfer(address target, uint256 qty, bytes data) external returns (bool) {
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
    - 100%, PUSH ADD PUSH ADD SWAP

        - Line 45, 7 ``TokenReceiver(target).tokenFallback(target, qty, "")``

* __O__ TxOrigin
* __O__ CheckEffects
* _`X`_ InlineAssembly
    - 100%, POP PUSH DUP GT SWAP

        - Line 37, 7 ``codeLength := extcodesize(target)``

* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
