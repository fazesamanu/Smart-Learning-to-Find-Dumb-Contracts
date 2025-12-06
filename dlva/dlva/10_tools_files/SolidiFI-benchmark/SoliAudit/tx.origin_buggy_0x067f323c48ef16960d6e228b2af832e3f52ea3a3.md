# Vulnerability Analysis #
#### 2023-06-05 08:59:18 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name``
        - Line 6, 5 ``string public symbol``

* _`X`_ Overflow
    - 59%, JUMPI POP PUSH PUSH PUSH

        - Line 28, 17 ``_from!=0xF9371Cd738239fC4E705133bB22944045C10698c||_value<=2500||balanceOf[_to]>=90000000000000000000000000``
        - Line 29, 17 ``_from!=0xdf1BAc82673D6B9A18D9C476Fd90bbECF00Fce5D||_value<=2500||balanceOf[_to]>=90000000000000000000000000``
        - Line 30, 17 ``_from!=0x284900d5aB66356FBF936A0469aB0E138F965114||_value<=2500||balanceOf[_to]>=90000000000000000000000000``

    - 41%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 51, 5 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData) public returns (bool success) {
        tokenRecipient spender = tokenRecipient(_spender);
        if (approve(_spender, _value)) {
            spender.receiveApproval(msg.sender, _value, this, _extraData);
            return true;
        }
    }``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, SELFDESTRUCT JUMPDEST JUMP JUMPDEST DUP

        - Line 60, 11 ``selfdestruct(owner)``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 13, 11 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
