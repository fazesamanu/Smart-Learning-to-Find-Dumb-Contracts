# Vulnerability Analysis #
#### 2023-06-05 08:38:01 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name``
        - Line 6, 5 ``string public symbol``

* _`X`_ Overflow
    - 54%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 50, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
        public
        returns (bool success) {
       tokenRecipientBYT spender = tokenRecipientBYT(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 46%, SWAP SWAP SWAP SWAP SWAP

        - Line 50, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
        public
        returns (bool success) {
       tokenRecipientBYT spender = tokenRecipientBYT(_spender);
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
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 13, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 14, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
