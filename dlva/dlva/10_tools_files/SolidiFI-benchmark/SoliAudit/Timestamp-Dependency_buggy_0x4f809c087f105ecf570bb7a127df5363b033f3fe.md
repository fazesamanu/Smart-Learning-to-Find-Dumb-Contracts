# Vulnerability Analysis #
#### 2023-06-05 08:43:41 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	NIGERIA_WINS		"``
        - Line 6, 2 ``string	public		symbol =	"	NIGWII		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 20, 3 ``balanceOf[to]``
        - Line 42, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 20, 3 ``balanceOf[to] += value``
        - Line 42, 3 ``balanceOf[to] += value``

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
