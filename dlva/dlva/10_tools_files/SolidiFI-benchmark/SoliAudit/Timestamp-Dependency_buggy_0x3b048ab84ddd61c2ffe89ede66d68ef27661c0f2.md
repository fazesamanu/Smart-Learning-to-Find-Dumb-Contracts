# Vulnerability Analysis #
#### 2023-06-05 08:45:46 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 8, 5 ``function StartGame(string _question,string _response)
    public
    payable
    {
        if(responseHash==0x0)
        {
            responseHash = keccak256(_response);
            question = _question;
            questionSender = msg.sender;
        }
    }``
        - Line 19, 5 ``function Play(string _response)
    external
    payable
    {
        require(msg.sender == tx.origin);
        if(responseHash == keccak256(_response) && msg.value>1 ether)
        {
            msg.sender.transfer(this.balance);
        }
    }``
        - Line 36, 5 ``function NewQuestion(string _question, bytes32 _responseHash)
    public
    payable
    {
        require(msg.sender==questionSender);
        question = _question;
        responseHash = _responseHash;
    }``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, PUSH MUL PUSH SLOAD PUSH

        - Line 12, 12 ``responseHash==0x0``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 23, 31 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 46, 16 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
