# Vulnerability Analysis #
#### 2023-06-05 08:37:13 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	CAC_2400_20190919		"``
        - Line 6, 2 ``string	public		symbol =	"	CACAGC		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 26, 3 ``balanceOf[to]``
        - Line 48, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 26, 3 ``balanceOf[to] += value``
        - Line 48, 3 ``balanceOf[to] += value``

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

        - Line 11, 17 ``now``
        - Line 12, 33 ``now``
        - Line 13, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
