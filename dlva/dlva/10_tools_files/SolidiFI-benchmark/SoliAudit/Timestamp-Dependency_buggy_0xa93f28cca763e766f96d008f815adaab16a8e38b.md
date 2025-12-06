# Vulnerability Analysis #
#### 2023-06-05 08:44:36 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name="Levblockchain"``
        - Line 6, 5 ``string public symbol="LVE"``

* _`X`_ Overflow
    - 54%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 61, 9 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
        public
        returns (bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 46%, SWAP SWAP SWAP SWAP SWAP

        - Line 61, 9 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
        public
        returns (bool success) {
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

        - Line 15, 17 ``now``
        - Line 16, 34 ``now``
        - Line 17, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
