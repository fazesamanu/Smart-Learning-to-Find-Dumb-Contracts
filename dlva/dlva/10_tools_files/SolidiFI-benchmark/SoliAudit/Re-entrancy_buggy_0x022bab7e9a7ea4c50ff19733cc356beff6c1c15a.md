# Vulnerability Analysis #
#### 2023-06-05 08:33:59 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, ISZERO PUSH JUMPI JUMPDEST SWAP

        - Line 9, 2 ``GameInfo[] public games``
        - Line 34, 3 ``games[gameNum]``
        - Line 34, 25 ``games[gameNum]``
        - Line 35, 3 ``games[gameNum]``
        - Line 37, 7 ``games[gameNum]``
        - Line 39, 4 ``games[gameNum]``
        - Line 39, 31 ``games[gameNum]``
        - Line 40, 4 ``games[gameNum]``
        - Line 40, 31 ``games[gameNum]``
        - Line 41, 4 ``games[gameNum]``
        - Line 41, 31 ``games[gameNum]``
        - Line 42, 18 ``games[gameNum]``
        - Line 43, 18 ``games[gameNum]``
        - Line 44, 18 ``games[gameNum]``
        - Line 47, 29 ``games[gameNum]``
        - Line 70, 28 ``games[lastGame[msg.sender]]``
        - Line 81, 28 ``games[gameNum]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, SSTORE POP POP POP JUMPDEST

        - Line 56, 4 ``games.push(GameInfo(0))``

* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, AND PUSH PUSH SLOAD DUP

        - Line 39, 31 ``games[gameNum].funder[winNum]``
        - Line 40, 31 ``games[gameNum].funder[(winNum+3)%10]``
        - Line 41, 31 ``games[gameNum].funder[(winNum+6)%10]``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 38, 19 ``now``

* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 66, 9 ``msg.sender.transfer(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
