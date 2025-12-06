# Vulnerability Analysis #
#### 2023-06-05 08:59:24 ####

* __O__ Underflow
* _`X`_ Overflow
    - 50%, OR SWAP SSTORE POP DUP

        - Line 86, 5 ``User_1		=	_User_1``
        - Line 87, 5 ``Police_1		=	_Police_1``
        - Line 97, 5 ``User_2		=	_User_2``
        - Line 98, 5 ``Police_2		=	_Police_2``
        - Line 108, 5 ``User_3		=	_User_3``
        - Line 109, 5 ``Police_3		=	_Police_3``
        - Line 119, 5 ``User_4		=	_User_4``
        - Line 120, 5 ``Police_4		=	_Police_4``
        - Line 130, 5 ``User_5		=	_User_5``
        - Line 131, 5 ``Police_5		=	_Police_5``

    - 50%, JUMPDEST JUMP JUMPDEST PUSH PUSH

        - Line 146, 5 ``require(	Ouverture_des_droits == Ouverture_effective			)``
        - Line 160, 5 ``require(	Ouverture_des_droits == Ouverture_effective			)``

* __O__ Multisig
* _`X`_ CallDepth
    - 100%, SLOAD PUSH SLOAD EQ ISZERO

        - Line 137, 26 ``Sinistre_effectif``
        - Line 138, 29 ``Realisation_effective``
        - Line 139, 38 ``Ouverture_effective``
        - Line 144, 26 ``Sinistre_effectif``
        - Line 145, 29 ``Realisation_effective``
        - Line 146, 38 ``Ouverture_effective``
        - Line 151, 26 ``Sinistre_effectif``
        - Line 152, 29 ``Realisation_effective``
        - Line 153, 38 ``Ouverture_effective``
        - Line 158, 26 ``Sinistre_effectif``
        - Line 159, 29 ``Realisation_effective``
        - Line 160, 38 ``Ouverture_effective``
        - Line 165, 26 ``Sinistre_effectif``
        - Line 166, 29 ``Realisation_effective``
        - Line 167, 38 ``Ouverture_effective``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH SLOAD PUSH SLOAD EQ

        - Line 137, 26 ``Sinistre_effectif``
        - Line 138, 29 ``Realisation_effective``
        - Line 139, 38 ``Ouverture_effective``
        - Line 144, 26 ``Sinistre_effectif``
        - Line 145, 29 ``Realisation_effective``
        - Line 146, 38 ``Ouverture_effective``
        - Line 151, 26 ``Sinistre_effectif``
        - Line 152, 29 ``Realisation_effective``
        - Line 153, 38 ``Ouverture_effective``
        - Line 158, 26 ``Sinistre_effectif``
        - Line 159, 29 ``Realisation_effective``
        - Line 160, 38 ``Ouverture_effective``
        - Line 165, 26 ``Sinistre_effectif``
        - Line 166, 29 ``Realisation_effective``
        - Line 167, 38 ``Ouverture_effective``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* __O__ BlockTimestamp
* _`X`_ LowlevelCalls
    - 100%, GAS CALL

        - Line 136, 14 ``Police_1.transfer(User_1, Standard_1)``
        - Line 143, 14 ``Police_2.transfer(User_1, Standard_2)``
        - Line 150, 14 ``Police_3.transfer(User_1, Standard_3)``
        - Line 157, 14 ``Police_4.transfer(User_1, Standard_4)``
        - Line 164, 14 ``Police_5.transfer(User_1, Standard_5)``
        - Line 172, 16 ``msg.sender.call.value(1 ether)("")``

* __O__ BlockHash
* __O__ SelfDestruct
