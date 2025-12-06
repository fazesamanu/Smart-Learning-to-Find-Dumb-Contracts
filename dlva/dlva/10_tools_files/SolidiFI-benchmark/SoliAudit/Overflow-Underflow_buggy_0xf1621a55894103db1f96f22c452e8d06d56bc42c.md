# Vulnerability Analysis #
#### 2023-06-05 08:41:29 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 58, 5 ``string public name = "Goldglp"``
        - Line 60, 5 ``string public symbol = "GLP"``

* __O__ Overflow
* __O__ Multisig
* _`X`_ CallDepth
    - 100%, PUSH JUMPI PUSH MLOAD PUSH

        - Line 74, 9 ``require(msg.sender == _owner, "Not an admin")``
        - Line 95, 9 ``require(!_notransferible[from], "No authorized ejecutor")``
        - Line 96, 9 ``require(value <= _balances[from], "Not enough balance")``
        - Line 97, 9 ``require(to != address(0), "Invalid account")``
        - Line 103, 9 ``require(spender != address(0), "Invalid account")``
        - Line 116, 9 ``require(value <= _allowed[from][msg.sender], "Not enough approved ammount")``
        - Line 128, 9 ``require(spender != address(0), "Invalid account")``
        - Line 141, 9 ``require(spender != address(0), "Invalid account")``
        - Line 160, 9 ``require(_administradores[admin], "Not an admin")``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, ADD DUP DUP PUSH ADD

        - Line 74, 9 ``require(msg.sender == _owner, "Not an admin")``
        - Line 95, 9 ``require(!_notransferible[from], "No authorized ejecutor")``
        - Line 96, 9 ``require(value <= _balances[from], "Not enough balance")``
        - Line 97, 9 ``require(to != address(0), "Invalid account")``
        - Line 103, 9 ``require(spender != address(0), "Invalid account")``
        - Line 116, 9 ``require(value <= _allowed[from][msg.sender], "Not enough approved ammount")``
        - Line 128, 9 ``require(spender != address(0), "Invalid account")``
        - Line 141, 9 ``require(spender != address(0), "Invalid account")``
        - Line 160, 9 ``require(_administradores[admin], "Not an admin")``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
