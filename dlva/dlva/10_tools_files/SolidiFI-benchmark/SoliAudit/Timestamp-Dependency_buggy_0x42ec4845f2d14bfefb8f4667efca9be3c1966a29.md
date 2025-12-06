# Vulnerability Analysis #
#### 2023-06-05 08:52:31 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 6, 5 ``string      public standard = 'Token 0.1'``
        - Line 7, 5 ``string      public name = 'ZombieToken'``
        - Line 8, 5 ``string      public symbol = 'ZMB'``
        - Line 21, 14 ``NameChange(name)``
        - Line 27, 14 ``SymbolChange(symbol)``

* _`X`_ Overflow
    - 51%, JUMPDEST POP POP SWAP POP

        - Line 21, 14 ``NameChange(name)``
        - Line 27, 14 ``SymbolChange(symbol)``

    - 49%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 18, 5 ``function changeName(string _name) public ownerOnly returns(bool success) 
    {
        name = _name;
        emit NameChange(name);
        return true;
    }``
        - Line 24, 5 ``function changeSymbol(string _symbol) public ownerOnly returns(bool success) 
    {
        symbol = _symbol;
        emit SymbolChange(symbol);
        return true;
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

        - Line 91, 16 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
