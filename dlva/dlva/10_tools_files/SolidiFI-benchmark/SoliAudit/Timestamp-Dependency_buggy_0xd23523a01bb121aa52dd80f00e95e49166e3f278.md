# Vulnerability Analysis #
#### 2023-06-05 08:40:00 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 4, 5 ``string public name``
        - Line 5, 5 ``string public symbol``

* _`X`_ Overflow
    - 100%, JUMPDEST PUSH PUSH PUSH SWAP

        - Line 67, 5 ``function appointNewcfo (address newcfo) onlycfo public returns (bool) {
        require (newcfo != address(0x0));
        require (newcfo != cfoOfTokenQUC);
        cfoOfTokenQUC = newcfo;
        return true;
    }``
        - Line 73, 5 ``function mintToken (address target, uint256 amount) onlycfo public returns (bool) {
        require (target != address(0x0));
        require (amount != 0);
        balanceOf[target] += amount;
        totalSupply += amount;
        emit MintToken (target, amount);
        return true;
    }``
        - Line 81, 5 ``function meltToken (address target, uint256 amount) onlycfo public returns (bool) {
        require (target != address(0x0));
        require (amount <= balanceOf[target]);
        require (amount != 0);
        balanceOf[target] -= amount;
        totalSupply -= amount;
        emit MeltToken (target, amount);
        return true;
    }``
        - Line 90, 5 ``function freezeAccount (address target, bool freeze) onlycfo public returns (bool) {
        require (target != address(0x0));
        frozenAccount[target] = freeze;
        emit FreezeEvent (target, freeze);
        return true;
    }``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 18, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
