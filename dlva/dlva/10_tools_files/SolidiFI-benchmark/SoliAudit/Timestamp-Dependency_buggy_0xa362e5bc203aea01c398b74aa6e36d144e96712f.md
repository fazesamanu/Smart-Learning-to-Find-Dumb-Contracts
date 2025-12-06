# Vulnerability Analysis #
#### 2023-06-05 08:37:29 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 5 ``string public name = "Arcblock Token"``
        - Line 7, 5 ``string public symbol = "ABT"``

* _`X`_ Overflow
    - 100%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 23, 5 ``function changeToken(string cName, string cSymbol) onlyOwner public {
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
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 39, 17 ``now``
        - Line 40, 34 ``now``
        - Line 41, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
