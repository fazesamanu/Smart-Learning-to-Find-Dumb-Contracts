# Vulnerability Analysis #
#### 2023-06-05 08:51:42 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH SHA SLOAD ADD PUSH

        - Line 25, 33 ``totalVoting[videoNum]``
        - Line 31, 37 ``totalVoting[videoNum]``
        - Line 39, 33 ``totalVoting[videoNum]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* _`X`_ CheckEffects
    - 100%, DUP PUSH AND ORIGIN PUSH

        - Line 8, 24 ``owner_txorigin31``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 9, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
