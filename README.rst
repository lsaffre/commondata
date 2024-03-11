==========================
The ``commondata`` package
==========================

Share structured common data in a pythonic way

The library just provides pure data, it does *not* feature any querying or
rendering functionality.  This is a design choice. This data is meant to be
imported into existing systems that use their own preferences for rendering and
querying data.

Online version of this document on https://github.com/lsaffre/commondata


Countries of the world
======================

>>> from commondata.countries import COUNTRIES, FIELDS
>>> FIELDS
('entity', 'name', 'isoCode2', 'isoCode3', 'zipCode', 'population')
>>> COUNTRIES[0]
Country(entity='Q228', name={'en': 'Andorra', 'de': 'Andorra', 'fr': 'Andorre', 'nl': 'Andorra', 'et': 'Andorra', 'bn': 'অ্যান্ডোরা', 'es': 'Andorra'}, isoCode2='AD', isoCode3='AND', zipCode=None, population='85101')

>>> len(COUNTRIES)
195

These are the countries of the world:

>>> lst = ["{} ({})".format(c.name['en'], c.isoCode2) for c in COUNTRIES]
>>> print(", ".join(lst))  #doctest: +REPORT_UDIFF +NORMALIZE_WHITESPACE
Andorra (AD), United Arab Emirates (AE), Afghanistan (AF), Antigua and Barbuda
(AG), Albania (AL), Armenia (AM), Angola (AO), Argentina (AR), Austria (AT),
Australia (AU), Azerbaijan (AZ), Bosnia and Herzegovina (BA), Barbados (BB),
Bangladesh (BD), Belgium (BE), Burkina Faso (BF), Bulgaria (BG), Bahrain (BH),
Burundi (BI), Benin (BJ), Brunei (BN), Bolivia (BO), Brazil (BR), The Bahamas
(BS), Bhutan (BT), Botswana (BW), Belarus (BY), Belize (BZ), Canada (CA),
Democratic Republic of the Congo (CD), Central African Republic (CF), Republic
of the Congo (CG), Switzerland (CH), Ivory Coast (CI), Chile (CL), Cameroon
(CM), People's Republic of China (CN), Colombia (CO), Costa Rica (CR), Cuba
(CU), Cape Verde (CV), Cyprus (CY), Czech Republic (CZ), Germany (DE), Djibouti
(DJ), Dominica (DM), Dominican Republic (DO), Algeria (DZ), Ecuador (EC),
Estonia (EE), Egypt (EG), Eritrea (ER), Spain (ES), Ethiopia (ET), Finland (FI),
Fiji (FJ), Federated States of Micronesia (FM), France (FR), Gabon (GA), United
Kingdom (GB), Grenada (GD), Georgia (GE), Ghana (GH), the Gambia (GM), Guinea
(GN), Equatorial Guinea (GQ), Greece (GR), Guatemala (GT), Guinea-Bissau (GW),
Guyana (GY), Honduras (HN), Croatia (HR), Haiti (HT), Hungary (HU), Indonesia
(ID), Republic of Ireland (IE), Israel (IL), India (IN), Iraq (IQ), Iran (IR),
Iceland (IS), Italy (IT), Jamaica (JM), Jordan (JO), Japan (JP), Kenya (KE),
Kyrgyzstan (KG), Cambodia (KH), Kiribati (KI), Comoros (KM), Saint Kitts and
Nevis (KN), North Korea (KP), South Korea (KR), Kuwait (KW), Kazakhstan (KZ),
Laos (LA), Lebanon (LB), Saint Lucia (LC), Liechtenstein (LI), Sri Lanka (LK),
Liberia (LR), Lesotho (LS), Lithuania (LT), Luxembourg (LU), Latvia (LV), Libya
(LY), Morocco (MA), Monaco (MC), Moldova (MD), Montenegro (ME), Madagascar (MG),
Marshall Islands (MH), North Macedonia (MK), Mali (ML), Myanmar (MM), Mongolia
(MN), Mauritania (MR), Malta (MT), Mauritius (MU), Maldives (MV), Malawi (MW),
Mexico (MX), Malaysia (MY), Mozambique (MZ), Namibia (NA), Niger (NE), Nigeria
(NG), Nicaragua (NI), Kingdom of the Netherlands (NL), Norway (NO), Nepal (NP),
Nauru (NR), New Zealand (NZ), Oman (OM), Panama (PA), Peru (PE), Papua New
Guinea (PG), Philippines (PH), Pakistan (PK), Poland (PL), State of Palestine
(PS), Portugal (PT), Palau (PW), Paraguay (PY), Qatar (QA), Romania (RO), Serbia
(RS), Russia (RU), Rwanda (RW), Saudi Arabia (SA), Solomon Islands (SB),
Seychelles (SC), Sudan (SD), Sweden (SE), Singapore (SG), Slovenia (SI),
Slovakia (SK), Sierra Leone (SL), San Marino (SM), Senegal (SN), Somalia (SO),
Suriname (SR), South Sudan (SS), São Tomé and Príncipe (ST), El Salvador (SV),
Syria (SY), Eswatini (SZ), Chad (TD), Togo (TG), Thailand (TH), Tajikistan (TJ),
East Timor (TL), Turkmenistan (TM), Tunisia (TN), Tonga (TO), Turkey (TR),
Trinidad and Tobago (TT), Tuvalu (TV), Taiwan (TW), Tanzania (TZ), Ukraine (UA),
Uganda (UG), United States of America (US), Uruguay (UY), Uzbekistan (UZ),
Vatican City (VA), Saint Vincent and the Grenadines (VC), Venezuela (VE),
Vietnam (VN), Vanuatu (VU), Samoa (WS), Yemen (YE), South Africa (ZA), Zambia
(ZM), Zimbabwe (ZW)

