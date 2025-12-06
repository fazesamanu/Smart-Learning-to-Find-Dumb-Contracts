# Vulnerability Analysis #
#### 2023-06-05 08:48:22 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	VOCC_I086_20181211		"``
        - Line 6, 3 ``string	public		symbol =	"	VOCC_I086_20181211_subDT		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 22, 4 ``balanceOf[to]``
        - Line 44, 4 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 22, 4 ``balanceOf[to] += value``
        - Line 44, 4 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 12, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
