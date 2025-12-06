# Vulnerability Analysis #
#### 2023-06-05 09:01:54 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* _`X`_ CallDepth
    - 100%, SLOAD PUSH SLOAD EQ ISZERO

        - Line 138, 19 ``ID_control``
        - Line 139, 20 ``Cmd_control``
        - Line 140, 36 ``Depositary_function_control``
        - Line 145, 19 ``ID_control``
        - Line 146, 20 ``Cmd_control``
        - Line 147, 36 ``Depositary_function_control``
        - Line 152, 19 ``ID_control``
        - Line 153, 20 ``Cmd_control``
        - Line 154, 36 ``Depositary_function_control``
        - Line 159, 19 ``ID_control``
        - Line 160, 20 ``Cmd_control``
        - Line 161, 36 ``Depositary_function_control``
        - Line 166, 19 ``ID_control``
        - Line 167, 20 ``Cmd_control``
        - Line 168, 36 ``Depositary_function_control``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH SLOAD PUSH SLOAD EQ

        - Line 138, 19 ``ID_control``
        - Line 139, 20 ``Cmd_control``
        - Line 140, 36 ``Depositary_function_control``
        - Line 145, 19 ``ID_control``
        - Line 146, 20 ``Cmd_control``
        - Line 147, 36 ``Depositary_function_control``
        - Line 152, 19 ``ID_control``
        - Line 153, 20 ``Cmd_control``
        - Line 154, 36 ``Depositary_function_control``
        - Line 159, 19 ``ID_control``
        - Line 160, 20 ``Cmd_control``
        - Line 161, 36 ``Depositary_function_control``
        - Line 166, 19 ``ID_control``
        - Line 167, 20 ``Cmd_control``
        - Line 168, 36 ``Depositary_function_control``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 171, 12 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
