# Vulnerability Analysis #
#### 2023-06-05 08:58:19 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 12, 5 ``string public question``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 5, 5 ``function Try(string _response) external payable {
        require(msg.sender == tx.origin);
        if(responseHash == keccak256(_response) && msg.value>3 ether)
        {
            msg.sender.transfer(this.balance);
        }
    }``
        - Line 15, 5 ``function set_game(string _question,string _response) public payable {
        if(responseHash==0x0) 
        {
            responseHash = keccak256(_response);
            question = _question;
            questionSender = msg.sender;
        }
    }``
        - Line 27, 5 ``function NewQuestion(string _question, bytes32 _responseHash) public payable {
        if(msg.sender==questionSender){
            question = _question;
            responseHash = _responseHash;
        }
    }``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, PUSH MUL PUSH SLOAD PUSH

        - Line 16, 12 ``responseHash==0x0``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
    - 100%, ORIGIN

        - Line 6, 31 ``tx.origin``

* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 9, 13 ``msg.sender.transfer(this.balance)``
        - Line 25, 9 ``msg.sender.transfer(this.balance)``

* __O__ BlockHash
* __O__ SelfDestruct
