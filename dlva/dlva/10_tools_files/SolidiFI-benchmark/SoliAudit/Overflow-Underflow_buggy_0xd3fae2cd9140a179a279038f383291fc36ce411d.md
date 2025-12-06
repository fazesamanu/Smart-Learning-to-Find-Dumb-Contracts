# Vulnerability Analysis #
#### 2023-06-05 08:59:40 ####

* _`X`_ Underflow
    - 100%, NOT DUP

        - Line 18, 2 ``         ``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 85, 5 ``function updateWinnerBid(
        bool _isAskBid,
        bytes _bidder,
        uint256 _bidValue,
        bytes _previousBidHash,
        bytes _signatureAssistant,
        bytes _signatureAuctioneer
    ) 
        external
    {
        tryClose();
        require(phase != PHASE_CLOSED);
        require(!_isAskBid);
        require(_bidValue > winnerBidValue);
        require(_bidValue >= minBidValue);
        bytes32 _fingerprint = keccak256(
            abi.encodePacked(
                "auctionBid",
                _isAskBid,
                _bidder,
                _bidValue,
                _previousBidHash
            )
        );
        _fingerprint = ECRecovery.toEthSignedMessageHash(_fingerprint);
        require(auctioneer == ECRecovery.recover(_fingerprint, _signatureAuctioneer));
        require(assistant == ECRecovery.recover(_fingerprint, _signatureAssistant));
        winnerBidder = _bidder;
        winnerBidValue = _bidValue;
        closingBlock = block.number + challengePeriod;
        phase = PHASE_CHALLENGE;  
    }``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, DUP DUP SUB SUB DUP

        - Line 4, 13 ``covery ``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, JUMPDEST PUSH AND PUSH DUP

        - Line 110, 31 ``ECRecovery.recover(_fingerprint, _signatureAuctioneer)``

* _`X`_ InlineAssembly
    - 100%, DUP ADD MLOAD SWAP POP

        - Line 18, 28 ``sig``
        - Line 19, 28 ``sig``

* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
