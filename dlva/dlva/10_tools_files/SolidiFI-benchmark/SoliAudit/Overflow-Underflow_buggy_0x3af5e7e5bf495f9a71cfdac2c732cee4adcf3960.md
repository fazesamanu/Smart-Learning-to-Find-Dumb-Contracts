# Vulnerability Analysis #
#### 2023-06-05 08:52:47 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	RUSS_PFXXII_I_883		"``
        - Line 6, 3 ``string	public		symbol =	"	RUSS_PFXXII_I_IMTD		"``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 17, 4 ``balanceOf[to]``
        - Line 26, 5 ``balances_intou2[_to]``
        - Line 46, 4 ``balanceOf[to]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
