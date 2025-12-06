# Vulnerability Analysis #
#### 2023-06-05 08:53:52 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 3 ``mapping (uint256 => bytes) public marks``

* _`X`_ Overflow
    - 100%, PUSH ADD SWAP SWAP POP

        - Line 29, 5 ``markId ++``
        - Line 30, 5 ``marked[msg.sender] ++``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, DUP DUP SUB SUB DUP

        - Line 3, 14 ``Efg {
 ``

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
