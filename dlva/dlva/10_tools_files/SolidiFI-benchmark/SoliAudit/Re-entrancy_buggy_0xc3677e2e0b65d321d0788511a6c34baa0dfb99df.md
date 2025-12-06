# Vulnerability Analysis #
#### 2023-06-05 08:36:25 ####

* _`X`_ Underflow
    - 100%, SLOAD DIV

        - Line 26, 2 ``string public standard = 'Sent 2.0'``

* _`X`_ Overflow
    - 52%, SSTORE POP PUSH DUP PUSH

        - Line 63, 9 ``balances[msg.sender] = balances[msg.sender].sub(_value)``
        - Line 71, 9 ``balances[_to] = balances[_to].add(_value)``

    - 48%, PUSH SHA SLOAD PUSH SWAP

        - Line 63, 32 ``balances[msg.sender]``
        - Line 64, 25 ``balances[_to]``
        - Line 71, 25 ``balances[_to]``
        - Line 72, 27 ``balances[_from]``

* __O__ Multisig
* __O__ CallDepth
* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, JUMPI JUMPDEST DUP DUP SUB

        - Line 16, 9 ``assert(b <= a)``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 38, 16 ``msg.sender.call.value(1 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
