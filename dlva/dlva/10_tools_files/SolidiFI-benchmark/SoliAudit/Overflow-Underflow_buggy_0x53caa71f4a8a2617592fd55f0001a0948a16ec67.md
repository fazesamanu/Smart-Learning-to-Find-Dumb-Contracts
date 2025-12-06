# Vulnerability Analysis #
#### 2023-06-05 08:50:06 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = 'TOAB'``
        - Line 6, 5 ``string public symbol = 'TOAB'``

* _`X`_ Overflow
    - 50%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 46, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData) public returns (bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 50%, PUSH DUP DUP SLOAD ADD

        - Line 16, 5 ``balances_intou26[_to]``
        - Line 29, 9 ``balanceOf[_to]``

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
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
