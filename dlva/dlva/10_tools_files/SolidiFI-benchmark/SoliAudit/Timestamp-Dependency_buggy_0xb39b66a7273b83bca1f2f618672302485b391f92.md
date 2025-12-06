# Vulnerability Analysis #
#### 2023-06-05 08:53:03 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	ANHUI_ANNUITY_DAO_33_c		"``
        - Line 6, 2 ``string	public		symbol =	"	AAII		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 22, 3 ``balanceOf[to]``
        - Line 44, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 22, 3 ``balanceOf[to] += value``
        - Line 44, 3 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, DUP ADD EQ ISZERO PUSH

        - Line 11, 6 ``startTime``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
