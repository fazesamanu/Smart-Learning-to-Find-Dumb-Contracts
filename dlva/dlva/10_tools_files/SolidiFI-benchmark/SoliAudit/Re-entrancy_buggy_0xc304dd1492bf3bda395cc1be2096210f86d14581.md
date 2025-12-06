# Vulnerability Analysis #
#### 2023-06-05 08:45:19 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 5, 2 ``string	public		name =	"	CAC_2400_20190919		"``
        - Line 6, 2 ``string	public		symbol =	"	CACAGC		"``

* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 17, 3 ``balanceOf[to]``
        - Line 46, 3 ``balanceOf[to]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 17, 3 ``balanceOf[to] += value``
        - Line 46, 3 ``balanceOf[to] += value``

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

        - Line 23, 16 ``msg.sender.call.value(1 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
