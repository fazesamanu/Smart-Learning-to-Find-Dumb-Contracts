# Vulnerability Analysis #
#### 2023-05-29 09:08:07 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* _`X`_ CallDepth
    - 100%, PUSH JUMPI PUSH MLOAD PUSH

        - Line 14, 9 ``require(msg.sender == owner, "Permission Denied.")``
        - Line 15, 9 ``require(evidenceList[id].hash == 0x0, "Evidence exists.")``
        - Line 16, 9 ``require(evidenceList[id].time == 0, "Evidence exists.")``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
