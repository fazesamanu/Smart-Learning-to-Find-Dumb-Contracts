# Vulnerability Analysis #
#### 2023-05-29 11:45:59 ####

* __O__ Underflow
* _`X`_ Overflow
    - 58%, SLOAD DUP JUMP PUSH PUSH

        - Line 5, 3 ``mapping (address => uint) public tokenBalance``

    - 42%, ISZERO PUSH JUMPI DUP MLOAD

        - Line 4, 10 ``ModifierEntrancy {
  mapping (address => uint) public tokenBalance;
  string constant name = "Nu Token";
  function airDrop() hasNoBalance supportsToken ``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, DUP DUP SUB SUB DUP

        - Line 4, 13 ``ifierEn``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, POP POP POP JUMPDEST PUSH

        - Line 29, 13 ``ModifierEntrancy(msg.sender).airDrop()``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, CALL ISZERO

        - Line 11, 56 ``Bank(msg.sender).supportsToken()``
        - Line 29, 13 ``ModifierEntrancy(msg.sender).airDrop()``
        - Line 34, 9 ``ModifierEntrancy(token).airDrop()``

* __O__ BlockHash
* __O__ SelfDestruct
