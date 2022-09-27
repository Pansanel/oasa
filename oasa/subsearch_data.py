# Copyright (C) 2003-2008 Beda Kosata <beda@zirael.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>


# automatically generated file - may be overwritten at any time
structures = [
    ('aldehyde', 'carbonyl group', 'HC=O', []),
    ('ketone', 'carbonyl group', 'CC(=O)C', [1, 4]),
    ('carboxylic acid', 'carboxyl group', 'HOC=O', []),
    ('carboxylate anion', 'carboxyl group', '[O-]C=O', []),
    ('ester', 'carboxyl group', 'COC=O', [1]),
    ('anhydride', 'anhydride', 'O=COC=O', []),
    ('acyl chloride', 'acyl chloride', 'O=CCl', []),
    ('acyl flouride', 'acyl flouride', 'O=CF', []),
    ('acyl bromide', 'acyl bromide', 'O=CBr', []),
    ('acyl iodide', 'acyl iodide', 'O=CI', []),
    ('nitrile', 'nitrile', 'C#N', []),
    ('amide', 'amide', 'C(=O)N', []),
    ('alkyl chloride', 'alkyl chloride', 'C-Cl', [1]),
    ('alkyl bromide', 'alkyl bromide', 'C-Br', [1]),
    ('alkyl fluoride', 'alkyl fluoride', 'C-F', [1]),
    ('alkyl iodide', 'alkyl iodide', 'C-I', [1]),
    ('alcohol', 'hydroxy group', 'C-[OH]', [1]),
    ('alcoxide anion', 'alkoxide', 'C-[O-]', [1]),
    ('ether', 'ether', 'C-O-C', [1, 3]),
    ('thiol', 'thiol', 'C-[SH]', [1]),
    ('thiolate anion', 'thiolate', 'C-[S-]', [1]),
    ('thioether', 'thioether', 'C-S-C', [1, 3]),
    ('primary amine', 'amino group', 'C-[NH2]', [1]),
    ('secondary amine', 'amino group', 'C-[NH]-C', [1, 3]),
    ('tertiary amine', 'amino group', 'CN(C)C', [1, 3, 4]),
    ('quarternary ammonium salt', 'amino group', 'C[N+](C)(C)C', [1, 3, 4, 5]),
    ('borane', 'borane', 'C-[BH2]', [1]),
    ('borane', 'borane', 'C-[BH]-C', [1, 3]),
    ('borane', 'borane', 'C-B(C)C', [1, 3, 4]),
    ('nitro compound', 'nitro group', 'C-N(=O)=O', [1]),
    ('sulfonic acid', 'sulfonyl group', 'C-S(=O)(=O)O', [1]),
    ('sulfate anion', 'sulfate', 'C-S(=O)(=O)[O-]', [1]),
]
rings = [
    ('benzene', 'C1=CC=CC=C1', '350796d8048c08e039528ff682c2886fb617caaf'),
    ('pyridine', 'C1=CC=NC=C1', 'cf57c9c221dcef058588e5718cc0f4d6cff5d9cc'),
    ('thiolane', 'C1CCSC1', '17e910702bcda3fb1ee721f24bddd3f04c5ff9b8'),
    ('piperazine', 'C1CNCCN1', '84846557d99c1bc92e8e2f839f438c1124608c0e'),
    ('cyclopropane', 'C1CC1', '0d4d50316ada08de65c5ad9bdbe6b4f69c44344f'),
    ('oxirane', 'C1CO1', '6f929e37b37d323fc6dc236bd574f23014f9cc58'),
    ('1H-pyrrole', 'C1=CNC=C1', '29e0fc670f81762d5654a0293a6699dfaa01b50b'),
    ('oxolane', 'C1CCOC1', '18ee72a2a84912feffeb31dc1405e7d018c95f0e'),
    ('furan', 'C1=COC=C1', '3d7f9eb442fc790ee6dfd16d715041f710a2e90a'),
    ('thiophene', 'C1=CSC=C1', '348f4f456ec4f9ea7c148b9b588bcd58fb4d905c'),
    ('cyclohexane', 'C1CCCCC1', '431733eb3addf4944ce5bedb02524754ea459a70'),
    ('cyclohexene', 'C1CCC=CC1', '0023eb1833d1884c2e8123996cc38b69bae3becc'),
    ('piperidine', 'C1CCNCC1', '8fb354481a85c3017b0ffe644c7cdf0be99aa530'),
    ('morpholine', 'C1COCCN1', '0da779e5e31bfbfb025f6e4c176d3291a3c1d68a'),
    ('azepane', 'C1CCCNCC1', 'ff46e572cbe148da06eb262e89f15b682b2f5227'),
    ('cyclopentene', 'C1CC=CC1', '40517ae1a62ef40c8dbe7546312298dabf35850c'),
    ('oxane', 'C1CCOCC1', '36ad6ab83ec9c6d43251967854bd0dc84325a778'),
    ('aziridine', 'C1CN1', '54f2a460a8357bb5e5ecbc2f2d51dae167a256dc'),
    ('cyclobutane', 'C1CCC1', 'e97ad0643bc6ba7b72d701695d05185a55199291'),
    ('thietane', 'C1CSC1', 'b2d1abc89d0d540ff4dfaf7e35f74f0e65395e36'),
    ('cyclopentane', 'C1CCCC1', '4ca53e63f47ae1c479fedcee520bbecfe7017b82'),
    ('pyridazine', 'C1=CC=NN=C1', '2855bb8bb1cc163a8e4b6add5642c1d9f37073c6'),
    ('pyrimidine', 'C1=CN=CN=C1', '959bceeb09fbb4f48e46f3582d39b6beccdd27fd'),
    ('pyrazine', 'C1=CN=CC=N1', '0a2d9f7e5b882c36eb7d875b01be66ad7fdc98ca'),
    ('cycloheptane', 'C1CCCCCC1', 'c77a5b0844a6a6f884bd0137d9d4ca3f75bc56b5'),
    ('cyclooctane', 'C1CCCCCCC1', '14f4b482684afd368b6fab21d5010fc18e7e36ff'),
    ('cyclodecane', 'C1CCCCCCCCC1', 'f0ac50914527659ad2613cdcd95da846ac328247'),
    ('cyclododecane', 'C1CCCCCCCCCCC1', '51261d03082ed6a57cfbe27c54f87cb01bc0c6a5'),
    ('thiirane', 'C1CS1', '9af082c9d2cd9b93716df861f2ac1ba1a439226d'),
    ('azetidine', 'C1CNC1', 'f7f6de01b36bed0ef503e453965da50ff54eec92'),
    ('oxetane', 'C1COC1', '7a5f0c189b422f154f6dd74cd2ba0338bb327339'),
    ('oxepane', 'C1CCCOCC1', '0385e44b970128e523484e2bbb247337bcf2e12e'),
    ('cycloheptene', 'C1CCC=CCC1', '4e1d399678ea912ed47b635df708b27895850507'),
    ('cyclooctatetraene', 'C1=CC=CC=CC=C1',
     '16731e44f910160a6670509592f883e3ead4e357'),
    ('cyclooctene', 'C1CCCC=CCC1', '99bca2a4525fd8bd4b407bb0b29c5e40c3a93913'),
    ('cyclodecene', 'C1CCCCC=CCCC1', '46797f868adb9aa5b634083701a7230ddff5bd35'),
    ('azocane', 'C1CCCNCCC1', '04a249f214d4d31b9488cf2674682dfdc04e08ef'),
    ('cyclododecene', 'C1CCCCCC=CCCCC1', '99049ae96447c87becf0a83b7291e69bcf3f8505'),
    ('thiane', 'C1CCSCC1', '0fcce6b3d6f5e5d3bbae896d926ff67ebd44c27c'),
    ('azecane', 'C1CCCCNCCCC1', '27a623104ec68af70355c2ce66ac6493b6c2e128'),
    ('pyrrolidine', 'C1CCNC1', '997bd7dc868ea899cb064de29b6f096a459445c0'),
    ('thiomorpholine', 'C1CSCCN1', '68e58d8fd06ba90a84701b7ed187f4a5cc710561'),
    ('thiadiazole', 'C1=CSN=N1', 'b6fbe37f0950f8bd1637330cbcc08d1397071a02'),
    ('cyclotetradecane', 'C1CCCCCCCCCCCCC1',
     '51ee0d72c6e802ea649701ad4641d65ee711ee81'),
    ('cyclopentadecane', 'C1CCCCCCCCCCCCCC1',
     '86f3d9da03d0ddb76560a105c2e943174e1755e8'),
    ('cyclohexadecane', 'C1CCCCCCCCCCCCCCC1',
     'ab6827c71f1e330cb56a6da147d157ea8b5585c8'),
    ('cyclobutene', 'C1CC=C1', '801c06baea3fd40bd10a95845bb9fbec44392883'),
    ('phospholane', 'C1CCPC1', '5d1c6067c37a19a88b7b766e149fec4de7aac54f'),
    ('thiepane', 'C1CCCSCC1', '2fd7591c33b05c6e097e199de637eb17801be2a4'),
    ('pyrazolidine', 'C1CNNC1', '577a673e5d3d568ab3b3379d69c9a7a7da324406'),
    ('dithiolane', 'C1CSSC1', 'ded6dbb77dda101cdbd2e1683b8e70737ca60cc1'),
    ('azonane', 'C1CCCCNCCC1', '451d9f0d0037cc6b4c3b4ad2cd76672b8b139d70'),
    ('hexathiepane', 'C1SSSSSS1', '45f5a5aa67df5e1c370156076681804dc2afb87d'),
    ('azaboretidine', 'B1CCN1', '774654a93af38313389d3c20a5a64a0d67efaaba'),
    ('dioxetane', 'C1COO1', '982ef947b7bc7c43514a14c4172714a8d2bebadf'),
    ('phosphinine', 'C1=CC=PC=C1', '135c35e52dfae56eacbedf706d88fb85c43d23b0'),
    ('triazine', 'C1=CN=NN=C1', 'a1af4d8c97e8b076a7143a73891842a25b94040c'),
    ('cyclopropene', 'C1C=C1', 'd1f3db031419f8c22f6f7c500992f01e722ecb75'),
    ('trithiane', 'C1CSSSC1', '134d7d93d8858632f4014889a086c4d9df504954'),
    ('cyclononane', 'C1CCCCCCCC1', '66e6c25e69eda88d7bd27929b78e10c6e3de3d96'),
    ('cycloundecane', 'C1CCCCCCCCCC1', '2e90d677a596d98387272806222e2a412680e68f'),
    ('cyclotridecane', 'C1CCCCCCCCCCCC1',
     'cd63ad2dcee7fa54c252d36b070a484e0ad6e59e'),
    ('cycloheptadecane', 'C1CCCCCCCCCCCCCCCC1',
     'cf535eecb259e341659e4f4e1cd56b721cc1e193'),
    ('cyclooctadecane', 'C1CCCCCCCCCCCCCCCCC1',
     'c21f462611d018f7c3421ff246e188c7abe68f91'),
    ('diazinane', 'C1CCNNC1', '3a4dafe6d15aeb9ba8d32a0ff7928b333eccdbcb'),
    ('dithiane', 'C1CCSSC1', '87c14e137db7023dffdfc04ababe2350a236a19c'),
    ('dioxepane', 'C1CCOOCC1', 'b8985532e75bdbfeb1f89c38c003151de4cbaa2c'),
    ('cycloundecyne', 'C1CCCCC#CCCCC1', 'f3706b74c5045ef990a2387782bc2b81edc5d8c7'),
    ('cyclobutadiene', 'C1=CC=C1', 'a600e8a75d931a6d7eb2bcd8999c418ab08b346c'),
    ('cyclododecyne', 'C1CCCCCC#CCCCC1', '443f57fe0cb9b6fb1fc1dc95ed9244e5eee344e5'),
    ('cyclooctyne', 'C1CCCC#CCC1', 'bf0ef0e62fe7392f42e36f1e31c8a67e681f0046'),
    ('cyclodecyne', 'C1CCCCC#CCCC1', '650a888751e6b496022ee42405f3297177d0a7d9'),
    ('dioxolane', 'C1COOC1', 'b26104001ab13f31d096ad8dff1c9e665bb07dcc'),
    ('phosphinane', 'C1CCPCC1', '0a8cc7bf4ffe603977712d57bac305cc680b7a4e'),
    ('oxathiolane', 'C1COSC1', '4d20d194fa55b745d4f01401019fffea9a911c63'),
    ('dioxane', 'C1CCOOC1', 'd96577e0fbbd49e3f112bf3be4914ce0ae29ba75'),
    ('dioxocane', 'C1CCCOOCC1', 'cd5cfcfa6681b5bc07a5ddb0ff99269a2e0b43b4'),
    ('cyclononyne', 'C1CCCC#CCCC1', '044a001e9c37cf41ccba1e0a306bf9845219e503'),
    ('dithiete', 'C1=CSS1', '0f93f7d4f0f4229fd95bda655265968dcdb4512e'),
    ('oxazinane', 'C1CCONC1', 'aa65ea759150de6e715fa071f3e1b34e5f50416e'),
    ('oxirene', 'C1=CO1', '2c836bcf1d872fe7a2206089ac63599d755e5b93'),
    ('oxonane', 'C1CCCCOCCC1', 'f90e9088e9da9c3035fd8160a4fb5b80f3394679'),
    ('thiocane', 'C1CCCSCCC1', '3824ce63ab7add7310957fb862efdd1f224cd0ff'),
    ('imidazolidine', 'C1CNCN1', '6b8b5e6ba3ef5ec0b47769c32cf6c71fa8a17997'),
    ('dioxirane', 'C1OO1', '14d8dc16520e67e60161e5980bd7b66182fe382e'),
    ('cycloicosane', 'C1CCCCCCCCCCCCCCCCCCC1',
     'f83f352fb286c8f8196441716e464732fae15baf'),
    ('cyclotetracosane', 'C1CCCCCCCCCCCCCCCCCCCCCCC1',
     '813de51ca763c71756ebefaafa049883b8e846e3'),
    ('dithiepane', 'C1CCSSCC1', '2860adab37f68c6ac4d76fb3700580e8f14b543d'),
    ('oxadithiole', 'C1=CSSO1', 'b55537faa488df8529f2a4ded6c560c410968ab7'),
    ('tetrathiepane', 'C1CSSSSC1', 'be64ca38faea662875fd211a4312c2dbb3a327a6'),
    ('dithiocane', 'C1CCCSSCC1', '8e9ad5c8fe1b3e5845857f49f3277b89ce2e0461'),
    ('trithiolane', 'C1CSSS1', '8d153a99f1e39e4b2f084d19e00f2d26b78e1f80'),
    ('tetrathiine', 'C1=CSSSS1', 'd4791f2954ab58a34b49450147067cc73885aa1b'),
    ('tetrathiane', 'C1CSSSS1', '385385a3f4441c84f1d1997abdd315c84402fbd5'),
    ('oxathietane', 'C1CSO1', 'b2fe37b651ac8133b4c6d6725355e0b430f450cf'),
    ('diaziridine', 'C1NN1', '4f538486d12df7d88605346dcc5ec5c19bcfa186'),
    ('tetrazolidine', 'C1NNNN1', '9f78cf3fbb3524148a620de2233f497e6829c426'),
    ('oxazirene', 'C1=NO1', '8cf80d062b1b24c165c8dab8f8db344390d407f1'),
    ('thiirene', 'C1=CS1', '6c69bc937c11775b5e14dadf47ae2d9357f67d71'),
    ('cyclobutatetraene', 'C=1=C=C=C1', '961cd73ed9bb150af834c1f0f53778352af9842e'),
    ('pentazine', 'C1=NN=NN=N1', '355086e0fe424b0ee6e6e1f7b58cbd579b3517e5'),
    ('oxepine', 'C1=CC=COC=C1', 'cdcf5031b069c89472ea145e4d4dc190f8e17c1b'),
    ('oxadiazole', 'C1=CON=N1', '5aae07d09ecdc69362b3d1050127bac612c72e3c'),
    ('cycloheptyne', 'C1CCC#CCC1', '2827288cd65a0e1ba0aad43d0d7bfa65c9c8c84a'),
    ('borinine', 'B1=CC=CC=C1', 'e1e1b60e3d204e73088193fa93553910130206a4'),
    ('cyclohexyne', 'C1CCC#CC1', 'dcb5ebafcb32befb46b2aba7393871813b6658fd'),
    ('cyclotridecyne', 'C1CCCCCC#CCCCCC1',
     '1f737da455b3305283e49d1eca61320eabf7fecf'),
    ('thionane', 'C1CCCCSCCC1', '297a2a259a078df7e5111712d81b8d8ad698aac2'),
    ('dioxazine', 'C1=COON=C1', '91dc380b4410faa1174dac90b2cde032889ef1a5'),
    ('dithiine', 'C1=CSSC=C1', 'dcec36bd6e9dcdb8066d7616038860cd7d0cb5eb'),
    ('cyclohexacosane', 'C1CCCCCCCCCCCCCCCCCCCCCCCCC1',
     'cd8fc040b9b526588dd9f0920b0822d8c3c9871a'),
    ('dithietane', 'C1CSS1', '7eeca53bbdd3bfddbedabbb8faf8a2ec0b328348'),
    ('tetrazine', 'C1=CN=NN=N1', '7cf758d32dd71d641703429489ee22e64fbeea13'),
    ('thiazepine', 'C1=CC=NSC=C1', '16fed730a19c040eda525e52b0002964cf558698'),
    ('thiepine', 'C1=CC=CSC=C1', '4019c280163f87d00cbed500f891fed25bd203a5'),
    ('oxathiane', 'C1CCSOC1', '9a9c05cbc93c34a351b8a9bb1b7b5b1fc6914f91'),
    ('diazocane', 'C1CCCNNCC1', '1f71308fa16c925352a8321c12c6005d8dfaa34f'),
    ('trithiepane', 'C1CCSSSC1', '3a0550857269121171d4cfa02b4a60e391008f8e'),
    ('oxocane', 'C1CCCOCCC1', 'f810d3c6d7033ca9d544f22caacc458ec3586d13'),
    ('trithionane', 'C1CCCSSSCC1', '343040278bd1da3b558df9dc94d865b0cace1984'),
    ('diazepane', 'C1CCNNCC1', '2df73e7034e5449cc5ef63b21d5d8d5ca7999d84'),
    ('dithionane', 'C1CCCSSCCC1', '3a1ec9f7282eab0b935d2af57fdd3ffe032f0e3f'),
    ('oxonine', 'C1=CC=COC=CC=C1', 'f49d94491c44b840dd0df00e5b836f328d0e1b3e'),
    ('thionine', 'C1=CC=CSC=CC=C1', '9ec69f6b3dc4a2a093b3a21653b49ab3a3770cf4'),
    ('cyclohenicosane', 'C1CCCCCCCCCCCCCCCCCCCC1',
     '2973544d8f8196cd188373364a3d814edb9a90cc'),
    ('cyclodocosane', 'C1CCCCCCCCCCCCCCCCCCCCC1',
     'fe1ead29e43ffcbf2cd523de0d225416a250b9f8'),
    ('cyclotricosane', 'C1CCCCCCCCCCCCCCCCCCCCCC1',
     '119b5f17605d30602e61fbb19b4af2839ec60e2b'),
    ('oxazepine', 'C1=CC=NOC=C1', '57ab48a5b9e6cd15eb2a3de800aa1c45653b6d65'),
    ('thiatriazole', 'C1=NN=NS1', '4a4eefec8072df698e17aef07683b17a4828d96f'),
    ('oxecane', 'C1CCCCOCCCC1', 'd89283583bb20cc014e25f6065442ace7ffa0ecf'),
    ('phosphepane', 'C1CCCPCC1', 'fa0dc617ad23b30170f59c85952ac45f3fd280de'),
    ('cyclodecapentaene', 'C1=CC=CC=CC=CC=C1',
     '4169cf9eb9e401cf5213a2a36cd57f631843c4d0'),
    ('dioxine', 'C1=COOC=C1', '635f53e36526a0a7739cf658748b3fd56e952df4'),
    ('phosphirane', 'C1CP1', '3a448f3692483c4d9848411779fef0d322370934'),
    ('oxaziridine', 'C1NO1', '715029842446df199ac78a81d16f32f15fd21280'),
    ('triazinane', 'C1CNNNC1', 'dfde7e3d21db5538b768592e02676187e0c4167d'),
    ('pentathiepane', 'C1CSSSSS1', '3e8584bb02f40e13387ce008f53b5f56d30aae1a'),
    ('diphospholane', 'C1CPPC1', '9e874a73f57247f11967f34318c7810b45ea3f43'),
    ('azaphosphiridine', 'C1NP1', '66044516871e9ad5e1fc38eaf61e32c8fade3334'),
    ('oxadiazepane', 'C1CCONNC1', '5e5cff7ebf29b7bde84fb602aa36579ef954f2db'),
    ('dioxaphospholane', 'C1CPOO1', 'f5b4ba19aeac0177345200a384322895597c397d'),
    ('tetrathiolane', 'C1SSSS1', '636168f3883d7dcd603ca1841d58347ed904212c'),
    ('dioxathiolane', 'C1CSOO1', 'db310b8d6a4f2f5de3dd8da794c56e9f1f285226'),
    ('dithiazolidine', 'C1CSSN1', 'c9d59e75872fa09d054d580415da90907fd95e99'),
    ('dithiazinane', 'C1CNSSC1', 'f12a1fbaf7c6af33b2c10f79827eec2b7515dd56'),
    ('thiazetidine', 'C1CSN1', '1d5158a5e94d7120b6aa6a9971b75ea478ded917'),
    ('diazaborinine', 'B1=CC=CN=N1', 'f1eeb5081c91763ab861b6f91174e0fea245eca3'),
    ('cyclopropyne', 'C1C#C1', '5cdc00b7c84f012faf32667fb41a666131f0d380'),
    ('oxazetidine', 'C1CON1', '9e92f5f2c1a5ddeba2e6942b39185bb55aea2f3b'),
    ('hexaoxecane', 'C1CCOOOOOOC1', 'aa985362e8f0251701aca17edd11c156b4407424'),
    ('triazete', 'C1=NN=N1', 'edf50618d184779e0b0f0fb577b23fcceb412242'),
    ('oxadiazolidine', 'C1CONN1', '3a61a99d3ef0e01e4d1178ca9165fa748891ec43'),
    ('azaphospholidine', 'C1CNPC1', 'bbbb2d6d166f64f4c1abf0f43809a928ed1d92b8'),
    ('diazetidine', 'C1CNN1', '53c8dbfcf7c0e4f7d11cc353098fde0696261ddf'),
    ('hexathiocane', 'C1CSSSSSS1', '2d1ca01e0f1d74c57956eb330de3136502c0b47e'),
    ('oxathiirane', 'C1OS1', '110bb8900719882698322a2a482b58884b697115'),
    ('oxazonane', 'C1CCCNOCCC1', '2fa4399ae035509c892450109ac9319afee7f6dc'),
    ('oxathiazinane', 'C1CNSOC1', '587722dfa53b283dd48f72237ab5eaa14955aca0'),
    ('oxadiazinane', 'C1CNNOC1', '6c5353238ffe463bc0f68df6db49cfba1d3d7779'),
    ('oxaphosphepine', 'C1=CC=POC=C1', '4990add5c563d2732e7ef9c0a9737b75c9bcb833'),
    ('azaborinine', 'B1=NC=CC=C1', 'c5608dd6c838e533b27fe79ce67897e54e69aaa9'),
    ('trioxetane', 'C1OOO1', '8b53555333fff059db3977adc7246d50f0accf40'),
    ('oxathiine', 'C1=COSC=C1', '57ef13e1e7ff73b7ab75da35ab1e45fd143bc937'),
    ('diphosphetane', 'C1CPP1', '8458108160ffdba74fcade3b55fa08d4621daf8b'),
    ('dithiadiazine', 'C1=CSSN=N1', '0cdeb2316f6f9770157ee8dc485362ce2fe49fc2'),
    ('triazaborinine', 'B1=CC=NN=N1', 'b094bce4fdc27e8ec136eadb3342ecf6439215d6'),
    ('dioxatriazine', 'C1=NN=NOO1', '21f6196c1610891139b3274ef0d7514dac6f06d0'),
    ('trioxane', 'C1COOOC1', '522e8a3d04d891ed21d440c5db0de92f41c99bf9'),
    ('dioxaphosphinine', 'C1=COOP=C1', 'ed4b8ddb7b836bfea5c0869db6f19e31a17ec7fc'),
    ('dioxazolidine', 'C1COON1', '6cea07386b7ed0462fb3d967eb6475f58606a83c'),
    ('dioxaphosphinane', 'C1COOPC1', 'e48686307c03dc4e2beba3e7f5baf7cb276c215f'),
    ('oxazaphosphinane', 'C1CONPC1', 'b633f8c5a3532d0b14d4901572fddc2d992792f6'),
    ('tetraoxecane', 'C1CCCOOOOCC1', '303d769622ea32fd9942a59c69652e2c1b1ffb2b'),
    ('thiazepane', 'C1CCNSCC1', '5427cfdb1f1a1259f2d97e86142255fbeb16032d'),
    ('oxazepane', 'C1CCNOCC1', 'e9de69f1bb6d04af47123bb26ba59033fc12fb59'),
    ('trithiazole', 'C1=NSSS1', 'b51693d0b45cf5143b8d93c9992dfd8daeb9503a'),
    ('oxazaphospholidine', 'C1CPNO1', '7b304fa46adf627e4319a7cbf81c1ab14fb34550'),
    ('dithiaphosphetane', 'C1PSS1', 'd9d0754bf2ed9862525c361a75d189ae40a9dc51'),
    ('cyclobutyne', 'C1CC#C1', '22eafeec6ab23da517a42a852b69ce8e2f72c781'),
    ('cyclooctadecyne', 'C1CCCCCCCCC#CCCCCCCC1',
     '0091a553fe3cddb3ada8a474b47addd0e3b61d86'),
    ('thiazocane', 'C1CCCSNCC1', '5d16343e31e84d28dd164faa25b0366d0709dd51'),
    ('oxazocane', 'C1CCCONCC1', 'badc1ba6a20263389ff0e39cf40e17e023a004b8'),
    ('azete', 'C1=CN=C1', '71c5464586b37647a6bfbb6129eab332827c9da9'),
    ('thiadiphosphinane', 'C1CPPSC1', '391b958ce0fd68dad4e158a2442c26754025c8f5'),
    ('hexaoxocane', 'C1COOOOOO1', '23584e4502e4d0ef5f081c22ed79f1fba458d854'),
    ('oxathiadiazine', 'C1=COSN=N1', 'c43f8bd421c1e398ea7bc273be15f75adbe772e6'),
    ('oxadithiane', 'C1COSSC1', '193bb93ecb815d6d74c9e98734ea41d465bfeca2'),
    ('dioxazepane', 'C1CCOONC1', '1c88f4337a309538eff2bdd2aaaa236336f56861'),
    ('diazaphosphinane', 'C1CNNPC1', '66f183b133681b1afdf4bdaea70e0c1a651652a2'),
    ('dioxadiazecane', 'C1CCCOONNCC1', '1c8f5eab329af07b4570b5f4c7c2ae6db2d46a0f'),
    ('dioxadiazonane', 'C1CCNNOOCC1', '5c9daa9121f71cb15ee1b031f21e5848af2df8bf'),
    ('dioxadiazocane', 'C1CCOONNC1', 'efc1a204dc7c21702f187dc156588fec6f43e667'),
    ('oxadiazecane', 'C1CCCNNOCCC1', '585510072c8e0c9cfac51db25c622bb2be9fc0c2'),
    ('oxadiazonane', 'C1CCCONNCC1', '221b6da6d3a3aada0f12a90d965c28e6288b7dce'),
    ('oxadiazocane', 'C1CCNNOCC1', 'acead1b345487fdae399ff97045ee91366298a6c'),
    ('dioxazaborinine', 'B1=NOOC=C1', '030f0983333da5470200390f87ca76b65ca08c81'),
    ('dioxecane', 'C1CCCCOOCCC1', 'e0294012a81603b0a77e0d88847dc9e960621f97'),
    ('dioxazinane', 'C1CNOOC1', '5a6cc06023c137f0f7b9b3c11cece0bd603d26aa'),
    ('oxathiepane', 'C1CCOSCC1', '371c969316608f47f1c7090fda71284feb669dc8'),
    ('thiaziridine', 'C1NS1', 'c0b88d6ebc38b3aeb8bfbe301b09279c0443144e'),
    ('trioxazolidine', 'C1NOOO1', '5f3c6fe44e62fccce5aa856416018173300b2b0a'),
    ('tetrazocane', 'C1CCNNNNC1', '63388a7ab542aa8d42cbb7b1c22bcaa233bdb261'),
    ('tetraoxane', 'C1COOOO1', '544c64fcb3dd03c3aad864dacc127f3b65c7b90c'),
    ('triazecane', 'C1CCCNNNCCC1', '9490e0ed8f1791e391e26bb8b89a56911a6eddf2'),
    ('dioxocine', 'C1=CC=COOC=C1', 'b8d2746ba5fe8d040e2248651300978514edc529'),
    ('cyclononadecane', 'C1CCCCCCCCCCCCCCCCCC1',
     '7f937f8028b7096bed706dd6dce7c6b207c67d3e'),
    ('thiazinane', 'C1CCSNC1', '8fb6179aedb4d70bd9bba28559bbe6f1a484e971'),
    ('azadiborinine', 'B1=CC=CN=B1', '680fd74b389ce272569cd58931c0f820af9693d9'),
    ('oxatetrathiane', 'C1OSSSS1', 'c7d26e4cac672ce8249511ca244de80d7b6bc509'),
    ('oxatriazole', 'C1=NN=NO1', 'a08ba137c2fa6059a440a892db8b73eeb19bf655'),
    ('dithiirane', 'C1SS1', 'f90fe2671584c5761388a026856ae140e21e18c7'),
    ('oxathiazine', 'C1=COSN=C1', 'ecf57d3aef19b75cc4b9a1d227f3dc62cf76ff44'),
    ('dithiazine', 'C1=CSSN=C1', 'e2ec6255ce4f957b7a0687d6a687128cb14c16f4'),
    ('thiadiazepine', 'C1=CN=NSC=C1', '37d8ab83307a220c52cdf655793500b274b0d2ac'),
    ('triazolidine', 'C1CNNN1', '83374cb6d6936e5e0e0f1db02ee350888c4de666'),
    ('oxadiazepine', 'C1=CN=NOC=C1', 'f6c4a58a86462ee7f874ba61ce7e958b473edef6'),
    ('tetrazonane', 'C1CCNNNNCC1', 'a87bd0bf3616220e955efcbffec5f01e44e37716'),
    ('thiadiazolidine', 'C1CSNN1', '6854276625fc20d6ede0a7a3afbc0f402b209c9c'),
    ('thiadiazepane', 'C1CCSNNC1', '5d18321fd58647b0f043c6a3abddf8481e1f6850'),
    ('thiadiazinane', 'C1CNNSC1', '0d82137ec152069685ff0438d13efc543c37d31c'),
    ('triazonane', 'C1CCCNNNCC1', '97d5d32aa687f65cbe69f89c8f3492ccde5f7f65'),
    ('oxathiazolidine', 'C1COSN1', '0f7b095cb0cba97bee79ff3fa6c1c2570a7ade48'),
    ('dioxazocine', 'C1=CC=NOOC=C1', '16a01f0ed74d90b104ab32afaf0ae9309fc6141a'),
    ('trioxolane', 'C1COOO1', '485f6481058ecc384ea4d59ecce5613ff0e30fac'),
    ('dithiadiphosphinane', 'C1CSSPP1', '3cc665eed72417b07b5133c51941d19d304b8dfa'),
    ('diphosphinane', 'C1CCPPC1', '7ef5852616d3c724a0b35cb9764bb8f358ae072b'),
    ('diphosphepane', 'C1CCPPCC1', '20c0aa7d09532a45f1342080398a5f0e5d4cffe6'),
    ('thiazonane', 'C1CCCNSCCC1', '3a27b0523db52326917da97a1d15ec0e5c1d1e13'),
    ('tetrazinane', 'C1CNNNN1', '81abe199380d51d88414b1385f6f51b49549a167'),
    ('trithiole', 'C1=CSSS1', '9204e479bd47a1e7a44ce8a2d8930fba40805b46'),
    ('trioxole', 'C1=COOO1', '6ff1f27d2eee426adcbbe81a47ce81ec44aa9c3b'),
    ('oxadithiolane', 'C1CSSO1', '112aa6a6bb089c6cb62a53057dca158a1e70d16f'),
    ('trioxepane', 'C1CCOOOC1', 'cf3b4298b5554a1fa231cc78e2dba6ccd6436f41'),
    ('diazaphospholidine', 'C1CPNN1', '2e74649eb87672d23f242f9b4f12a007c050afdd'),
    ('dioxaborinine', 'B1=CC=COO1', 'bef359904126ce3f4699930a5b9d41671fe3827e'),
    ('tetrazecane', 'C1CCCNNNNCC1', 'ed1abc4c9823a8786d4ebb9f0a74e395fc1e8955'),
    ('dioxathiane', 'C1COOSC1', '50154b3a766e04da5debb23f23b703cfbe018732'),
    ('oxadithiazole', 'C1=NSSO1', '8dbb4edb6cee44dae6c526580e9e360fb6e91742'),
    ('oxathiaphospholane', 'C1CPSO1', '0827fbd02a7b4345198259617cb34af0357469c2'),
    ('dioxaphosphocine', 'C1=CC=POOC=C1',
     '581ffacbef62f591556f7b9eb1dd0b88fcac2791'),
    ('thiatriazolidine', 'C1NNNS1', 'b154a07a59dbef28df1057d845fe310983768f44'),
    ('oxatriazolidine', 'C1NNNO1', 'e354367317f6027f75a541516f543190c6c85dd3'),
    ('diazonane', 'C1CCCNNCCC1', 'ff04eed2d94092952561106545e4a3cb8e913466'),
    ('triazepane', 'C1CCNNNC1', '439f8f0f9b04a588292680344a5e96b06a3b9dd3'),
    ('triphosphinane', 'C1CPPPC1', '907e429ec178db85e99a661df31a1a6a4005b5db'),
    ('dioxete', 'C1=COO1', 'bc12a49992d17807de6798dc7fd11a67ab09762f'),
    ('oxaphospholane', 'C1COPC1', 'a6cca1c3f2929b11e3dcdeb1ca4cc5e0a6fbd185'),
    ('trioxazole', 'C1=NOOO1', 'ea253efca5d4bf9987ee0d41d6109c298a74eb23'),
    ('triphosphinine', 'C1=CP=PP=C1', 'cdfe8af6dfd6d4dc25c450607867e48b354a6801'),
    ('oxathiocine', 'C1=CC=CSOC=C1', 'fb49d5ea2b73dfa0a9c94ac2b207757509c838cd'),
    ('azaphosphepane', 'C1CCNPCC1', 'eb74fd435a478a70fd2a9a195b94665345a88120'),
    ('dioxaphosphepane', 'C1CCPOOC1', '06397f029c0cb79f4d68500b0d1dfd9a7d67a4b8'),
    ('azaphosphinane', 'C1CCPNC1', '70e3ef4924d0055a402f57065dc552bcbf90f9ee'),
    ('triazetidine', 'C1NNN1', 'da5ec424bba6b7ab69ea4fa992125eae8b248209'),
    ('dioxaphosphonane', 'C1CCCPOOCC1', 'd30ec082388e5d8e20aa0cc5abb16397f2217571'),
    ('pentazecane', 'C1CCNNNNNCC1', 'ff09f109b2265802230ed82dbc49aab2293b6df1'),
    ('thiadiazonane', 'C1CCCSNNCC1', '27e002205d75e109bf5dd0987c623ed5e9cdd82e'),
    ('thiadiazocane', 'C1CCNNSCC1', '546170f8c647cf582b53ed3a73db17d55d6353e1'),
    ('tetrathiecane', 'C1CCCSSSSCC1', '92f2b03540740806b778e2afab19af56cd3f04cf'),
    ('oxazecane', 'C1CCCCONCCC1', 'f81e12755c6bb4dfb881e58209a7d6469f4eaf3a'),
    ('oxathiazocane', 'C1CCNSOCC1', '0f815be8e796692e2519651332d03578f33bfec3'),
    ('diazecane', 'C1CCCCNNCCC1', '97c7d7f99033994f0723b113a8531735fe65e493'),
    ('phosphetane', 'C1CPC1', '00194707c5ebc3653d7497d107811b312b9abf8a'),
    ('trioxocane', 'C1CCOOOCC1', '34c09eb9a24bf8e280495ff3594bb5c155fdfc19'),
    ('oxaphosphetane', 'C1CPO1', '95f6e955f3967cdca678530d1f49ddba069951a8'),
    ('phosphecane', 'C1CCCCPCCCC1', 'f6ec97611287768b60598d87275c708147b1894a'),
    ('phosphocane', 'C1CCCPCCC1', 'f5ed7c2040ea55bff0cdf27ce2d3816d024e306d'),
    ('phosphonane', 'C1CCCCPCCC1', '2c608a8f710660ae48421f0e68b780274738c645'),
    ('tetrazocine', 'C1=CN=NN=NC=C1', '2c5b47cd32e43d55b00dbdbf99077d8392f3579a'),
]
