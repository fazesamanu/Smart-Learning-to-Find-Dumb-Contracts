# Vulnerability Analysis #
#### 2023-06-05 08:28:02 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 16, 63 ``keccak256(bytes((_ethToSphtx[msg.sender])))``
        - Line 17, 62 ``keccak256(bytes((_ethToSphtx[msg.sender])))``
        - Line 23, 9 ``return _ethToSphtx[addr]``
        - Line 26, 9 ``return _accountToPubKey[_ethToSphtx[addr]]``
        - Line 26, 16 ``_accountToPubKey[_ethToSphtx[addr]]``

* _`X`_ Overflow
    - 100%, ISZERO PUSH JUMPI JUMPDEST SWAP

        - Line 11, 19 ``b[0]``
        - Line 11, 33 ``b[0]``
        - Line 11, 49 ``b[0]``
        - Line 11, 63 ``b[0]``
        - Line 13, 23 ``b[i]``
        - Line 13, 37 ``b[i]``
        - Line 13, 53 ``b[i]``
        - Line 13, 67 ``b[i]``
        - Line 13, 83 ``b[i]``
        - Line 13, 98 ``b[i]``
        - Line 34, 14 ``b[0]``
        - Line 34, 28 ``b[0]``
        - Line 34, 45 ``b[0]``
        - Line 34, 59 ``b[0]``
        - Line 37, 17 ``b[0]``
        - Line 37, 31 ``b[0]``
        - Line 37, 48 ``b[0]``
        - Line 37, 62 ``b[0]``
        - Line 37, 78 ``b[i]``
        - Line 37, 93 ``b[i]``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, NOT AND GT JUMPDEST DUP

        - Line 34, 28 ``b[0] > 'z'``
        - Line 37, 31 ``b[0] > 'z'``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, NOT AND GT JUMPDEST DUP

        - Line 34, 28 ``b[0] > 'z'``
        - Line 37, 31 ``b[0] > 'z'``

* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 43, 16 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
