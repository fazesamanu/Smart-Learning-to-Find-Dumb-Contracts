# Vulnerability Analysis #
#### 2023-06-05 08:42:20 ####

* __O__ Underflow
* _`X`_ Overflow
    - 50%, OR SWAP SSTORE POP DUP

        - Line 87, 5 ``User_1		=	_User_1``
        - Line 88, 5 ``Police_1		=	_Police_1``
        - Line 98, 5 ``User_2		=	_User_2``
        - Line 99, 5 ``Police_2		=	_Police_2``
        - Line 109, 5 ``User_3		=	_User_3``
        - Line 110, 5 ``Police_3		=	_Police_3``
        - Line 120, 5 ``User_4		=	_User_4``
        - Line 121, 5 ``Police_4		=	_Police_4``
        - Line 131, 5 ``User_5		=	_User_5``
        - Line 132, 5 ``Police_5		=	_Police_5``

    - 50%, JUMPDEST JUMP JUMPDEST PUSH PUSH

        - Line 147, 5 ``require(	Ouverture_des_droits == Ouverture_effective			)``
        - Line 161, 5 ``require(	Ouverture_des_droits == Ouverture_effective			)``

* __O__ Multisig
* _`X`_ CallDepth
    - 100%, SLOAD PUSH SLOAD EQ ISZERO

        - Line 138, 26 ``Sinistre_effectif``
        - Line 139, 29 ``Realisation_effective``
        - Line 140, 38 ``Ouverture_effective``
        - Line 145, 26 ``Sinistre_effectif``
        - Line 146, 29 ``Realisation_effective``
        - Line 147, 38 ``Ouverture_effective``
        - Line 152, 26 ``Sinistre_effectif``
        - Line 153, 29 ``Realisation_effective``
        - Line 154, 38 ``Ouverture_effective``
        - Line 159, 26 ``Sinistre_effectif``
        - Line 160, 29 ``Realisation_effective``
        - Line 161, 38 ``Ouverture_effective``
        - Line 166, 26 ``Sinistre_effectif``
        - Line 167, 29 ``Realisation_effective``
        - Line 168, 38 ``Ouverture_effective``

* __O__ TOD
* __O__ TimeDep
* __O__ Reentrancy
* _`X`_ AssertFail
    - 100%, PUSH SLOAD PUSH SLOAD EQ

        - Line 138, 26 ``Sinistre_effectif``
        - Line 139, 29 ``Realisation_effective``
        - Line 140, 38 ``Ouverture_effective``
        - Line 145, 26 ``Sinistre_effectif``
        - Line 146, 29 ``Realisation_effective``
        - Line 147, 38 ``Ouverture_effective``
        - Line 152, 26 ``Sinistre_effectif``
        - Line 153, 29 ``Realisation_effective``
        - Line 154, 38 ``Ouverture_effective``
        - Line 159, 26 ``Sinistre_effectif``
        - Line 160, 29 ``Realisation_effective``
        - Line 161, 38 ``Ouverture_effective``
        - Line 166, 26 ``Sinistre_effectif``
        - Line 167, 29 ``Realisation_effective``
        - Line 168, 38 ``Ouverture_effective``

* __O__ TxOrigin
* __O__ CheckEffects
* __O__ InlineAssembly
* _`X`_ BlockTimestamp
    - 100%, TIMESTAMP

        - Line 171, 12 ``block.timestamp``

* __O__ LowlevelCalls
* __O__ BlockHash
* __O__ SelfDestruct