Place names in Estonia
======================

>>> from commondata.places.estonia import PLACES, COUNTIES
>>> len(PLACES)
4564
>>> len(COUNTIES)
15

>>> for county in COUNTIES:
...    print(county.name, ":", ", ".join([p.name for p in county.children]))
Harju : Tallinn, Ääsmäe, Loksa, Vasalemma, Nissi, Saku, Saue, Viimsi, Raasiku, Jõelähtme, Maardu, Rae, Harku, Keila, Anija, Kehra, Kiili, Paldiski, Kose, Padise, Kõue, Kuusalu, Kernu, Aegviidu, Kaasiku, Kibuna, Vahastu, Vansi, Vikipalu, Jägala-Joa, Kersalu, Haapse, Jõesuu, Pohla, Andineeme
Pärnu : Pärnu, Halinga, Tootsi, Vändra, Tori, Tõstamaa, Tahkuranna, Sauga, Paikuse, Sindi, Audru, Häädemeeste, Kilingi-Nõmme, Are, Lavassaare, Varbla, Saarde, Surju, Kihnu, Koonga, Metsaääre, Aruvälja
Rapla : Vigala, Rapla, Kehtna, Märjamaa, Järvakandi, Juuru, Kaiu, Käru, Kohila, Raikküla
Hiiu : Kärdla, Käina, Kõrgessaare, Pühalepa, Emmaste
Ida-Viru : Lohusuu, Sonda, Toila, Tudulinna, Sillamäe, Püssi, Lüganuse, Vaivara, Narva, Avinurme, Narva-Jõesuu, Kohtla-Järve, Aseri, Jõhvi, Iisaku, Kiviõli, Alajõe, Kohtla-Nõmme, Maidla, Mäetaguse, Kohtla, Illuka
Jõgeva : Torma, Põltsamaa, Tabivere, Mustvee, Jõgeva, Palamuse, Puurmani, Saare, Kasepää, Pajusi, Pala, Vägeva
Järva : Türi, Roosna-Alliku, Paide, Väätsa, Ambla, Järva-Jaani, Koeru, Kareda, Albu, Imavere, Koigi, Kolu
Lääne : Lihula, Risti, Ridala, Haapsalu, Hanila, Taebla, Oru, Vormsi, Martna, Noarootsi, Nõva, Kullamaa
Lääne-Viru : Tapa, Rakvere, Vinni, Tamsalu, Rakke, Väike-Maarja, Sõmeru, Vihula, Haljala, Kunda, Kadrina, Laekvere, Viru-Nigula, Eisma
Põlva : Räpina, Põlva, Veriora, Kanepi, Ahja, Kõlleste, Vastse-Kuuste, Värska, Mikitamäe, Mooste, Orava, Valgjärve, Laheda
Saare : Leisi, Salme, Kaarma, Orissaare, Kärla, Kihelkonna, Kuressaare, Valjala, Lümanda, Pöide, Pihtla, Torgu, Mustjala, Laimjala, Muhu, Ruhnu
Tartu : Tartu, Luunja, Ülenurme, Haaslava, Rõngu, Kambja, Elva, Nõo, Kallaste, Puhja, Alatskivi, Mäksa, Tähtvere, Konguta, Rannu, Laeva, Võnnu, Peipsiääre, Meeksi, Vara, Piirissaare, Vehendi, Kriimani, Illi, Neemisküla
Valga : Valga, Tõrva, Otepää, Puka, Õru, Tõlliste, Sangaste, Karula, Helme, Taheva, Põdrala, Palupera, Hummuli
Viljandi : Suure-Jaani, Abja, Abja-Paluoja, Viljandi, Võhma, Mõisaküla, Viiratsi, Halliste, Karksi, Karksi-Nuia, Kolga-Jaani, Pärsti, Tarvastu, Saarepeedi, Paistu, Kõpu, Kõo, Soe
Võru : Vastseliina, Võru, Antsla, Varstu, Sõmerpalu, Rõuge, Mõniste, Haanja, Urvaste, Lasva, Misso, Meremäe, Kirumpää, Navi, Meegomäe

