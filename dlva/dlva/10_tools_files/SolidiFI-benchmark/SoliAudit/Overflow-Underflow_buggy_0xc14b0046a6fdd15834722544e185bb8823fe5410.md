# Vulnerability Analysis #
#### 2023-06-05 08:40:49 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 174, 3 ``return	inData_1``
        - Line 181, 3 ``return	inData_2``
        - Line 188, 3 ``return	inData_3``
        - Line 195, 3 ``return	inData_4``
        - Line 202, 3 ``return	inData_5``
        - Line 209, 3 ``return	inData_6``
        - Line 216, 3 ``return	inData_7``
        - Line 223, 3 ``return	inData_8``
        - Line 230, 3 ``return	inData_9``
        - Line 237, 3 ``return	inData_10``

* _`X`_ Overflow
    - 100%, SWAP DUP ADD DUP CALLDATALOAD

        - Line 170, 2 ``function	setData_1	(	string	newData_1	)	public	onlyOwner	{		
		inData_1	=	newData_1	;						
	}``
        - Line 177, 2 ``function	setData_2	(	string	newData_2	)	public	onlyOwner	{		
		inData_2	=	newData_2	;						
	}``
        - Line 184, 2 ``function	setData_3	(	string	newData_3	)	public	onlyOwner	{		
		inData_3	=	newData_3	;						
	}``
        - Line 191, 2 ``function	setData_4	(	string	newData_4	)	public	onlyOwner	{		
		inData_4	=	newData_4	;						
	}``
        - Line 198, 2 ``function	setData_5	(	string	newData_5	)	public	onlyOwner	{		
		inData_5	=	newData_5	;						
	}``
        - Line 205, 2 ``function	setData_6	(	string	newData_6	)	public	onlyOwner	{		
		inData_6	=	newData_6	;						
	}``
        - Line 212, 2 ``function	setData_7	(	string	newData_7	)	public	onlyOwner	{		
		inData_7	=	newData_7	;						
	}``
        - Line 219, 2 ``function	setData_8	(	string	newData_8	)	public	onlyOwner	{		
		inData_8	=	newData_8	;						
	}``
        - Line 226, 2 ``function	setData_9	(	string	newData_9	)	public	onlyOwner	{		
		inData_9	=	newData_9	;						
	}``
        - Line 233, 2 ``function	setData_10	(	string	newData_10	)	public	onlyOwner	{		
		inData_10	=	newData_10	;						
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
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
