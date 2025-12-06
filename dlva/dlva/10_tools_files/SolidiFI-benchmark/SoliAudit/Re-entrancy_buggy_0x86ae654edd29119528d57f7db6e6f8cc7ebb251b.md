# Vulnerability Analysis #
#### 2023-06-05 08:31:55 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	VOCC_I002_20181211		"``
        - Line 6, 3 ``string	public		symbol =	"	VOCC_I002_20181211_subDT		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 4 ``balanceOf[to]``
        - Line 47, 4 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 4 ``balanceOf[to] += value``
        - Line 47, 4 ``balanceOf[to] += value``

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

        - Line 25, 16 ``msg.sender.call.value(userBalance_re_ent12[msg.sender])("")``

* __O__ BlockHash
* __O__ SelfDestruct