Note: The data about Estonian places is currently obsolete by several years. We
plan to maintain it in collaboration with
https://maaamet.ee/ruumiandmed-ja-kaardid/aadressid-ja-kohanimed/kohanimeregister


Historic note
=============

Until March 2024 this was a namespace package and country-specific data was
contained in individual subpackages. The following packages are now obsolete

- `commondata.be <https://github.com/lsaffre/commondata-be>`_ :
  Common data about Belgium
- `commondata.ee <https://github.com/lsaffre/commondata-ee>`_:
  Common data about Estonia
- `commondata.eg <https://github.com/ExcellentServ/commondata-eg>`_:
  Common data about Egypt

How to uninstall the old commondata packages: find your `site-packages`
directory (e.g. `~/env/lib/python3.10/site-packages`) and manually remove
all files `commondata*-nspkg.pth`

Don't read on
=============

The remaining part of this document is obsolete but still valid.

How to use the Place and PlaceGenerator classes.

You define a subclass of Place for each "type" of place:

>>> from commondata.utils import Place, PlaceGenerator
>>> class PlaceInFoo(Place):
...     def __str__(self):
...        return self.name
>>> class Kingdom(PlaceInFoo):
...     value = 1
>>> class County(PlaceInFoo):
...     value = 2
>>> class Borough(PlaceInFoo):
...     value = 3
>>> class Village(PlaceInFoo):
...     value = 3

The PlaceGenerator is used to instantiate to populate

Part 1 : configuration:

>>> pg = PlaceGenerator()
>>> pg.install(Kingdom, County, Borough, Village)
>>> pg.set_args('name')

Part 2 : filling data

>>> root = pg.kingdom("Kwargia")
>>> def fill(pg):
...    pg.county("Kwargia")
...    pg.borough("Kwargia")
...    pg.village("Virts")
...    pg.village("Vinks")
...    pg.county("Gorgia")
...    pg.village("Girts")
...    pg.village("Ginks")

>>> fill(pg)

Part 3 : using the data

>>> [str(x) for x in root.children]
['Kwargia', 'Gorgia']
>>> kwargia = root.children[0]
>>> [str(x) for x in kwargia.children]
['Kwargia', 'Virts', 'Vinks']


Multilingual place names
-------------------------

You use the `commondata.utils.PlaceGenerator.set_args()` method to
specify the names of the fields of subsequent places.

>>> pg = PlaceGenerator()
>>> pg.install(Kingdom, County, Borough, Village)
>>> pg.set_args('name name_ar')
>>> root = pg.kingdom("Egypt", u'مصر')
>>> print(root.name_ar)
مصر
