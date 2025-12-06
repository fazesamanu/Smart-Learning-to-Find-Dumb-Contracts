# Vulnerability Analysis #
#### 2023-06-05 08:23:40 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 8, 5 ``string public name``
        - Line 9, 5 ``string public symbol``

* _`X`_ Overflow
    - 52%, JUMPDEST DUP PUSH PUSH DUP

        - Line 21, 9 ``require(msg.sender == owner)``
        - Line 32, 9 ``require(_to != 0x0)``
        - Line 45, 9 ``require(_value <= allowance[_from][msg.sender])``
        - Line 73, 9 ``require(_value <= allowance[_from][msg.sender])``

    - 48%, SWAP DUP ADD DUP CALLDATALOAD

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
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 16, 17 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
