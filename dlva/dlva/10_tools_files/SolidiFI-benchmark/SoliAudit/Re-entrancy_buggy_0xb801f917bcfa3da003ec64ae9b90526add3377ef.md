# Vulnerability Analysis #
#### 2023-06-05 08:58:13 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, SWAP POP POP JUMP PUSHDEPLOYADDRESS

        - Line 19, 3 ``function sub(uint256 _a, uint256 _b) internal pure returns (uint256) {
    assert(_b <= _a);
    return _a - _b;
  }``

    - 48%, SSTORE POP PUSH DUP PUSH

        - Line 78, 13 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 89, 13 ``balances[_to] = _value.add(balances[_to])``
        - Line 90, 13 ``balances[_from] = balances[_from].sub(_value)``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPDEST GT JUMPDEST ISZERO PUSH

        - Line 77, 47 ``balances[_to].add(_value)``
        - Line 88, 82 ``balances[_to].add(_value)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 66, 17 ``msg.sender.call.value(_weiToWithdraw)("")``

* __O__ BlockHash
* _`X`_ SelfDestruct
    - 100%, SELFDESTRUCT JUMPDEST DUP PUSH PUSH

        - Line 104, 9 ``selfdestruct(owner)``

