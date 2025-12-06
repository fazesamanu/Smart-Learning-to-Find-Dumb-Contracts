# Vulnerability Analysis #
#### 2023-06-05 08:36:19 ####

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

* _`X`_ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, CALL ISZERO

        - Line 136, 13 ``Securities_1.transfer(User_1, Standard_1)``
        - Line 143, 13 ``Securities_2.transfer(User_2, Standard_2)``
        - Line 150, 13 ``Securities_3.transfer(User_3, Standard_3)``
        - Line 157, 13 ``Securities_4.transfer(User_4, Standard_4)``
        - Line 164, 13 ``Securities_5.transfer(User_5, Standard_5)``

* __O__ BlockHash
* __O__ SelfDestruct
