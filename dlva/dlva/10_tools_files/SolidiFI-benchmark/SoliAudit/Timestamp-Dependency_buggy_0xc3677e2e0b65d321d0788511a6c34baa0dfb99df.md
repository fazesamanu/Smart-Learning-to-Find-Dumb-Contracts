# Vulnerability Analysis #
#### 2023-06-05 08:22:54 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 26, 2 ``string public standard = 'Sent 2.0'``

* _`X`_ Overflow
    - 52%, SSTORE POP PUSH DUP PUSH

        - Line 65, 9 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 73, 9 ``balances[_to] = balances[_to].add(_value)``

    - 48%, PUSH SHA SLOAD PUSH SWAP

        - Line 65, 32 ``balances[msg.sender]``
        - Line 66, 25 ``balances[_to]``
        - Line 73, 25 ``balances[_to]``
        - Line 74, 27 ``balances[_from]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPDEST PUSH PUSH CALLVALUE EQ

        - Line 34, 3 ``function bug_tmstmp28 () public payable {
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

        - Line 37, 17 ``now``
        - Line 38, 34 ``now``
        - Line 39, 12 ``now``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
