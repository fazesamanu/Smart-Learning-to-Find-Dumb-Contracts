# Vulnerability Analysis #
#### 2023-06-05 08:39:55 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 21, 63 ``keccak256(bytes((_ethToSphtx[msg.sender])))``
        - Line 22, 62 ``keccak256(bytes((_ethToSphtx[msg.sender])))``
        - Line 28, 9 ``return _ethToSphtx[addr]``
        - Line 31, 9 ``return _accountToPubKey[_ethToSphtx[addr]]``
        - Line 31, 16 ``_accountToPubKey[_ethToSphtx[addr]]``

* _`X`_ Overflow
    - 100%, ISZERO PUSH JUMPI JUMPDEST SWAP

        - Line 16, 19 ``b[0]``
        - Line 16, 33 ``b[0]``
        - Line 16, 49 ``b[0]``
        - Line 16, 63 ``b[0]``
        - Line 18, 23 ``b[i]``
        - Line 18, 37 ``b[i]``
        - Line 18, 53 ``b[i]``
        - Line 18, 67 ``b[i]``
        - Line 18, 83 ``b[i]``
        - Line 18, 98 ``b[i]``
        - Line 39, 14 ``b[0]``
        - Line 39, 28 ``b[0]``
        - Line 39, 45 ``b[0]``
        - Line 39, 59 ``b[0]``
        - Line 42, 17 ``b[0]``
        - Line 42, 31 ``b[0]``
        - Line 42, 48 ``b[0]``
        - Line 42, 62 ``b[0]``
        - Line 42, 78 ``b[i]``
        - Line 42, 93 ``b[i]``

* __O__ Multisig
* __O__ CallDepth
* _`X`_ TOD
    - 100%, NOT AND GT JUMPDEST DUP

        - Line 39, 28 ``b[0] > 'z'``
        - Line 42, 31 ``b[0] > 'z'``

* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, NOT AND GT JUMPDEST DUP

        - Line 39, 28 ``b[0] > 'z'``
        - Line 42, 31 ``b[0] > 'z'``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
