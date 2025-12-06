# Vulnerability Analysis #
#### 2023-06-05 08:55:16 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 3 ``string	public		name =	"	SHERE_PFVII_883		"``
        - Line 6, 3 ``string	public		symbol =	"	SHERE_PFVII_IMTD		"``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 17, 4 ``balanceOf[to]``
        - Line 27, 9 ``counter_re_ent35``
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
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 24, 9 ``msg.sender.call.value(10 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
