# Vulnerability Analysis #
#### 2023-06-05 08:36:14 ####

* __O__ Underflow
* __O__ Overflow
* __O__ Multisig
* _`X`_ CallDepth
    - 100%, SLOAD PUSH SLOAD EQ ISZERO

        - Line 137, 18 ``ID_control``
        - Line 138, 19 ``Cmd_control``
        - Line 139, 35 ``Depositary_function_control``
        - Line 144, 18 ``ID_control``
        - Line 145, 19 ``Cmd_control``
        - Line 146, 35 ``Depositary_function_control``
        - Line 151, 18 ``ID_control``
        - Line 152, 19 ``Cmd_control``
        - Line 153, 35 ``Depositary_function_control``
        - Line 158, 18 ``ID_control``
        - Line 159, 19 ``Cmd_control``
        - Line 160, 35 ``Depositary_function_control``
        - Line 165, 18 ``ID_control``
        - Line 166, 19 ``Cmd_control``
        - Line 167, 35 ``Depositary_function_control``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH SLOAD PUSH SLOAD EQ

        - Line 137, 18 ``ID_control``
        - Line 138, 19 ``Cmd_control``
        - Line 139, 35 ``Depositary_function_control``
        - Line 144, 18 ``ID_control``
        - Line 145, 19 ``Cmd_control``
        - Line 146, 35 ``Depositary_function_control``
        - Line 151, 18 ``ID_control``
        - Line 152, 19 ``Cmd_control``
        - Line 153, 35 ``Depositary_function_control``
        - Line 158, 18 ``ID_control``
        - Line 159, 19 ``Cmd_control``
        - Line 160, 35 ``Depositary_function_control``
        - Line 165, 18 ``ID_control``
        - Line 166, 19 ``Cmd_control``
        - Line 167, 35 ``Depositary_function_control``

* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
