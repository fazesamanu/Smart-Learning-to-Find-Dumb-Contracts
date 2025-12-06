# Vulnerability Analysis #
#### 2023-06-05 08:50:12 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	ADIDAS_AG		"``
        - Line 6, 2 ``string	public		symbol =	"	ADIDI		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 3 ``balanceOf[to]``
        - Line 47, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 3 ``balanceOf[to] += value``
        - Line 47, 3 ``balanceOf[to] += value``

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
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 24, 16 ``msg.sender.call.value(userBalance_re_ent19[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
