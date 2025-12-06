# Vulnerability Analysis #
#### 2023-06-05 08:52:15 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 7, 5 ``string public name="Duchening"``
        - Line 8, 5 ``string public symbol="Bimah"``

* _`X`_ Overflow
    - 54%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 43, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
    public
    returns(bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 46%, SWAP SWAP SWAP SWAP SWAP

        - Line 43, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
    public
    returns(bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

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

        - Line 55, 17 ``now``
        - Line 56, 34 ``now``
        - Line 57, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
