# Vulnerability Analysis #
#### 2023-06-05 08:34:53 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 7, 2 ``string	public		name =	"	NDD_RUSAL_I_883o		"``
        - Line 8, 2 ``string	public		symbol =	"	NDD_RUSAL_I_1subDTo		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 19, 3 ``balanceOf[to]``
        - Line 44, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 19, 3 ``balanceOf[to] += value``
        - Line 44, 3 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* _`X`_ CheckEffects
    - 100%, DUP PUSH AND ORIGIN PUSH

        - Line 23, 24 ``owner_txorigin35``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 24, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
