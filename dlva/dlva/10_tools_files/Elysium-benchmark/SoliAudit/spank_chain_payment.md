# Vulnerability Analysis #
#### 2023-05-29 11:47:39 ####

* _`X`_ Underflow
    - 39%, PUSH NOT

        - Line 16, 6 ``function recoverSigner(bytes32 _hashedMsg, string _sig) public pure returns (address) {
         require(_hashedMsg != 0x00);
         bytes memory prefix = "\x19Ethereum Signed Message:\n32";
         bytes32 prefixedHash = keccak256(abi.encodePacked(prefix, _hashedMsg));
         if (bytes(_sig).length != 132) {
             return 0x0;
         }
         bytes32 r;
         bytes32 s;
         uint8 v;
         bytes memory sig = hexstrToBytes(substring(_sig, 2, 132));
         assembly {
             r := mload(add(sig, 32))
             s := mload(add(sig, 64))
             v := byte(0, mload(add(sig, 96)))
         }
         if (v < 27) {
             v += 27;
         }
         if (v < 27 || v > 28) {
             return 0x0;
         }
         return ecrecover(prefixedHash, v, r, s);
     }``
        - Line 17, 18 ``_hashedMsg != 0x00``
        - Line 19, 43 ``abi.encodePacked(prefix, _hashedMsg)``
        - Line 38, 17 ``ecrecover(prefixedHash, v, r, s)``
        - Line 40, 6 ``function isSignedBy(bytes32 _hashedMsg, string _sig, address _addr) public pure returns (bool) {
         require(_addr != 0x0);
         return _addr == recoverSigner(_hashedMsg, _sig);
     }``
        - Line 47, 36 ``new string(len / 2)``
        - Line 55, 14 ``bstr[k++] = uintToBytes32(p)[31]``
        - Line 61, 15 ``bresult[0] >= 48``
        - Line 61, 37 ``bresult[0] <= 57``
        - Line 63, 22 ``bresult[0] >= 65``
        - Line 63, 44 ``bresult[0] <= 70``
        - Line 65, 22 ``bresult[0] >= 97``
        - Line 65, 44 ``bresult[0] <= 102``
        - Line 72, 14 ``new bytes(32)``
        - Line 75, 6 ``function toEthereumSignedMessage(string _msg) public pure returns (bytes32) {
         uint len = bytes(_msg).length;
         require(len > 0);
         bytes memory prefix = "\x19Ethereum Signed Message:\n";
         return keccak256(abi.encodePacked(prefix, uintToString(len), _msg));
     }``
        - Line 88, 27 ``new bytes(len)``
        - Line 93, 14 ``b[i--] = byte(48 + remainder)``
        - Line 102, 32 ``new bytes(_endIndex - _startIndex)``
        - Line 104, 14 ``result[i - _startIndex] = strBytes[i]``
        - Line 263, 6 ``mapping(bytes32 => VirtualChannel) public virtualChannels``
        - Line 264, 6 ``mapping(bytes32 => Channel) public Channels``
        - Line 265, 6 ``function createChannel(
         bytes32 _lcID,
         address _partyI,
         uint256 _confirmTime,
         address _token,
         uint256[2] _balances
     )
         public
         payable
     {
         require(Channels[_lcID].partyAddresses[0] == address(0), "Channel has already been created.");
         require(_partyI != 0x0, "No partyI address provided to LC creation");
         require(_balances[0] >= 0 && _balances[1] >= 0, "Balances cannot be negative");
         Channels[_lcID].partyAddresses[0] = msg.sender;
         Channels[_lcID].partyAddresses[1] = _partyI;
         if(_balances[0] != 0) {
             require(msg.value == _balances[0], "Eth balance does not match sent value");
             Channels[_lcID].ethBalances[0] = msg.value;
         }
         if(_balances[1] != 0) {
             Channels[_lcID].token = HumanStandardToken(_token);
             require(Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1]),"CreateChannel: token transfer failure");
             Channels[_lcID].erc20Balances[0] = _balances[1];
         }
         Channels[_lcID].sequence = 0;
         Channels[_lcID].confirmTime = _confirmTime;
         Channels[_lcID].LCopenTimeout = now + _confirmTime;
         Channels[_lcID].initialDeposit = _balances;
         emit DidLCOpen(_lcID, msg.sender, _partyI, _balances[0], _token, _balances[1], Channels[_lcID].LCopenTimeout);
     }``
        - Line 275, 18 ``Channels[_lcID]``
        - Line 278, 10 ``Channels[_lcID]``
        - Line 279, 10 ``Channels[_lcID]``
        - Line 282, 14 ``Channels[_lcID]``
        - Line 285, 14 ``Channels[_lcID]``
        - Line 286, 22 ``Channels[_lcID]``
        - Line 287, 14 ``Channels[_lcID]``
        - Line 289, 10 ``Channels[_lcID]``
        - Line 290, 10 ``Channels[_lcID]``
        - Line 291, 10 ``Channels[_lcID]``
        - Line 292, 10 ``Channels[_lcID]``
        - Line 293, 15 ``DidLCOpen(_lcID, msg.sender, _partyI, _balances[0], _token, _balances[1], Channels[_lcID].LCopenTimeout)``
        - Line 293, 89 ``Channels[_lcID]``
        - Line 295, 6 ``function LCOpenTimeout(bytes32 _lcID) public {
         require(msg.sender == Channels[_lcID].partyAddresses[0] && Channels[_lcID].isOpen == false);
         require(now > Channels[_lcID].LCopenTimeout);
         if(Channels[_lcID].initialDeposit[0] != 0) {
             Channels[_lcID].partyAddresses[0].transfer(Channels[_lcID].ethBalances[0]);
         }
         if(Channels[_lcID].initialDeposit[1] != 0) {
             require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], Channels[_lcID].erc20Balances[0]),"CreateChannel: token transfer failure");
         }
         emit DidLCClose(_lcID, 0, Channels[_lcID].ethBalances[0], Channels[_lcID].erc20Balances[0], 0, 0);
         delete Channels[_lcID];
     }``
        - Line 296, 32 ``Channels[_lcID]``
        - Line 296, 69 ``Channels[_lcID]``
        - Line 297, 24 ``Channels[_lcID]``
        - Line 298, 13 ``Channels[_lcID]``
        - Line 299, 14 ``Channels[_lcID]``
        - Line 299, 57 ``Channels[_lcID]``
        - Line 301, 13 ``Channels[_lcID]``
        - Line 302, 22 ``Channels[_lcID]``
        - Line 302, 53 ``Channels[_lcID]``
        - Line 302, 88 ``Channels[_lcID]``
        - Line 304, 15 ``DidLCClose(_lcID, 0, Channels[_lcID].ethBalances[0], Channels[_lcID].erc20Balances[0], 0, 0)``
        - Line 304, 36 ``Channels[_lcID]``
        - Line 304, 68 ``Channels[_lcID]``
        - Line 305, 17 ``Channels[_lcID]``
        - Line 307, 6 ``function joinChannel(bytes32 _lcID, uint256[2] _balances) public payable {
         require(Channels[_lcID].isOpen == false);
         require(msg.sender == Channels[_lcID].partyAddresses[1]);
         if(_balances[0] != 0) {
             require(msg.value == _balances[0], "state balance does not match sent value");
             Channels[_lcID].ethBalances[1] = msg.value;
         }
         if(_balances[1] != 0) {
             require(Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1]),"joinChannel: token transfer failure");
             Channels[_lcID].erc20Balances[1] = _balances[1];
         }
         Channels[_lcID].initialDeposit[0]+=_balances[0];
         Channels[_lcID].initialDeposit[1]+=_balances[1];
         Channels[_lcID].isOpen = true;
         numChannels++;
         emit DidLCJoin(_lcID, _balances[0], _balances[1]);
     }``
        - Line 308, 18 ``Channels[_lcID]``
        - Line 309, 32 ``Channels[_lcID]``
        - Line 312, 14 ``Channels[_lcID]``
        - Line 315, 22 ``Channels[_lcID]``
        - Line 316, 14 ``Channels[_lcID]``
        - Line 318, 10 ``Channels[_lcID]``
        - Line 319, 10 ``Channels[_lcID]``
        - Line 320, 10 ``Channels[_lcID]``
        - Line 322, 15 ``DidLCJoin(_lcID, _balances[0], _balances[1])``
        - Line 324, 6 ``function deposit(bytes32 _lcID, address recipient, uint256 _balance, bool isToken) public payable {
         require(Channels[_lcID].isOpen == true, "Tried adding funds to a closed channel");
         require(recipient == Channels[_lcID].partyAddresses[0] || recipient == Channels[_lcID].partyAddresses[1]);
         if (Channels[_lcID].partyAddresses[0] == recipient) {
             if(isToken) {
                 require(Channels[_lcID].token.transferFrom(msg.sender, this, _balance),"deposit: token transfer failure");
                 Channels[_lcID].erc20Balances[2] += _balance;
             } else {
                 require(msg.value == _balance, "state balance does not match sent value");
                 Channels[_lcID].ethBalances[2] += msg.value;
             }
         }
         if (Channels[_lcID].partyAddresses[1] == recipient) {
             if(isToken) {
                 require(Channels[_lcID].token.transferFrom(msg.sender, this, _balance),"deposit: token transfer failure");
                 Channels[_lcID].erc20Balances[3] += _balance;
             } else {
                 require(msg.value == _balance, "state balance does not match sent value");
                 Channels[_lcID].ethBalances[3] += msg.value;
             }
         }
         emit DidLCDeposit(_lcID, recipient, _balance, isToken);
     }``
        - Line 325, 18 ``Channels[_lcID]``
        - Line 326, 31 ``Channels[_lcID]``
        - Line 326, 81 ``Channels[_lcID]``
        - Line 327, 14 ``Channels[_lcID]``
        - Line 329, 26 ``Channels[_lcID]``
        - Line 330, 18 ``Channels[_lcID]``
        - Line 333, 18 ``Channels[_lcID]``
        - Line 336, 14 ``Channels[_lcID]``
        - Line 338, 26 ``Channels[_lcID]``
        - Line 339, 18 ``Channels[_lcID]``
        - Line 342, 18 ``Channels[_lcID]``
        - Line 345, 15 ``DidLCDeposit(_lcID, recipient, _balance, isToken)``
        - Line 347, 6 ``function consensusCloseChannel(
         bytes32 _lcID,
         uint256 _sequence,
         uint256[4] _balances,
         string _sigA,
         string _sigI
     )
         public
     {
         require(Channels[_lcID].isOpen == true);
         uint256 totalEthDeposit = Channels[_lcID].initialDeposit[0] + Channels[_lcID].ethBalances[2] + Channels[_lcID].ethBalances[3];
         uint256 totalTokenDeposit = Channels[_lcID].initialDeposit[1] + Channels[_lcID].erc20Balances[2] + Channels[_lcID].erc20Balances[3];
         require(totalEthDeposit == _balances[0] + _balances[1]);
         require(totalTokenDeposit == _balances[2] + _balances[3]);
         bytes32 _state = keccak256(
             abi.encodePacked(
                 _lcID,
                 true,
                 _sequence,
                 uint256(0),
                 bytes32(0x0),
                 Channels[_lcID].partyAddresses[0],
                 Channels[_lcID].partyAddresses[1],
                 _balances[0],
                 _balances[1],
                 _balances[2],
                 _balances[3]
             )
         );
         require(Channels[_lcID].partyAddresses[0] == ECTools.recoverSigner(_state, _sigA));
         require(Channels[_lcID].partyAddresses[1] == ECTools.recoverSigner(_state, _sigI));
         Channels[_lcID].isOpen = false;
         if(_balances[0] != 0 || _balances[1] != 0) {
             Channels[_lcID].partyAddresses[0].transfer(_balances[0]);
             Channels[_lcID].partyAddresses[1].transfer(_balances[1]);
         }
         if(_balances[2] != 0 || _balances[3] != 0) {
             require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], _balances[2]),"happyCloseChannel: token transfer failure");
             require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[1], _balances[3]),"happyCloseChannel: token transfer failure");
         }
         numChannels--;
         emit DidLCClose(_lcID, _sequence, _balances[0], _balances[1], _balances[2], _balances[3]);
     }``
        - Line 356, 18 ``Channels[_lcID]``
        - Line 357, 36 ``Channels[_lcID]``
        - Line 357, 72 ``Channels[_lcID]``
        - Line 357, 105 ``Channels[_lcID]``
        - Line 358, 38 ``Channels[_lcID]``
        - Line 358, 74 ``Channels[_lcID]``
        - Line 358, 109 ``Channels[_lcID]``
        - Line 362, 14 ``abi.encodePacked(
                 _lcID,
                 true,
                 _sequence,
                 uint256(0),
                 bytes32(0x0),
                 Channels[_lcID].partyAddresses[0],
                 Channels[_lcID].partyAddresses[1],
                 _balances[0],
                 _balances[1],
                 _balances[2],
                 _balances[3]
             )``
        - Line 368, 18 ``Channels[_lcID]``
        - Line 369, 18 ``Channels[_lcID]``
        - Line 376, 18 ``Channels[_lcID]``
        - Line 376, 55 ``ECTools.recoverSigner(_state, _sigA)``
        - Line 377, 18 ``Channels[_lcID]``
        - Line 377, 55 ``ECTools.recoverSigner(_state, _sigI)``
        - Line 378, 10 ``Channels[_lcID]``
        - Line 380, 14 ``Channels[_lcID]``
        - Line 381, 14 ``Channels[_lcID]``
        - Line 384, 22 ``Channels[_lcID]``
        - Line 384, 53 ``Channels[_lcID]``
        - Line 385, 22 ``Channels[_lcID]``
        - Line 385, 53 ``Channels[_lcID]``
        - Line 388, 15 ``DidLCClose(_lcID, _sequence, _balances[0], _balances[1], _balances[2], _balances[3])``
        - Line 390, 6 ``function updateLCstate(
         bytes32 _lcID,
         uint256[6] updateParams,
         bytes32 _VCroot,
         string _sigA,
         string _sigI
     )
         public
     {
         Channel storage channel = Channels[_lcID];
         require(channel.isOpen);
         require(channel.sequence < updateParams[0]);
         require(channel.ethBalances[0] + channel.ethBalances[1] >= updateParams[2] + updateParams[3]);
         require(channel.erc20Balances[0] + channel.erc20Balances[1] >= updateParams[4] + updateParams[5]);
         if(channel.isUpdateLCSettling == true) {
             require(channel.updateLCtimeout > now);
         }
         bytes32 _state = keccak256(
             abi.encodePacked(
                 _lcID,
                 false,
                 updateParams[0],
                 updateParams[1],
                 _VCroot,
                 channel.partyAddresses[0],
                 channel.partyAddresses[1],
                 updateParams[2],
                 updateParams[3],
                 updateParams[4],
                 updateParams[5]
             )
         );
         require(channel.partyAddresses[0] == ECTools.recoverSigner(_state, _sigA));
         require(channel.partyAddresses[1] == ECTools.recoverSigner(_state, _sigI));
         channel.sequence = updateParams[0];
         channel.numOpenVC = updateParams[1];
         channel.ethBalances[0] = updateParams[2];
         channel.ethBalances[1] = updateParams[3];
         channel.erc20Balances[0] = updateParams[4];
         channel.erc20Balances[1] = updateParams[5];
         channel.VCrootHash = _VCroot;
         channel.isUpdateLCSettling = true;
         channel.updateLCtimeout = now + channel.confirmTime;
         emit DidLCUpdateState (
             _lcID,
             updateParams[0],
             updateParams[1],
             updateParams[2],
             updateParams[3],
             updateParams[4],
             updateParams[5],
             _VCroot,
             channel.updateLCtimeout
         );
     }``
        - Line 399, 36 ``Channels[_lcID]``
        - Line 408, 14 ``abi.encodePacked(
                 _lcID,
                 false,
                 updateParams[0],
                 updateParams[1],
                 _VCroot,
                 channel.partyAddresses[0],
                 channel.partyAddresses[1],
                 updateParams[2],
                 updateParams[3],
                 updateParams[4],
                 updateParams[5]
             )``
        - Line 422, 47 ``ECTools.recoverSigner(_state, _sigA)``
        - Line 423, 47 ``ECTools.recoverSigner(_state, _sigI)``
        - Line 430, 10 ``channel.VCrootHash = _VCroot``
        - Line 433, 15 ``DidLCUpdateState (
             _lcID,
             updateParams[0],
             updateParams[1],
             updateParams[2],
             updateParams[3],
             updateParams[4],
             updateParams[5],
             _VCroot,
             channel.updateLCtimeout
         )``
        - Line 445, 6 ``function initVCstate(
         bytes32 _lcID,
         bytes32 _vcID,
         bytes _proof,
         address _partyA,
         address _partyB,
         uint256[2] _bond,
         uint256[4] _balances,
         string sigA
     )
         public
     {
         require(Channels[_lcID].isOpen, "LC is closed.");
         require(!virtualChannels[_vcID].isClose, "VC is closed.");
         require(Channels[_lcID].updateLCtimeout < now, "LC timeout not over.");
         require(virtualChannels[_vcID].updateVCtimeout == 0);
         bytes32 _initState = keccak256(
             abi.encodePacked(_vcID, uint256(0), _partyA, _partyB, _bond[0], _bond[1], _balances[0], _balances[1], _balances[2], _balances[3])
         );
         require(_partyA == ECTools.recoverSigner(_initState, sigA));
         require(_isContained(_initState, _proof, Channels[_lcID].VCrootHash) == true);
         virtualChannels[_vcID].partyA = _partyA;
         virtualChannels[_vcID].partyB = _partyB;
         virtualChannels[_vcID].sequence = uint256(0);
         virtualChannels[_vcID].ethBalances[0] = _balances[0];
         virtualChannels[_vcID].ethBalances[1] = _balances[1];
         virtualChannels[_vcID].erc20Balances[0] = _balances[2];
         virtualChannels[_vcID].erc20Balances[1] = _balances[3];
         virtualChannels[_vcID].bond = _bond;
         virtualChannels[_vcID].updateVCtimeout = now + Channels[_lcID].confirmTime;
         virtualChannels[_vcID].isInSettlementState = true;
         emit DidVCInit(_lcID, _vcID, _proof, uint256(0), _partyA, _partyB, _balances[0], _balances[1]);
     }``
        - Line 457, 18 ``Channels[_lcID]``
        - Line 458, 19 ``virtualChannels[_vcID]``
        - Line 459, 18 ``Channels[_lcID]``
        - Line 460, 18 ``virtualChannels[_vcID]``
        - Line 462, 14 ``abi.encodePacked(_vcID, uint256(0), _partyA, _partyB, _bond[0], _bond[1], _balances[0], _balances[1], _balances[2], _balances[3])``
        - Line 464, 29 ``ECTools.recoverSigner(_initState, sigA)``
        - Line 465, 51 ``Channels[_lcID]``
        - Line 466, 10 ``virtualChannels[_vcID]``
        - Line 467, 10 ``virtualChannels[_vcID]``
        - Line 468, 10 ``virtualChannels[_vcID]``
        - Line 469, 10 ``virtualChannels[_vcID]``
        - Line 470, 10 ``virtualChannels[_vcID]``
        - Line 471, 10 ``virtualChannels[_vcID]``
        - Line 472, 10 ``virtualChannels[_vcID]``
        - Line 473, 10 ``virtualChannels[_vcID]``
        - Line 474, 10 ``virtualChannels[_vcID]``
        - Line 474, 57 ``Channels[_lcID]``
        - Line 475, 10 ``virtualChannels[_vcID]``
        - Line 476, 15 ``DidVCInit(_lcID, _vcID, _proof, uint256(0), _partyA, _partyB, _balances[0], _balances[1])``
        - Line 478, 6 ``function settleVC(
         bytes32 _lcID,
         bytes32 _vcID,
         uint256 updateSeq,
         address _partyA,
         address _partyB,
         uint256[4] updateBal,
         string sigA
     )
         public
     {
         require(Channels[_lcID].isOpen, "LC is closed.");
         require(!virtualChannels[_vcID].isClose, "VC is closed.");
         require(virtualChannels[_vcID].sequence < updateSeq, "VC sequence is higher than update sequence.");
         require(
             virtualChannels[_vcID].ethBalances[1] < updateBal[1] && virtualChannels[_vcID].erc20Balances[1] < updateBal[3],
             "State updates may only increase recipient balance."
         );
         require(
             virtualChannels[_vcID].bond[0] == updateBal[0] + updateBal[1] &&
             virtualChannels[_vcID].bond[1] == updateBal[2] + updateBal[3],
             "Incorrect balances for bonded amount");
         require(Channels[_lcID].updateLCtimeout < now);
         bytes32 _updateState = keccak256(
             abi.encodePacked(
                 _vcID,
                 updateSeq,
                 _partyA,
                 _partyB,
                 virtualChannels[_vcID].bond[0],
                 virtualChannels[_vcID].bond[1],
                 updateBal[0],
                 updateBal[1],
                 updateBal[2],
                 updateBal[3]
             )
         );
         require(virtualChannels[_vcID].partyA == ECTools.recoverSigner(_updateState, sigA));
         virtualChannels[_vcID].challenger = msg.sender;
         virtualChannels[_vcID].sequence = updateSeq;
         virtualChannels[_vcID].ethBalances[0] = updateBal[0];
         virtualChannels[_vcID].ethBalances[1] = updateBal[1];
         virtualChannels[_vcID].erc20Balances[0] = updateBal[2];
         virtualChannels[_vcID].erc20Balances[1] = updateBal[3];
         virtualChannels[_vcID].updateVCtimeout = now + Channels[_lcID].confirmTime;
         emit DidVCSettle(_lcID, _vcID, updateSeq, updateBal[0], updateBal[1], msg.sender, virtualChannels[_vcID].updateVCtimeout);
     }``
        - Line 489, 18 ``Channels[_lcID]``
        - Line 490, 19 ``virtualChannels[_vcID]``
        - Line 491, 18 ``virtualChannels[_vcID]``
        - Line 493, 14 ``virtualChannels[_vcID]``
        - Line 493, 70 ``virtualChannels[_vcID]``
        - Line 497, 14 ``virtualChannels[_vcID]``
        - Line 498, 14 ``virtualChannels[_vcID]``
        - Line 500, 18 ``Channels[_lcID]``
        - Line 502, 14 ``abi.encodePacked(
                 _vcID,
                 updateSeq,
                 _partyA,
                 _partyB,
                 virtualChannels[_vcID].bond[0],
                 virtualChannels[_vcID].bond[1],
                 updateBal[0],
                 updateBal[1],
                 updateBal[2],
                 updateBal[3]
             )``
        - Line 507, 18 ``virtualChannels[_vcID]``
        - Line 508, 18 ``virtualChannels[_vcID]``
        - Line 515, 18 ``virtualChannels[_vcID]``
        - Line 515, 51 ``ECTools.recoverSigner(_updateState, sigA)``
        - Line 516, 10 ``virtualChannels[_vcID]``
        - Line 517, 10 ``virtualChannels[_vcID]``
        - Line 518, 10 ``virtualChannels[_vcID]``
        - Line 519, 10 ``virtualChannels[_vcID]``
        - Line 520, 10 ``virtualChannels[_vcID]``
        - Line 521, 10 ``virtualChannels[_vcID]``
        - Line 522, 10 ``virtualChannels[_vcID]``
        - Line 522, 57 ``Channels[_lcID]``
        - Line 523, 15 ``DidVCSettle(_lcID, _vcID, updateSeq, updateBal[0], updateBal[1], msg.sender, virtualChannels[_vcID].updateVCtimeout)``
        - Line 523, 92 ``virtualChannels[_vcID]``
        - Line 525, 6 ``function closeVirtualChannel(bytes32 _lcID, bytes32 _vcID) public {
         require(Channels[_lcID].isOpen, "LC is closed.");
         require(virtualChannels[_vcID].isInSettlementState, "VC is not in settlement state.");
         require(virtualChannels[_vcID].updateVCtimeout < now, "Update vc timeout has not elapsed.");
         require(!virtualChannels[_vcID].isClose, "VC is already closed");
         Channels[_lcID].numOpenVC--;
         virtualChannels[_vcID].isClose = true;
         if(virtualChannels[_vcID].partyA == Channels[_lcID].partyAddresses[0]) {
             Channels[_lcID].ethBalances[0] += virtualChannels[_vcID].ethBalances[0];
             Channels[_lcID].ethBalances[1] += virtualChannels[_vcID].ethBalances[1];
             Channels[_lcID].erc20Balances[0] += virtualChannels[_vcID].erc20Balances[0];
             Channels[_lcID].erc20Balances[1] += virtualChannels[_vcID].erc20Balances[1];
         } else if (virtualChannels[_vcID].partyB == Channels[_lcID].partyAddresses[0]) {
             Channels[_lcID].ethBalances[0] += virtualChannels[_vcID].ethBalances[1];
             Channels[_lcID].ethBalances[1] += virtualChannels[_vcID].ethBalances[0];
             Channels[_lcID].erc20Balances[0] += virtualChannels[_vcID].erc20Balances[1];
             Channels[_lcID].erc20Balances[1] += virtualChannels[_vcID].erc20Balances[0];
         }
         emit DidVCClose(_lcID, _vcID, virtualChannels[_vcID].erc20Balances[0], virtualChannels[_vcID].erc20Balances[1]);
     }``
        - Line 526, 18 ``Channels[_lcID]``
        - Line 527, 18 ``virtualChannels[_vcID]``
        - Line 528, 18 ``virtualChannels[_vcID]``
        - Line 529, 19 ``virtualChannels[_vcID]``
        - Line 530, 10 ``Channels[_lcID]``
        - Line 531, 10 ``virtualChannels[_vcID]``
        - Line 532, 13 ``virtualChannels[_vcID]``
        - Line 532, 46 ``Channels[_lcID]``
        - Line 533, 14 ``Channels[_lcID]``
        - Line 533, 48 ``virtualChannels[_vcID]``
        - Line 534, 14 ``Channels[_lcID]``
        - Line 534, 48 ``virtualChannels[_vcID]``
        - Line 535, 14 ``Channels[_lcID]``
        - Line 535, 50 ``virtualChannels[_vcID]``
        - Line 536, 14 ``Channels[_lcID]``
        - Line 536, 50 ``virtualChannels[_vcID]``
        - Line 537, 21 ``virtualChannels[_vcID]``
        - Line 537, 54 ``Channels[_lcID]``
        - Line 538, 14 ``Channels[_lcID]``
        - Line 538, 48 ``virtualChannels[_vcID]``
        - Line 539, 14 ``Channels[_lcID]``
        - Line 539, 48 ``virtualChannels[_vcID]``
        - Line 540, 14 ``Channels[_lcID]``
        - Line 540, 50 ``virtualChannels[_vcID]``
        - Line 541, 14 ``Channels[_lcID]``
        - Line 541, 50 ``virtualChannels[_vcID]``
        - Line 543, 15 ``DidVCClose(_lcID, _vcID, virtualChannels[_vcID].erc20Balances[0], virtualChannels[_vcID].erc20Balances[1])``
        - Line 543, 40 ``virtualChannels[_vcID]``
        - Line 543, 81 ``virtualChannels[_vcID]``
        - Line 545, 6 ``function byzantineCloseChannel(bytes32 _lcID) public {
         Channel storage channel = Channels[_lcID];
         require(channel.isOpen, "Channel is not open");
         require(channel.isUpdateLCSettling == true);
         require(channel.numOpenVC == 0);
         require(channel.updateLCtimeout < now, "LC timeout over.");
         uint256 totalEthDeposit = channel.initialDeposit[0] + channel.ethBalances[2] + channel.ethBalances[3];
         uint256 totalTokenDeposit = channel.initialDeposit[1] + channel.erc20Balances[2] + channel.erc20Balances[3];
         uint256 possibleTotalEthBeforeDeposit = channel.ethBalances[0] + channel.ethBalances[1];
         uint256 possibleTotalTokenBeforeDeposit = channel.erc20Balances[0] + channel.erc20Balances[1];
         if(possibleTotalEthBeforeDeposit < totalEthDeposit) {
             channel.ethBalances[0]+=channel.ethBalances[2];
             channel.ethBalances[1]+=channel.ethBalances[3];
         } else {
             require(possibleTotalEthBeforeDeposit == totalEthDeposit);
         }
         if(possibleTotalTokenBeforeDeposit < totalTokenDeposit) {
             channel.erc20Balances[0]+=channel.erc20Balances[2];
             channel.erc20Balances[1]+=channel.erc20Balances[3];
         } else {
             require(possibleTotalTokenBeforeDeposit == totalTokenDeposit);
         }
         uint256 ethbalanceA = channel.ethBalances[0];
         uint256 ethbalanceI = channel.ethBalances[1];
         uint256 tokenbalanceA = channel.erc20Balances[0];
         uint256 tokenbalanceI = channel.erc20Balances[1];
         channel.ethBalances[0] = 0;
         channel.ethBalances[1] = 0;
         channel.erc20Balances[0] = 0;
         channel.erc20Balances[1] = 0;
         if(ethbalanceA != 0 || ethbalanceI != 0) {
             channel.partyAddresses[0].transfer(ethbalanceA);
             channel.partyAddresses[1].transfer(ethbalanceI);
         }
         if(tokenbalanceA != 0 || tokenbalanceI != 0) {
             require(
                 channel.token.transfer(channel.partyAddresses[0], tokenbalanceA),
                 "byzantineCloseChannel: token transfer failure"
             );
             require(
                 channel.token.transfer(channel.partyAddresses[1], tokenbalanceI),
                 "byzantineCloseChannel: token transfer failure"
             );
         }
         channel.isOpen = false;
         numChannels--;
         emit DidLCClose(_lcID, channel.sequence, ethbalanceA, ethbalanceI, tokenbalanceA, tokenbalanceI);
     }``
        - Line 546, 36 ``Channels[_lcID]``
        - Line 591, 15 ``DidLCClose(_lcID, channel.sequence, ethbalanceA, ethbalanceI, tokenbalanceA, tokenbalanceI)``
        - Line 598, 18 ``cursor < proofElem``
        - Line 599, 37 ``abi.encodePacked(cursor, proofElem)``
        - Line 601, 37 ``abi.encodePacked(proofElem, cursor)``
        - Line 604, 17 ``cursor == _root``
        - Line 606, 6 ``function getChannel(bytes32 id) public view returns (
         address[2],
         uint256[4],
         uint256[4],
         uint256[2],
         uint256,
         uint256,
         bytes32,
         uint256,
         uint256,
         bool,
         bool,
         uint256
     ) {
         Channel memory channel = Channels[id];
         return (
             channel.partyAddresses,
             channel.ethBalances,
             channel.erc20Balances,
             channel.initialDeposit,
             channel.sequence,
             channel.confirmTime,
             channel.VCrootHash,
             channel.LCopenTimeout,
             channel.updateLCtimeout,
             channel.isOpen,
             channel.isUpdateLCSettling,
             channel.numOpenVC
         );
     }``
        - Line 620, 10 ``Channel memory channel = Channels[id]``
        - Line 620, 35 ``Channels[id]``
        - Line 636, 6 ``function getVirtualChannel(bytes32 id) public view returns(
         bool,
         bool,
         uint256,
         address,
         uint256,
         address,
         address,
         address,
         uint256[2],
         uint256[2],
         uint256[2]
     ) {
         VirtualChannel memory virtualChannel = virtualChannels[id];
         return(
             virtualChannel.isClose,
             virtualChannel.isInSettlementState,
             virtualChannel.sequence,
             virtualChannel.challenger,
             virtualChannel.updateVCtimeout,
             virtualChannel.partyA,
             virtualChannel.partyB,
             virtualChannel.partyI,
             virtualChannel.ethBalances,
             virtualChannel.erc20Balances,
             virtualChannel.bond
         );
     }``
        - Line 649, 49 ``virtualChannels[id]``

    - 36%, NOT DUP

        - Line 9, 62 ``6 _value)``

    - 14%, SLOAD DIV

        - Line 142, 6 ``string public name``
        - Line 144, 6 ``string public symbol``
        - Line 145, 6 ``string public version = 'H0.1'``

    - 11%, JUMPDEST ADD

        - Line 275, 18 ``Channels[_lcID].partyAddresses[0]``
        - Line 278, 10 ``Channels[_lcID].partyAddresses[0]``
        - Line 279, 10 ``Channels[_lcID].partyAddresses[1]``
        - Line 282, 14 ``Channels[_lcID].ethBalances[0]``
        - Line 287, 14 ``Channels[_lcID].erc20Balances[0]``
        - Line 296, 32 ``Channels[_lcID].partyAddresses[0]``
        - Line 298, 13 ``Channels[_lcID].initialDeposit[0]``
        - Line 299, 14 ``Channels[_lcID].partyAddresses[0]``
        - Line 299, 57 ``Channels[_lcID].ethBalances[0]``
        - Line 301, 13 ``Channels[_lcID].initialDeposit[1]``
        - Line 302, 53 ``Channels[_lcID].partyAddresses[0]``
        - Line 302, 88 ``Channels[_lcID].erc20Balances[0]``
        - Line 304, 36 ``Channels[_lcID].ethBalances[0]``
        - Line 304, 68 ``Channels[_lcID].erc20Balances[0]``
        - Line 309, 32 ``Channels[_lcID].partyAddresses[1]``
        - Line 312, 14 ``Channels[_lcID].ethBalances[1]``
        - Line 316, 14 ``Channels[_lcID].erc20Balances[1]``
        - Line 318, 10 ``Channels[_lcID].initialDeposit[0]``
        - Line 319, 10 ``Channels[_lcID].initialDeposit[1]``
        - Line 326, 31 ``Channels[_lcID].partyAddresses[0]``
        - Line 326, 81 ``Channels[_lcID].partyAddresses[1]``
        - Line 327, 14 ``Channels[_lcID].partyAddresses[0]``
        - Line 330, 18 ``Channels[_lcID].erc20Balances[2]``
        - Line 333, 18 ``Channels[_lcID].ethBalances[2]``
        - Line 336, 14 ``Channels[_lcID].partyAddresses[1]``
        - Line 339, 18 ``Channels[_lcID].erc20Balances[3]``
        - Line 342, 18 ``Channels[_lcID].ethBalances[3]``
        - Line 357, 36 ``Channels[_lcID].initialDeposit[0]``
        - Line 357, 72 ``Channels[_lcID].ethBalances[2]``
        - Line 357, 105 ``Channels[_lcID].ethBalances[3]``
        - Line 358, 38 ``Channels[_lcID].initialDeposit[1]``
        - Line 358, 74 ``Channels[_lcID].erc20Balances[2]``
        - Line 358, 109 ``Channels[_lcID].erc20Balances[3]``
        - Line 368, 18 ``Channels[_lcID].partyAddresses[0]``
        - Line 369, 18 ``Channels[_lcID].partyAddresses[1]``
        - Line 376, 18 ``Channels[_lcID].partyAddresses[0]``
        - Line 377, 18 ``Channels[_lcID].partyAddresses[1]``
        - Line 380, 14 ``Channels[_lcID].partyAddresses[0]``
        - Line 381, 14 ``Channels[_lcID].partyAddresses[1]``
        - Line 384, 53 ``Channels[_lcID].partyAddresses[0]``
        - Line 385, 53 ``Channels[_lcID].partyAddresses[1]``
        - Line 402, 18 ``channel.ethBalances[0]``
        - Line 402, 43 ``channel.ethBalances[1]``
        - Line 403, 18 ``channel.erc20Balances[0]``
        - Line 403, 45 ``channel.erc20Balances[1]``
        - Line 414, 18 ``channel.partyAddresses[0]``
        - Line 415, 18 ``channel.partyAddresses[1]``
        - Line 422, 18 ``channel.partyAddresses[0]``
        - Line 423, 18 ``channel.partyAddresses[1]``
        - Line 426, 10 ``channel.ethBalances[0]``
        - Line 427, 10 ``channel.ethBalances[1]``
        - Line 428, 10 ``channel.erc20Balances[0]``
        - Line 429, 10 ``channel.erc20Balances[1]``
        - Line 469, 10 ``virtualChannels[_vcID].ethBalances[0]``
        - Line 470, 10 ``virtualChannels[_vcID].ethBalances[1]``
        - Line 471, 10 ``virtualChannels[_vcID].erc20Balances[0]``
        - Line 472, 10 ``virtualChannels[_vcID].erc20Balances[1]``
        - Line 493, 14 ``virtualChannels[_vcID].ethBalances[1]``
        - Line 493, 70 ``virtualChannels[_vcID].erc20Balances[1]``
        - Line 497, 14 ``virtualChannels[_vcID].bond[0]``
        - Line 498, 14 ``virtualChannels[_vcID].bond[1]``
        - Line 507, 18 ``virtualChannels[_vcID].bond[0]``
        - Line 508, 18 ``virtualChannels[_vcID].bond[1]``
        - Line 518, 10 ``virtualChannels[_vcID].ethBalances[0]``
        - Line 519, 10 ``virtualChannels[_vcID].ethBalances[1]``
        - Line 520, 10 ``virtualChannels[_vcID].erc20Balances[0]``
        - Line 521, 10 ``virtualChannels[_vcID].erc20Balances[1]``
        - Line 532, 46 ``Channels[_lcID].partyAddresses[0]``
        - Line 533, 14 ``Channels[_lcID].ethBalances[0]``
        - Line 533, 48 ``virtualChannels[_vcID].ethBalances[0]``
        - Line 534, 14 ``Channels[_lcID].ethBalances[1]``
        - Line 534, 48 ``virtualChannels[_vcID].ethBalances[1]``
        - Line 535, 14 ``Channels[_lcID].erc20Balances[0]``
        - Line 535, 50 ``virtualChannels[_vcID].erc20Balances[0]``
        - Line 536, 14 ``Channels[_lcID].erc20Balances[1]``
        - Line 536, 50 ``virtualChannels[_vcID].erc20Balances[1]``
        - Line 537, 54 ``Channels[_lcID].partyAddresses[0]``
        - Line 538, 14 ``Channels[_lcID].ethBalances[0]``
        - Line 538, 48 ``virtualChannels[_vcID].ethBalances[1]``
        - Line 539, 14 ``Channels[_lcID].ethBalances[1]``
        - Line 539, 48 ``virtualChannels[_vcID].ethBalances[0]``
        - Line 540, 14 ``Channels[_lcID].erc20Balances[0]``
        - Line 540, 50 ``virtualChannels[_vcID].erc20Balances[1]``
        - Line 541, 14 ``Channels[_lcID].erc20Balances[1]``
        - Line 541, 50 ``virtualChannels[_vcID].erc20Balances[0]``
        - Line 543, 40 ``virtualChannels[_vcID].erc20Balances[0]``
        - Line 543, 81 ``virtualChannels[_vcID].erc20Balances[1]``
        - Line 551, 36 ``channel.initialDeposit[0]``
        - Line 551, 64 ``channel.ethBalances[2]``
        - Line 551, 89 ``channel.ethBalances[3]``
        - Line 552, 38 ``channel.initialDeposit[1]``
        - Line 552, 66 ``channel.erc20Balances[2]``
        - Line 552, 93 ``channel.erc20Balances[3]``
        - Line 553, 50 ``channel.ethBalances[0]``
        - Line 553, 75 ``channel.ethBalances[1]``
        - Line 554, 52 ``channel.erc20Balances[0]``
        - Line 554, 79 ``channel.erc20Balances[1]``
        - Line 556, 14 ``channel.ethBalances[0]``
        - Line 556, 38 ``channel.ethBalances[2]``
        - Line 557, 14 ``channel.ethBalances[1]``
        - Line 557, 38 ``channel.ethBalances[3]``
        - Line 562, 14 ``channel.erc20Balances[0]``
        - Line 562, 40 ``channel.erc20Balances[2]``
        - Line 563, 14 ``channel.erc20Balances[1]``
        - Line 563, 40 ``channel.erc20Balances[3]``
        - Line 567, 32 ``channel.ethBalances[0]``
        - Line 568, 32 ``channel.ethBalances[1]``
        - Line 569, 34 ``channel.erc20Balances[0]``
        - Line 570, 34 ``channel.erc20Balances[1]``
        - Line 571, 10 ``channel.ethBalances[0]``
        - Line 572, 10 ``channel.ethBalances[1]``
        - Line 573, 10 ``channel.erc20Balances[0]``
        - Line 574, 10 ``channel.erc20Balances[1]``
        - Line 576, 14 ``channel.partyAddresses[0]``
        - Line 577, 14 ``channel.partyAddresses[1]``
        - Line 581, 41 ``channel.partyAddresses[0]``
        - Line 585, 41 ``channel.partyAddresses[1]``

