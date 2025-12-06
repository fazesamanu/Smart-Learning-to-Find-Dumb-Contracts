# Vulnerability Analysis #
#### 2023-06-05 08:25:21 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	RUSS_PFXXXI_III_883		"``
        - Line 6, 3 ``string	public		symbol =	"	RUSS_PFXXXI_III_IMTD		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 20, 4 ``balanceOf[to]``
        - Line 42, 4 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 20, 4 ``balanceOf[to] += value``
        - Line 42, 4 ``balanceOf[to] += value``

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
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
