# Vulnerability Analysis #
#### 2023-05-29 11:47:13 ####

* __O__ Underflow
* _`X`_ Overflow
    - 52%, PUSH DUP DUP SLOAD ADD

        - Line 10, 10 ``userBalance[msg.sender]``

    - 48%, SLOAD ADD SWAP POP POP

        - Line 10, 10 ``userBalance[msg.sender] += msg.value``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* _`X`_ Reentrancy
    - 100%, SSTORE POP JUMP JUMPDEST CALLVALUE

        - Line 16, 10 ``userBalance[msg.sender] = 0``

* __O__ AssertFail
* __O__ TxOrigin
* _`X`_ CheckEffects
    - 100%, JUMP JUMPDEST CALLVALUE PUSH DUP

        - Line 12, 6 ``function withdrawBalance(){
         if( ! (msg.sender.call.value(userBalance[msg.sender])() ) ){
             throw;
         }
         userBalance[msg.sender] = 0;
     }``

* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 13, 17 ``msg.sender.call.value(userBalance[msg.sender])()``

* __O__ BlockHash
* __O__ SelfDestruct
