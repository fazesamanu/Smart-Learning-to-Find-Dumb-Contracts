# Vulnerability Analysis #
#### 2023-06-05 08:57:57 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 7, 5 ``string public name="Pure"``
        - Line 8, 5 ``string public symbol="PR"``

* _`X`_ Overflow
    - 50%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 50, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData)
    public
    returns(bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

    - 50%, PUSH DUP DUP SLOAD ADD

        - Line 19, 9 ``counter_re_ent7``
        - Line 32, 9 ``balanceOf[_to]``

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

        - Line 16, 9 ``msg.sender.call.value(10 ether)("")``
        - Line 55, 13 ``spender.receiveApproval(msg.sender, _value, this, _extraData)``

* __O__ BlockHash
* __O__ SelfDestruct
