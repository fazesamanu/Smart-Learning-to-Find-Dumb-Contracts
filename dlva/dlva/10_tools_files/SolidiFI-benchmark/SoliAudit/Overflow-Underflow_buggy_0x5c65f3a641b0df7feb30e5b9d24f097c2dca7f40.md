# Vulnerability Analysis #
#### 2023-06-05 08:30:39 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 17, 3 ``return	inMiniPoolEdit_1``
        - Line 24, 3 ``return	inMiniPoolEdit_2``
        - Line 31, 3 ``return	inMiniPoolEdit_3``
        - Line 38, 3 ``return	inMiniPoolEdit_4``
        - Line 45, 3 ``return	inMiniPoolEdit_5``
        - Line 52, 3 ``return	inMiniPoolEdit_6``
        - Line 59, 3 ``return	inMiniPoolEdit_7``
        - Line 66, 3 ``return	inMiniPoolEdit_8``
        - Line 73, 3 ``return	inMiniPoolEdit_9``

* _`X`_ Overflow
    - 100%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 13, 2 ``function	setMiniPoolEdit_1	(	string	newMiniPoolEdit_1	)	public	onlyOwner	{	
		inMiniPoolEdit_1	=	newMiniPoolEdit_1	;					
	}``
        - Line 20, 2 ``function	setMiniPoolEdit_2	(	string	newMiniPoolEdit_2	)	public	onlyOwner	{	
		inMiniPoolEdit_2	=	newMiniPoolEdit_2	;					
	}``
        - Line 27, 2 ``function	setMiniPoolEdit_3	(	string	newMiniPoolEdit_3	)	public	onlyOwner	{	
		inMiniPoolEdit_3	=	newMiniPoolEdit_3	;					
	}``
        - Line 34, 2 ``function	setMiniPoolEdit_4	(	string	newMiniPoolEdit_4	)	public	onlyOwner	{	
		inMiniPoolEdit_4	=	newMiniPoolEdit_4	;					
	}``
        - Line 41, 2 ``function	setMiniPoolEdit_5	(	string	newMiniPoolEdit_5	)	public	onlyOwner	{	
		inMiniPoolEdit_5	=	newMiniPoolEdit_5	;					
	}``
        - Line 48, 2 ``function	setMiniPoolEdit_6	(	string	newMiniPoolEdit_6	)	public	onlyOwner	{	
		inMiniPoolEdit_6	=	newMiniPoolEdit_6	;					
	}``
        - Line 55, 2 ``function	setMiniPoolEdit_7	(	string	newMiniPoolEdit_7	)	public	onlyOwner	{	
		inMiniPoolEdit_7	=	newMiniPoolEdit_7	;					
	}``
        - Line 62, 2 ``function	setMiniPoolEdit_8	(	string	newMiniPoolEdit_8	)	public	onlyOwner	{	
		inMiniPoolEdit_8	=	newMiniPoolEdit_8	;					
	}``
        - Line 69, 2 ``function	setMiniPoolEdit_9	(	string	newMiniPoolEdit_9	)	public	onlyOwner	{	
		inMiniPoolEdit_9	=	newMiniPoolEdit_9	;					
	}``

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

        - Line 81, 17 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
