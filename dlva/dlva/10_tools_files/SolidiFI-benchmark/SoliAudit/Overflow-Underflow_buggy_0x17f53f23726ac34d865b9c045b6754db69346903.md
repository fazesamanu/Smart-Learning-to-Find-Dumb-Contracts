# Vulnerability Analysis #
#### 2023-06-05 08:24:27 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* _`X`_ CallDepth
    - 100%, SLOAD PUSH SLOAD EQ ISZERO

        - Line 137, 19 ``ID_control``
        - Line 138, 20 ``Cmd_control``
        - Line 139, 36 ``Depositary_function_control``
        - Line 144, 19 ``ID_control``
        - Line 145, 20 ``Cmd_control``
        - Line 146, 36 ``Depositary_function_control``
        - Line 151, 19 ``ID_control``
        - Line 152, 20 ``Cmd_control``
        - Line 153, 36 ``Depositary_function_control``
        - Line 158, 19 ``ID_control``
        - Line 159, 20 ``Cmd_control``
        - Line 160, 36 ``Depositary_function_control``
        - Line 165, 19 ``ID_control``
        - Line 166, 20 ``Cmd_control``
        - Line 167, 36 ``Depositary_function_control``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH SLOAD PUSH SLOAD EQ

        - Line 137, 19 ``ID_control``
        - Line 138, 20 ``Cmd_control``
        - Line 139, 36 ``Depositary_function_control``
        - Line 144, 19 ``ID_control``
        - Line 145, 20 ``Cmd_control``
        - Line 146, 36 ``Depositary_function_control``
        - Line 151, 19 ``ID_control``
        - Line 152, 20 ``Cmd_control``
        - Line 153, 36 ``Depositary_function_control``
        - Line 158, 19 ``ID_control``
        - Line 159, 20 ``Cmd_control``
        - Line 160, 36 ``Depositary_function_control``
        - Line 165, 19 ``ID_control``
        - Line 166, 20 ``Cmd_control``
        - Line 167, 36 ``Depositary_function_control``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
