# Vulnerability Analysis #
#### 2023-06-05 08:50:17 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	RE_Portfolio_XVIII_883		"``
        - Line 6, 3 ``string	public		symbol =	"	RE883XVIII		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 4 ``balanceOf[to]``
        - Line 41, 4 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 4 ``balanceOf[to] += value``
        - Line 41, 4 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
