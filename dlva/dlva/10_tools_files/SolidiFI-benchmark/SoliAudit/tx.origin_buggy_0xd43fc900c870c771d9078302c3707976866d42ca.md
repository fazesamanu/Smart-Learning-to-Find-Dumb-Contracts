# Vulnerability Analysis #
#### 2023-06-05 08:49:11 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	NDD_WPO_I_883		"``
        - Line 6, 3 ``string	public		symbol =	"	NDD_WPO_I_1subDT		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 4 ``balanceOf[to]``
        - Line 42, 4 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 4 ``balanceOf[to] += value``
        - Line 42, 4 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* _`X`_ CheckEffects
    - 100%, DUP PUSH AND ORIGIN PUSH

        - Line 22, 24 ``owner_txorigin15``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 23, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
