# Vulnerability Analysis #
#### 2023-06-05 08:24:17 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, SSTORE POP PUSH DUP PUSH

        - Line 59, 3 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 68, 3 ``balances[_from] = balances[_from].sub(_value)``
        - Line 69, 3 ``balances[_to] = balances[_to].add(_value)``

    - 48%, PUSH SHA SLOAD PUSH SWAP

        - Line 59, 26 ``balances[msg.sender]``
        - Line 60, 19 ``balances[_to]``
        - Line 68, 21 ``balances[_from]``
        - Line 69, 19 ``balances[_to]``
        - Line 70, 32 ``allowed[_from][msg.sender]``
        - Line 83, 35 ``allowed[msg.sender][_spender]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPDEST PUSH PUSH CALLVALUE EQ

        - Line 33, 68 ``function bug_tmstmp28 () public payable {
	uint pastBlockTime_tmstmp28; // Forces one bet per block
	require(msg.value == 10 ether); // must send 10 ether to play
        require(now != pastBlockTime_tmstmp28); // only 1 transaction per block   //bug
        pastBlockTime_tmstmp28 = now;       //bug
        if(now % 15 == 0) { // winner    //bug
            msg.sender.transfer(address(this).balance);
        }
    }``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 36, 17 ``now``
        - Line 37, 34 ``now``
        - Line 38, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
