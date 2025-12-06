# Vulnerability Analysis #
#### 2023-06-05 08:23:35 ####

* _`X`_ Underflow
    - 69%, SLOAD SUB

        - Line 42, 9 ``balanceOf[_from] -= _value``
        - Line 53, 9 ``allowed[_from][msg.sender] -= _value``
        - Line 71, 9 ``balanceOf[msg.sender] -= _value``
        - Line 72, 9 ``totalSupply -= _value``

    - 31%, PUSH REVERT

        - Line 3, 49 ``v``

* _`X`_ Overflow
    - 50%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 62, 5 ``function approveAndCall(address _spender, uint _value, bytes _extraData) public returns(bool) {
        tokenRecipient spender = tokenRecipient(_spender);
        if(approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 50%, PUSH DUP DUP SLOAD ADD

        - Line 24, 9 ``lockTime_intou37[msg.sender]``
        - Line 43, 9 ``balanceOf[_to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 27, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
