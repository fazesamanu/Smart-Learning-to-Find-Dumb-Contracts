# Vulnerability Analysis #
#### 2023-06-05 08:42:09 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	NIGERIA_WINS		"``
        - Line 6, 2 ``string	public		symbol =	"	NIGWI		"``

* _`X`_ Overflow
    - 100%, PUSH DUP DUP SLOAD ADD

        - Line 17, 3 ``balanceOf[to]``
        - Line 26, 9 ``counter_re_ent7``
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
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 23, 9 ``msg.sender.call.value(10 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
