# Vulnerability Analysis #
#### 2023-06-05 08:37:51 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 6, 2 ``mapping(uint8 => string) public hashTypes``
        - Line 80, 3 ``return hashInfo.pubKeyHash``
        - Line 85, 3 ``return hashInfo.keyID``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 43, 2 ``function addHashType(uint8 hashType, string description) public onlyByOwner {
		if (hashType == 0) require(false);
		if (bytes(description).length == 0) require(false);
		if (bytes(description).length > 64) require(false);
		string storage prvDescription = hashTypes[hashType];
		if (bytes(prvDescription).length == 0)
		{
			allHashTypes.push(hashType);
			hashTypes[hashType] = description;
			PubKeyHashTypeAdded(hashType);
		}
	}``
        - Line 50, 4 ``allHashTypes.push(hashType)``
        - Line 59, 2 ``function addPubKeyHash(bytes20 userID, uint8 hashType, bytes pubKeyHash, bytes keyID) public onlyByOwner {
		if (!isValidHashType(hashType)) require(false);
		if (pubKeyHash.length == 0) require(false);
		if (keyID.length == 0) require(false);
		UserHashes storage userHashes = hashes[userID];
		if (!userHashes.initialized) {
			userHashes.initialized = true;
			UserAdded(userID);
		}
		HashInfo storage hashInfo = userHashes.hashes[hashType];
		if (hashInfo.blockNumber == 0)
		{
			hashInfo.pubKeyHash = pubKeyHash;
			hashInfo.keyID = keyID;
			hashInfo.blockNumber = block.number;
			PubKeyHashAdded(userID, hashType);
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

        - Line 20, 17 ``now``
        - Line 21, 34 ``now``
        - Line 22, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
