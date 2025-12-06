# Vulnerability Analysis #
#### 2023-06-05 08:43:30 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 6, 5 ``string public name='DAO'``
        - Line 7, 5 ``string public symbol='DAO'``

* _`X`_ Overflow
    - 54%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 55, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
        public
        returns (bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 46%, SWAP SWAP SWAP SWAP SWAP

        - Line 55, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
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
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 17, 17 ``msg.sender.call.value(_weiToWithdraw)("")``
        - Line 60, 13 ``spender.receiveApproval(msg.sender, _value, this, _extraData)``

* __O__ BlockHash
* __O__ SelfDestruct
