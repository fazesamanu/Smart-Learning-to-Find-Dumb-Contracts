# Vulnerability Analysis #
#### 2023-06-05 08:54:48 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, JUMPDEST SWAP POP PUSH CALLVALUE

        - Line 127, 25 ``now >= startTime && now <= endTime``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, CALLVALUE SWAP POP PUSH SLOAD

        - Line 82, 25 ``msg.value``

* _`X`_ TimeDep
    - 100%, DUP JUMP JUMPDEST PUSH SLOAD

        - Line 31, 3 ``uint256 public startTime``
        - Line 32, 3 ``uint256 public endTime``
        - Line 33, 3 ``uint public fundingGoal``
        - Line 35, 3 ``uint256 public price``
        - Line 39, 3 ``uint256 public stage3Bounty``
        - Line 40, 3 ``uint256 public stage4Bounty``
        - Line 41, 3 ``mapping(address => uint256) public balanceOf``

* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 48, 6 ``startTime``

* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, EQ ISZERO SWAP POP DUP

        - Line 128, 28 ``msg.value != 0``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 47, 16 ``block.timestamp``
        - Line 58, 11 ``now``
        - Line 84, 8 ``now``
        - Line 86, 14 ``now``
        - Line 88, 14 ``now``
        - Line 90, 14 ``now``
        - Line 127, 25 ``now``
        - Line 127, 45 ``now``
        - Line 132, 12 ``now``

* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 103, 21 ``msg.sender.send(amount)``
        - Line 112, 17 ``wallet.send(weiRaised)``

* __O__ BlockHash
* __O__ SelfDestruct
