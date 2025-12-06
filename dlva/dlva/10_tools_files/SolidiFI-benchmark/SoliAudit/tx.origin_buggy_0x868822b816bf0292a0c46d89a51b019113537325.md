# Vulnerability Analysis #
#### 2023-06-05 08:57:46 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	MOROCCO_WINS		"``
        - Line 6, 2 ``string	public		symbol =	"	MORWII		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 3 ``balanceOf[to]``
        - Line 42, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 3 ``balanceOf[to] += value``
        - Line 42, 3 ``balanceOf[to] += value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* _`X`_ CheckEffects
    - 100%, DUP PUSH AND ORIGIN PUSH

        - Line 21, 24 ``owner_txorigin35``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 22, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
