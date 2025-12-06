# Vulnerability Analysis #
#### 2023-06-05 08:57:41 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	DAX_4000_20200618		"``
        - Line 6, 2 ``string	public		symbol =	"	DAXADH		"``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 17, 3 ``balanceOf[to]``
        - Line 25, 5 ``balances_intou2[_to]``
        - Line 46, 3 ``balanceOf[to]``

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
