# Vulnerability Analysis #
#### 2023-06-05 08:44:25 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "Arcblock Token"``
        - Line 7, 5 ``string public symbol = "ABT"``

* _`X`_ Overflow
    - 100%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 22, 5 ``function changeToken(string cName, string cSymbol) onlyOwner public {
        name = cName;
        symbol = cSymbol;
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
    - 100%, GAS CALL

        - Line 38, 16 ``msg.sender.call.value(1 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