* _`X`_ Overflow
    - 58%, SWAP SWAP SWAP SWAP SWAP

        - Line 16, 6 ``function recoverSigner(bytes32 _hashedMsg, string _sig) public pure returns (address) {
         require(_hashedMsg != 0x00);
         bytes memory prefix = "\x19Ethereum Signed Message:\n32";
         bytes32 prefixedHash = keccak256(abi.encodePacked(prefix, _hashedMsg));
         if (bytes(_sig).length != 132) {
             return 0x0;
         }
         bytes32 r;
         bytes32 s;
         uint8 v;
         bytes memory sig = hexstrToBytes(substring(_sig, 2, 132));
         assembly {
             r := mload(add(sig, 32))
             s := mload(add(sig, 64))
             v := byte(0, mload(add(sig, 96)))
         }
         if (v < 27) {
             v += 27;
         }
         if (v < 27 || v > 28) {
             return 0x0;
         }
         return ecrecover(prefixedHash, v, r, s);
     }``
        - Line 40, 6 ``function isSignedBy(bytes32 _hashedMsg, string _sig, address _addr) public pure returns (bool) {
         require(_addr != 0x0);
         return _addr == recoverSigner(_hashedMsg, _sig);
     }``
        - Line 44, 6 ``function hexstrToBytes(string _hexstr) public pure returns (bytes) {
         uint len = bytes(_hexstr).length;
         require(len % 2 == 0);
         bytes memory bstr = bytes(new string(len / 2));
         uint k = 0;
         string memory s;
         string memory r;
         for (uint i = 0; i < len; i += 2) {
             s = substring(_hexstr, i, i + 1);
             r = substring(_hexstr, i + 1, i + 2);
             uint p = parseInt16Char(s) * 16 + parseInt16Char(r);
             bstr[k++] = uintToBytes32(p)[31];
         }
         return bstr;
     }``
        - Line 59, 6 ``function parseInt16Char(string _char) public pure returns (uint) {
         bytes memory bresult = bytes(_char);
         if ((bresult[0] >= 48) && (bresult[0] <= 57)) {
             return uint(bresult[0]) - 48;
         } else if ((bresult[0] >= 65) && (bresult[0] <= 70)) {
             return uint(bresult[0]) - 55;
         } else if ((bresult[0] >= 97) && (bresult[0] <= 102)) {
             return uint(bresult[0]) - 87;
         } else {
             revert();
         }
     }``
        - Line 75, 6 ``function toEthereumSignedMessage(string _msg) public pure returns (bytes32) {
         uint len = bytes(_msg).length;
         require(len > 0);
         bytes memory prefix = "\x19Ethereum Signed Message:\n";
         return keccak256(abi.encodePacked(prefix, uintToString(len), _msg));
     }``
        - Line 97, 6 ``function substring(string _str, uint _startIndex, uint _endIndex) public pure returns (string) {
         bytes memory strBytes = bytes(_str);
         require(_startIndex <= _endIndex);
         require(_startIndex >= 0);
         require(_endIndex <= strBytes.length);
         bytes memory result = new bytes(_endIndex - _startIndex);
         for (uint i = _startIndex; i < _endIndex; i++) {
             result[i - _startIndex] = strBytes[i];
         }
         return string(result);
     }``
        - Line 159, 6 ``function approveAndCall(address _spender, uint256 _value, bytes _extraData) public returns (bool success) {
         allowed[msg.sender][_spender] = _value;
         emit Approval(msg.sender, _spender, _value);
         require(_spender.call(bytes4(bytes32(keccak256("receiveApproval(address,uint256,address,bytes)"))), msg.sender, _value, this, _extraData));
         return true;
     }``
        - Line 265, 6 ``function createChannel(
         bytes32 _lcID,
         address _partyI,
         uint256 _confirmTime,
         address _token,
         uint256[2] _balances
     )
         public
         payable
     {
         require(Channels[_lcID].partyAddresses[0] == address(0), "Channel has already been created.");
         require(_partyI != 0x0, "No partyI address provided to LC creation");
         require(_balances[0] >= 0 && _balances[1] >= 0, "Balances cannot be negative");
         Channels[_lcID].partyAddresses[0] = msg.sender;
         Channels[_lcID].partyAddresses[1] = _partyI;
         if(_balances[0] != 0) {
             require(msg.value == _balances[0], "Eth balance does not match sent value");
             Channels[_lcID].ethBalances[0] = msg.value;
         }
         if(_balances[1] != 0) {
             Channels[_lcID].token = HumanStandardToken(_token);
             require(Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1]),"CreateChannel: token transfer failure");
             Channels[_lcID].erc20Balances[0] = _balances[1];
         }
         Channels[_lcID].sequence = 0;
         Channels[_lcID].confirmTime = _confirmTime;
         Channels[_lcID].LCopenTimeout = now + _confirmTime;
         Channels[_lcID].initialDeposit = _balances;
         emit DidLCOpen(_lcID, msg.sender, _partyI, _balances[0], _token, _balances[1], Channels[_lcID].LCopenTimeout);
     }``
        - Line 307, 6 ``function joinChannel(bytes32 _lcID, uint256[2] _balances) public payable {
         require(Channels[_lcID].isOpen == false);
         require(msg.sender == Channels[_lcID].partyAddresses[1]);
         if(_balances[0] != 0) {
             require(msg.value == _balances[0], "state balance does not match sent value");
             Channels[_lcID].ethBalances[1] = msg.value;
         }
         if(_balances[1] != 0) {
             require(Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1]),"joinChannel: token transfer failure");
             Channels[_lcID].erc20Balances[1] = _balances[1];
         }
         Channels[_lcID].initialDeposit[0]+=_balances[0];
         Channels[_lcID].initialDeposit[1]+=_balances[1];
         Channels[_lcID].isOpen = true;
         numChannels++;
         emit DidLCJoin(_lcID, _balances[0], _balances[1]);
     }``
        - Line 347, 6 ``function consensusCloseChannel(
         bytes32 _lcID,
         uint256 _sequence,
         uint256[4] _balances,
         string _sigA,
         string _sigI
     )
         public
     {
         require(Channels[_lcID].isOpen == true);
         uint256 totalEthDeposit = Channels[_lcID].initialDeposit[0] + Channels[_lcID].ethBalances[2] + Channels[_lcID].ethBalances[3];
         uint256 totalTokenDeposit = Channels[_lcID].initialDeposit[1] + Channels[_lcID].erc20Balances[2] + Channels[_lcID].erc20Balances[3];
         require(totalEthDeposit == _balances[0] + _balances[1]);
         require(totalTokenDeposit == _balances[2] + _balances[3]);
         bytes32 _state = keccak256(
             abi.encodePacked(
                 _lcID,
                 true,
                 _sequence,
                 uint256(0),
                 bytes32(0x0),
                 Channels[_lcID].partyAddresses[0],
                 Channels[_lcID].partyAddresses[1],
                 _balances[0],
                 _balances[1],
                 _balances[2],
                 _balances[3]
             )
         );
         require(Channels[_lcID].partyAddresses[0] == ECTools.recoverSigner(_state, _sigA));
         require(Channels[_lcID].partyAddresses[1] == ECTools.recoverSigner(_state, _sigI));
         Channels[_lcID].isOpen = false;
         if(_balances[0] != 0 || _balances[1] != 0) {
             Channels[_lcID].partyAddresses[0].transfer(_balances[0]);
             Channels[_lcID].partyAddresses[1].transfer(_balances[1]);
         }
         if(_balances[2] != 0 || _balances[3] != 0) {
             require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], _balances[2]),"happyCloseChannel: token transfer failure");
             require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[1], _balances[3]),"happyCloseChannel: token transfer failure");
         }
         numChannels--;
         emit DidLCClose(_lcID, _sequence, _balances[0], _balances[1], _balances[2], _balances[3]);
     }``
        - Line 390, 6 ``function updateLCstate(
         bytes32 _lcID,
         uint256[6] updateParams,
         bytes32 _VCroot,
         string _sigA,
         string _sigI
     )
         public
     {
         Channel storage channel = Channels[_lcID];
         require(channel.isOpen);
         require(channel.sequence < updateParams[0]);
         require(channel.ethBalances[0] + channel.ethBalances[1] >= updateParams[2] + updateParams[3]);
         require(channel.erc20Balances[0] + channel.erc20Balances[1] >= updateParams[4] + updateParams[5]);
         if(channel.isUpdateLCSettling == true) {
             require(channel.updateLCtimeout > now);
         }
         bytes32 _state = keccak256(
             abi.encodePacked(
                 _lcID,
                 false,
                 updateParams[0],
                 updateParams[1],
                 _VCroot,
                 channel.partyAddresses[0],
                 channel.partyAddresses[1],
                 updateParams[2],
                 updateParams[3],
                 updateParams[4],
                 updateParams[5]
             )
         );
         require(channel.partyAddresses[0] == ECTools.recoverSigner(_state, _sigA));
         require(channel.partyAddresses[1] == ECTools.recoverSigner(_state, _sigI));
         channel.sequence = updateParams[0];
         channel.numOpenVC = updateParams[1];
         channel.ethBalances[0] = updateParams[2];
         channel.ethBalances[1] = updateParams[3];
         channel.erc20Balances[0] = updateParams[4];
         channel.erc20Balances[1] = updateParams[5];
         channel.VCrootHash = _VCroot;
         channel.isUpdateLCSettling = true;
         channel.updateLCtimeout = now + channel.confirmTime;
         emit DidLCUpdateState (
             _lcID,
             updateParams[0],
             updateParams[1],
             updateParams[2],
             updateParams[3],
             updateParams[4],
             updateParams[5],
             _VCroot,
             channel.updateLCtimeout
         );
     }``
        - Line 445, 6 ``function initVCstate(
         bytes32 _lcID,
         bytes32 _vcID,
         bytes _proof,
         address _partyA,
         address _partyB,
         uint256[2] _bond,
         uint256[4] _balances,
         string sigA
     )
         public
     {
         require(Channels[_lcID].isOpen, "LC is closed.");
         require(!virtualChannels[_vcID].isClose, "VC is closed.");
         require(Channels[_lcID].updateLCtimeout < now, "LC timeout not over.");
         require(virtualChannels[_vcID].updateVCtimeout == 0);
         bytes32 _initState = keccak256(
             abi.encodePacked(_vcID, uint256(0), _partyA, _partyB, _bond[0], _bond[1], _balances[0], _balances[1], _balances[2], _balances[3])
         );
         require(_partyA == ECTools.recoverSigner(_initState, sigA));
         require(_isContained(_initState, _proof, Channels[_lcID].VCrootHash) == true);
         virtualChannels[_vcID].partyA = _partyA;
         virtualChannels[_vcID].partyB = _partyB;
         virtualChannels[_vcID].sequence = uint256(0);
         virtualChannels[_vcID].ethBalances[0] = _balances[0];
         virtualChannels[_vcID].ethBalances[1] = _balances[1];
         virtualChannels[_vcID].erc20Balances[0] = _balances[2];
         virtualChannels[_vcID].erc20Balances[1] = _balances[3];
         virtualChannels[_vcID].bond = _bond;
         virtualChannels[_vcID].updateVCtimeout = now + Channels[_lcID].confirmTime;
         virtualChannels[_vcID].isInSettlementState = true;
         emit DidVCInit(_lcID, _vcID, _proof, uint256(0), _partyA, _partyB, _balances[0], _balances[1]);
     }``
        - Line 478, 6 ``function settleVC(
         bytes32 _lcID,
         bytes32 _vcID,
         uint256 updateSeq,
         address _partyA,
         address _partyB,
         uint256[4] updateBal,
         string sigA
     )
         public
     {
         require(Channels[_lcID].isOpen, "LC is closed.");
         require(!virtualChannels[_vcID].isClose, "VC is closed.");
         require(virtualChannels[_vcID].sequence < updateSeq, "VC sequence is higher than update sequence.");
         require(
             virtualChannels[_vcID].ethBalances[1] < updateBal[1] && virtualChannels[_vcID].erc20Balances[1] < updateBal[3],
             "State updates may only increase recipient balance."
         );
         require(
             virtualChannels[_vcID].bond[0] == updateBal[0] + updateBal[1] &&
             virtualChannels[_vcID].bond[1] == updateBal[2] + updateBal[3],
             "Incorrect balances for bonded amount");
         require(Channels[_lcID].updateLCtimeout < now);
         bytes32 _updateState = keccak256(
             abi.encodePacked(
                 _vcID,
                 updateSeq,
                 _partyA,
                 _partyB,
                 virtualChannels[_vcID].bond[0],
                 virtualChannels[_vcID].bond[1],
                 updateBal[0],
                 updateBal[1],
                 updateBal[2],
                 updateBal[3]
             )
         );
         require(virtualChannels[_vcID].partyA == ECTools.recoverSigner(_updateState, sigA));
         virtualChannels[_vcID].challenger = msg.sender;
         virtualChannels[_vcID].sequence = updateSeq;
         virtualChannels[_vcID].ethBalances[0] = updateBal[0];
         virtualChannels[_vcID].ethBalances[1] = updateBal[1];
         virtualChannels[_vcID].erc20Balances[0] = updateBal[2];
         virtualChannels[_vcID].erc20Balances[1] = updateBal[3];
         virtualChannels[_vcID].updateVCtimeout = now + Channels[_lcID].confirmTime;
         emit DidVCSettle(_lcID, _vcID, updateSeq, updateBal[0], updateBal[1], msg.sender, virtualChannels[_vcID].updateVCtimeout);
     }``
        - Line 606, 6 ``function getChannel(bytes32 id) public view returns (
         address[2],
         uint256[4],
         uint256[4],
         uint256[2],
         uint256,
         uint256,
         bytes32,
         uint256,
         uint256,
         bool,
         bool,
         uint256
     ) {
         Channel memory channel = Channels[id];
         return (
             channel.partyAddresses,
             channel.ethBalances,
             channel.erc20Balances,
             channel.initialDeposit,
             channel.sequence,
             channel.confirmTime,
             channel.VCrootHash,
             channel.LCopenTimeout,
             channel.updateLCtimeout,
             channel.isOpen,
             channel.isUpdateLCSettling,
             channel.numOpenVC
         );
     }``
        - Line 636, 6 ``function getVirtualChannel(bytes32 id) public view returns(
         bool,
         bool,
         uint256,
         address,
         uint256,
         address,
         address,
         address,
         uint256[2],
         uint256[2],
         uint256[2]
     ) {
         VirtualChannel memory virtualChannel = virtualChannels[id];
         return(
             virtualChannel.isClose,
             virtualChannel.isInSettlementState,
             virtualChannel.sequence,
             virtualChannel.challenger,
             virtualChannel.updateVCtimeout,
             virtualChannel.partyA,
             virtualChannel.partyB,
             virtualChannel.partyI,
             virtualChannel.ethBalances,
             virtualChannel.erc20Balances,
             virtualChannel.bond
         );
     }``

    - 42%, ADD PUSH SHA PUSH ADD

        - Line 275, 18 ``Channels[_lcID]``
        - Line 278, 10 ``Channels[_lcID]``
        - Line 279, 10 ``Channels[_lcID]``
        - Line 282, 14 ``Channels[_lcID]``
        - Line 285, 14 ``Channels[_lcID]``
        - Line 286, 22 ``Channels[_lcID]``
        - Line 287, 14 ``Channels[_lcID]``
        - Line 289, 10 ``Channels[_lcID]``
        - Line 290, 10 ``Channels[_lcID]``
        - Line 291, 10 ``Channels[_lcID]``
        - Line 292, 10 ``Channels[_lcID]``
        - Line 293, 89 ``Channels[_lcID]``
        - Line 296, 32 ``Channels[_lcID]``
        - Line 296, 69 ``Channels[_lcID]``
        - Line 297, 24 ``Channels[_lcID]``
        - Line 298, 13 ``Channels[_lcID]``
        - Line 299, 14 ``Channels[_lcID]``
        - Line 299, 57 ``Channels[_lcID]``
        - Line 301, 13 ``Channels[_lcID]``
        - Line 302, 22 ``Channels[_lcID]``
        - Line 302, 53 ``Channels[_lcID]``
        - Line 302, 88 ``Channels[_lcID]``
        - Line 304, 36 ``Channels[_lcID]``
        - Line 304, 68 ``Channels[_lcID]``
        - Line 308, 18 ``Channels[_lcID]``
        - Line 309, 32 ``Channels[_lcID]``
        - Line 312, 14 ``Channels[_lcID]``
        - Line 315, 22 ``Channels[_lcID]``
        - Line 316, 14 ``Channels[_lcID]``
        - Line 318, 10 ``Channels[_lcID]``
        - Line 319, 10 ``Channels[_lcID]``
        - Line 320, 10 ``Channels[_lcID]``
        - Line 325, 18 ``Channels[_lcID]``
        - Line 326, 31 ``Channels[_lcID]``
        - Line 326, 81 ``Channels[_lcID]``
        - Line 327, 14 ``Channels[_lcID]``
        - Line 329, 26 ``Channels[_lcID]``
        - Line 330, 18 ``Channels[_lcID]``
        - Line 333, 18 ``Channels[_lcID]``
        - Line 336, 14 ``Channels[_lcID]``
        - Line 338, 26 ``Channels[_lcID]``
        - Line 339, 18 ``Channels[_lcID]``
        - Line 342, 18 ``Channels[_lcID]``
        - Line 356, 18 ``Channels[_lcID]``
        - Line 357, 36 ``Channels[_lcID]``
        - Line 357, 72 ``Channels[_lcID]``
        - Line 357, 105 ``Channels[_lcID]``
        - Line 358, 38 ``Channels[_lcID]``
        - Line 358, 74 ``Channels[_lcID]``
        - Line 358, 109 ``Channels[_lcID]``
        - Line 368, 18 ``Channels[_lcID]``
        - Line 369, 18 ``Channels[_lcID]``
        - Line 376, 18 ``Channels[_lcID]``
        - Line 377, 18 ``Channels[_lcID]``
        - Line 378, 10 ``Channels[_lcID]``
        - Line 380, 14 ``Channels[_lcID]``
        - Line 381, 14 ``Channels[_lcID]``
        - Line 384, 22 ``Channels[_lcID]``
        - Line 384, 53 ``Channels[_lcID]``
        - Line 385, 22 ``Channels[_lcID]``
        - Line 385, 53 ``Channels[_lcID]``
        - Line 457, 18 ``Channels[_lcID]``
        - Line 458, 19 ``virtualChannels[_vcID]``
        - Line 459, 18 ``Channels[_lcID]``
        - Line 460, 18 ``virtualChannels[_vcID]``
        - Line 465, 51 ``Channels[_lcID]``
        - Line 466, 10 ``virtualChannels[_vcID]``
        - Line 467, 10 ``virtualChannels[_vcID]``
        - Line 468, 10 ``virtualChannels[_vcID]``
        - Line 469, 10 ``virtualChannels[_vcID]``
        - Line 470, 10 ``virtualChannels[_vcID]``
        - Line 471, 10 ``virtualChannels[_vcID]``
        - Line 472, 10 ``virtualChannels[_vcID]``
        - Line 473, 10 ``virtualChannels[_vcID]``
        - Line 474, 10 ``virtualChannels[_vcID]``
        - Line 474, 57 ``Channels[_lcID]``
        - Line 475, 10 ``virtualChannels[_vcID]``
        - Line 489, 18 ``Channels[_lcID]``
        - Line 490, 19 ``virtualChannels[_vcID]``
        - Line 491, 18 ``virtualChannels[_vcID]``
        - Line 493, 14 ``virtualChannels[_vcID]``
        - Line 493, 70 ``virtualChannels[_vcID]``
        - Line 497, 14 ``virtualChannels[_vcID]``
        - Line 498, 14 ``virtualChannels[_vcID]``
        - Line 500, 18 ``Channels[_lcID]``
        - Line 507, 18 ``virtualChannels[_vcID]``
        - Line 508, 18 ``virtualChannels[_vcID]``
        - Line 515, 18 ``virtualChannels[_vcID]``
        - Line 516, 10 ``virtualChannels[_vcID]``
        - Line 517, 10 ``virtualChannels[_vcID]``
        - Line 518, 10 ``virtualChannels[_vcID]``
        - Line 519, 10 ``virtualChannels[_vcID]``
        - Line 520, 10 ``virtualChannels[_vcID]``
        - Line 521, 10 ``virtualChannels[_vcID]``
        - Line 522, 10 ``virtualChannels[_vcID]``
        - Line 522, 57 ``Channels[_lcID]``
        - Line 523, 92 ``virtualChannels[_vcID]``
        - Line 526, 18 ``Channels[_lcID]``
        - Line 527, 18 ``virtualChannels[_vcID]``
        - Line 528, 18 ``virtualChannels[_vcID]``
        - Line 529, 19 ``virtualChannels[_vcID]``
        - Line 530, 10 ``Channels[_lcID]``
        - Line 531, 10 ``virtualChannels[_vcID]``
        - Line 532, 13 ``virtualChannels[_vcID]``
        - Line 532, 46 ``Channels[_lcID]``
        - Line 533, 14 ``Channels[_lcID]``
        - Line 533, 48 ``virtualChannels[_vcID]``
        - Line 534, 14 ``Channels[_lcID]``
        - Line 534, 48 ``virtualChannels[_vcID]``
        - Line 535, 14 ``Channels[_lcID]``
        - Line 535, 50 ``virtualChannels[_vcID]``
        - Line 536, 14 ``Channels[_lcID]``
        - Line 536, 50 ``virtualChannels[_vcID]``
        - Line 537, 21 ``virtualChannels[_vcID]``
        - Line 537, 54 ``Channels[_lcID]``
        - Line 538, 14 ``Channels[_lcID]``
        - Line 538, 48 ``virtualChannels[_vcID]``
        - Line 539, 14 ``Channels[_lcID]``
        - Line 539, 48 ``virtualChannels[_vcID]``
        - Line 540, 14 ``Channels[_lcID]``
        - Line 540, 50 ``virtualChannels[_vcID]``
        - Line 541, 14 ``Channels[_lcID]``
        - Line 541, 50 ``virtualChannels[_vcID]``
        - Line 543, 40 ``virtualChannels[_vcID]``
        - Line 543, 81 ``virtualChannels[_vcID]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, ADD DUP DUP PUSH ADD

        - Line 275, 10 ``require(Channels[_lcID].partyAddresses[0] == address(0), "Channel has already been created.")``
        - Line 276, 10 ``require(_partyI != 0x0, "No partyI address provided to LC creation")``
        - Line 277, 10 ``require(_balances[0] >= 0 && _balances[1] >= 0, "Balances cannot be negative")``
        - Line 281, 14 ``require(msg.value == _balances[0], "Eth balance does not match sent value")``
        - Line 286, 14 ``require(Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1]),"CreateChannel: token transfer failure")``
        - Line 302, 14 ``require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], Channels[_lcID].erc20Balances[0]),"CreateChannel: token transfer failure")``
        - Line 311, 14 ``require(msg.value == _balances[0], "state balance does not match sent value")``
        - Line 315, 14 ``require(Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1]),"joinChannel: token transfer failure")``
        - Line 325, 10 ``require(Channels[_lcID].isOpen == true, "Tried adding funds to a closed channel")``
        - Line 329, 18 ``require(Channels[_lcID].token.transferFrom(msg.sender, this, _balance),"deposit: token transfer failure")``
        - Line 332, 18 ``require(msg.value == _balance, "state balance does not match sent value")``
        - Line 338, 18 ``require(Channels[_lcID].token.transferFrom(msg.sender, this, _balance),"deposit: token transfer failure")``
        - Line 341, 18 ``require(msg.value == _balance, "state balance does not match sent value")``
        - Line 384, 14 ``require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], _balances[2]),"happyCloseChannel: token transfer failure")``
        - Line 385, 14 ``require(Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[1], _balances[3]),"happyCloseChannel: token transfer failure")``
        - Line 457, 10 ``require(Channels[_lcID].isOpen, "LC is closed.")``
        - Line 458, 10 ``require(!virtualChannels[_vcID].isClose, "VC is closed.")``
        - Line 459, 10 ``require(Channels[_lcID].updateLCtimeout < now, "LC timeout not over.")``
        - Line 489, 10 ``require(Channels[_lcID].isOpen, "LC is closed.")``
        - Line 490, 10 ``require(!virtualChannels[_vcID].isClose, "VC is closed.")``
        - Line 491, 10 ``require(virtualChannels[_vcID].sequence < updateSeq, "VC sequence is higher than update sequence.")``
        - Line 492, 10 ``require(
             virtualChannels[_vcID].ethBalances[1] < updateBal[1] && virtualChannels[_vcID].erc20Balances[1] < updateBal[3],
             "State updates may only increase recipient balance."
         )``
        - Line 496, 10 ``require(
             virtualChannels[_vcID].bond[0] == updateBal[0] + updateBal[1] &&
             virtualChannels[_vcID].bond[1] == updateBal[2] + updateBal[3],
             "Incorrect balances for bonded amount")``
        - Line 526, 10 ``require(Channels[_lcID].isOpen, "LC is closed.")``
        - Line 527, 10 ``require(virtualChannels[_vcID].isInSettlementState, "VC is not in settlement state.")``
        - Line 528, 10 ``require(virtualChannels[_vcID].updateVCtimeout < now, "Update vc timeout has not elapsed.")``
        - Line 529, 10 ``require(!virtualChannels[_vcID].isClose, "VC is already closed")``
        - Line 547, 10 ``require(channel.isOpen, "Channel is not open")``
        - Line 550, 10 ``require(channel.updateLCtimeout < now, "LC timeout over.")``
        - Line 580, 14 ``require(
                 channel.token.transfer(channel.partyAddresses[0], tokenbalanceA),
                 "byzantineCloseChannel: token transfer failure"
             )``
        - Line 584, 14 ``require(
                 channel.token.transfer(channel.partyAddresses[1], tokenbalanceI),
                 "byzantineCloseChannel: token transfer failure"
             )``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 291, 42 ``now``
        - Line 297, 18 ``now``
        - Line 405, 48 ``now``
        - Line 432, 36 ``now``
        - Line 459, 52 ``now``
        - Line 474, 51 ``now``
        - Line 500, 52 ``now``
        - Line 522, 51 ``now``
        - Line 528, 59 ``now``
        - Line 550, 44 ``now``

