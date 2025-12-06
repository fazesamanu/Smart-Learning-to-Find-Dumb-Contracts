# Vulnerability Analysis #
#### 2023-06-05 08:40:06 ####

* __O__ Underflow
* _`X`_ Overflow
    - 100%, PUSH SLOAD SWAP POP SWAP

        - Line 17, 10 ``inData_1``
        - Line 24, 10 ``inData_2``
        - Line 31, 10 ``inData_3``
        - Line 38, 10 ``inData_4``
        - Line 45, 10 ``inData_5``
        - Line 52, 10 ``inData_6``
        - Line 59, 10 ``inData_7``
        - Line 66, 10 ``inData_8``
        - Line 73, 10 ``inData_9``
        - Line 80, 10 ``inData_10``
        - Line 87, 10 ``inData_11``
        - Line 94, 10 ``inData_12``
        - Line 101, 10 ``inData_13``
        - Line 108, 10 ``inData_14``
        - Line 115, 10 ``inData_15``
        - Line 122, 10 ``inData_16``
        - Line 129, 10 ``inData_17``
        - Line 136, 10 ``inData_18``
        - Line 143, 10 ``inData_19``
        - Line 150, 10 ``inData_20``
        - Line 157, 10 ``inData_21``
        - Line 164, 10 ``inData_22``
        - Line 171, 10 ``inData_23``
        - Line 178, 10 ``inData_24``
        - Line 185, 10 ``inData_25``
        - Line 192, 10 ``inData_26``
        - Line 199, 10 ``inData_27``
        - Line 206, 10 ``inData_28``
        - Line 213, 10 ``inData_29``
        - Line 220, 10 ``inData_30``
        - Line 227, 10 ``inData_31``
        - Line 234, 10 ``inData_32``
        - Line 241, 10 ``inData_33``
        - Line 248, 10 ``inData_34``
        - Line 255, 10 ``inData_35``
        - Line 262, 10 ``inData_36``
        - Line 269, 10 ``inData_37``
        - Line 276, 10 ``inData_38``
        - Line 283, 10 ``inData_39``
        - Line 290, 10 ``inData_40``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* __O__ AssertFail
* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, DUP CALL

        - Line 294, 3 ``to.send(amount)``

* __O__ BlockHash
* __O__ SelfDestruct
