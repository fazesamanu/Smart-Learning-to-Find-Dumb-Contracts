# Vulnerability Analysis #
#### 2023-06-05 08:46:38 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	SHERE_PFIII_III_883		"``
        - Line 6, 3 ``string	public		symbol =	"	SHERE_PFIII_III_IMTD		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 26, 4 ``balanceOf[to]``
        - Line 48, 4 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 26, 4 ``balanceOf[to] += value``
        - Line 48, 4 ``balanceOf[to] += value``

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

        - Line 12, 17 ``now``
        - Line 13, 33 ``now``
        - Line 14, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