* _`X`_ LowlevelCalls
    - 54%, POP GAS

        - Line 286, 22 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1])``
        - Line 302, 22 ``Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], Channels[_lcID].erc20Balances[0])``
        - Line 315, 22 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1])``
        - Line 329, 26 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balance)``
        - Line 338, 26 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balance)``
        - Line 376, 55 ``ECTools.recoverSigner(_state, _sigA)``
        - Line 377, 55 ``ECTools.recoverSigner(_state, _sigI)``
        - Line 384, 22 ``Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], _balances[2])``
        - Line 385, 22 ``Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[1], _balances[3])``
        - Line 422, 47 ``ECTools.recoverSigner(_state, _sigA)``
        - Line 423, 47 ``ECTools.recoverSigner(_state, _sigI)``
        - Line 464, 29 ``ECTools.recoverSigner(_initState, sigA)``
        - Line 515, 51 ``ECTools.recoverSigner(_updateState, sigA)``
        - Line 581, 18 ``channel.token.transfer(channel.partyAddresses[0], tokenbalanceA)``
        - Line 585, 18 ``channel.token.transfer(channel.partyAddresses[1], tokenbalanceI)``

    - 46%, CALL ISZERO

        - Line 38, 17 ``ecrecover(prefixedHash, v, r, s)``
        - Line 286, 22 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1])``
        - Line 302, 22 ``Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], Channels[_lcID].erc20Balances[0])``
        - Line 315, 22 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balances[1])``
        - Line 329, 26 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balance)``
        - Line 338, 26 ``Channels[_lcID].token.transferFrom(msg.sender, this, _balance)``
        - Line 384, 22 ``Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[0], _balances[2])``
        - Line 385, 22 ``Channels[_lcID].token.transfer(Channels[_lcID].partyAddresses[1], _balances[3])``
        - Line 581, 18 ``channel.token.transfer(channel.partyAddresses[0], tokenbalanceA)``
        - Line 585, 18 ``channel.token.transfer(channel.partyAddresses[1], tokenbalanceI)``

* __O__ BlockHash
* __O__ SelfDestruct
