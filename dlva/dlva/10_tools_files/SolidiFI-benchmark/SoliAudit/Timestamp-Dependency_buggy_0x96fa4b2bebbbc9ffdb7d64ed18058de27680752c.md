# Vulnerability Analysis #
#### 2023-06-05 08:52:52 ####

* _`X`_ Underflow
    - 100%, NOT DUP

        - Line 11, 5 ``    }
   ``

* _`X`_ Overflow
    - 100%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 8, 5 ``function Answer(string _response) public payable {
        if (responseHash == keccak256(_response) && msg.value>1 ether) {
            msg.sender.transfer(this.balance);
        }
    }``
        - Line 13, 5 ``function StartGame(string _question,string _response) public payable {
        if (responseHash==0x0) {
            responseHash = keccak256(_response);
            question = _question;
            questionSender = msg.sender;
        }
    }``
        - Line 25, 5 ``function NewQuestion(string _question, bytes32 _responseHash) public payable {
        if (msg.sender==questionSender) {
            question = _question;
            responseHash = _responseHash;
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

        - Line 33, 34 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
