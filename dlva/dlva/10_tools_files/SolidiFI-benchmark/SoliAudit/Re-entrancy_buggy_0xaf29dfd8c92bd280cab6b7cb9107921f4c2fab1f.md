# Vulnerability Analysis #
#### 2023-06-05 08:35:03 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 6, 2 ``mapping(uint8 => string) public hashTypes``
        - Line 78, 3 ``return hashInfo.pubKeyHash``
        - Line 83, 3 ``return hashInfo.keyID``

* _`X`_ Overflow
    - 100%, SWAP SWAP SWAP SWAP SWAP

        - Line 41, 2 ``function addHashType(uint8 hashType, string description) public onlyByOwner {
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
        - Line 48, 4 ``allHashTypes.push(hashType)``
        - Line 57, 2 ``function addPubKeyHash(bytes20 userID, uint8 hashType, bytes pubKeyHash, bytes keyID) public onlyByOwner {
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
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 61%, GAS CALL

        - Line 21, 9 ``msg.sender.call.value(10 ether)("")``

    - 39%, ADD JUMPDEST

        - Line 3, 1 ``contract PubKeyTrust {
	address owner;
	uint8[] public allHashTypes;
	mapping(uint8 => string) public hashTypes;
	struct HashInfo {
		bytes pubKeyHash;
		bytes keyID;
		uint blockNumber;
	}
	struct UserHashes {
		mapping(uint8 => HashInfo) hashes;
		bool initialized;
	}
	mapping(bytes20 => UserHashes) hashes;
	event UserAdded(bytes20 indexed userID);
	event PubKeyHashAdded(bytes20 indexed userID, uint8 indexed hashType);uint256 counter_re_ent21 =0;
function callme_re_ent21() public{
        require(counter_re_ent21<=5);
	if( ! (msg.sender.call.value(10 ether)("") ) ){
            revert();
        }
        counter_re_ent21 += 1;
    }

	event PubKeyHashTypeAdded(uint8 indexed hashType);
	function PubKeyTrust() public {
		owner = msg.sender;
	}
	modifier onlyByOwner()
	{
		if (msg.sender != owner)
			require(false);
		else
			_;
	}
	function numHashTypes() public view returns (uint) {
		return allHashTypes.length;
	}
	function addHashType(uint8 hashType, string description) public onlyByOwner {
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
	}
	function isValidHashType(uint8 hashType) public view returns (bool) {
		string storage description = hashTypes[hashType];
		return (bytes(description).length > 0);
	}
	function addPubKeyHash(bytes20 userID, uint8 hashType, bytes pubKeyHash, bytes keyID) public onlyByOwner {
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
	}
	function getPubKeyHash(bytes20 userID, uint8 hashType) public view returns (bytes) {
		UserHashes storage userHashes = hashes[userID];
		HashInfo storage hashInfo = userHashes.hashes[hashType];
		return hashInfo.pubKeyHash;
	}
	function getKeyID(bytes20 userID, uint8 hashType) public view returns (bytes) {
		UserHashes storage userHashes = hashes[userID];
		HashInfo storage hashInfo = userHashes.hashes[hashType];
		return hashInfo.keyID;
	}
	function getBlockNumber(bytes20 userID, uint8 hashType) public view returns (uint) {
		UserHashes storage userHashes = hashes[userID];
		HashInfo storage hashInfo = userHashes.hashes[hashType];
		return hashInfo.blockNumber;
	}
}``

* __O__ BlockHash
* __O__ SelfDestruct
