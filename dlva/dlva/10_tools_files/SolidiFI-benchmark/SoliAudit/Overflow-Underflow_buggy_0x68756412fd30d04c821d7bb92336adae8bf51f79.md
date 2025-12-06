# Vulnerability Analysis #
#### 2023-06-05 08:25:32 ####

* _`X`_ Underflow
    - 49%, SLOAD SUB

        - Line 36, 13 ``balances_intou14[msg.sender]``
        - Line 37, 5 ``balances_intou14[msg.sender] -= _value``

    - 31%, AND JUMP

        - Line 56, 32 ``balances[msg.sender].sub(_value)``
        - Line 57, 25 ``balances[_to].add(_value)``
        - Line 63, 25 ``balances[_to].add(_value)``
        - Line 64, 27 ``balances[_from].sub(_value)``
        - Line 65, 38 ``_allowance.sub(_value)``

    - 20%, SUB LT

        - Line 36, 13 ``balances_intou14[msg.sender] - _value``

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
    - 100%, PUSH DUP DUP PUSH PUSH

        - Line 35, 69 ``bool``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
