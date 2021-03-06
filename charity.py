from random import choice


class Charity:
    FIVE_DOLLAR_CHARITIES = [
    {'to_number': '20222', 'code': 'FIGHTHIV',
       'name': 'AIDS Athens'},
    {'to_number': '20222', 'code': 'FLOWER',
       'name': 'AIDS Healthcare Foundation'},
    {'to_number': '20222', 'code': 'YFALS',
       'name': 'ALS Therapy Development Institute'},
    {'to_number': '20222', 'code': 'AARDA',
       'name': 'American Autoimmune Related Diseases'},
    {'to_number': '20222', 'code': 'CHOOSEYOU',
       'name': 'American Cancer Society, Inc.'},
    {'to_number': '20222', 'code': 'CURE',
       'name': 'American Cancer Society, Inc.'},
    {'to_number': '20222', 'code': 'HOPE',
       'name': 'American Cancer Society, Inc.'},
    {'to_number': '20222', 'code': 'LIFE',
       'name': 'American Cancer Society, Inc.'},
    {'to_number': '41518', 'code': 'RELAY',
       'name': 'American Cancer Society, Inc.'},
    {'to_number': '20222', 'code': 'VICTORY',
       'name': 'American Cancer Society, Inc.'},
    {'to_number': '25383', 'code': 'ADA',
       'name': 'American Diabetes Association'},
    {'to_number': '20222', 'code': 'FIGHT',
        'name': 'American Kidney Fund, Inc.'},
    {'to_number': '20222', 'code': 'GIVEAKF',
        'name': 'American Kidney Fund, Inc.'},
    {'to_number': '20222', 'code': 'PREVENT',
        'name': 'American Kidney Fund, Inc.'},
    {'to_number': '20222', 'code': 'FLOWER',
        'name': 'AIDS Healthcare Foundation'},
    {'to_number': '20222', 'code': 'AARDA',
        'name': 'American Autoimmune Related Diseases'},
    {'to_number': '501501', 'code': 'AUDI',
        'name': 'Best Buddies International'},
    {'to_number': '501501', 'code': 'BEST',
        'name': 'Best Buddies International'},
    {'to_number': '501501', 'code': 'OPOSITIVE',
        'name': 'Best Buddies International'},
    {'to_number': '501501', 'code': 'TOM',
        'name': 'Best Buddies International'},
    {'to_number': '20222', 'code': 'BIGSUNDAY',
        'name': 'Big Sunday'},
    {'to_number': '20222', 'code': 'TACO',
        'name': 'Boys & Girls Clubs in New Jersey, Inc.'},
    {'to_number': '20222', 'code': 'BURN',
        'name': 'Burn Institute'},
    {'to_number': '20222', 'code': 'PENGUINS',
        'name': 'California Academy of Sciences'},
    {'to_number': '25383', 'code': 'ANDY',
        'name': 'Carnegie Institute'},
    {'to_number': '25383', 'code': 'DONATE',
        'name': 'Carnegie Institute'},
    {'to_number': '25383', 'code': 'JOY',
        'name': 'Carnegie Institute'},
    {'to_number': '25383', 'code': 'MINI',
        'name': 'Carnegie Institute'},
    {'to_number': '25383', 'code': 'SUB',
        'name': 'Carnegie Institute'},
    {'to_number': '20222', 'code': 'CQ',
        'name': 'Carthage College'},
    {'to_number': '20222', 'code': 'FLAME',
        'name': 'Carthage College'},
    {'to_number': '20222', 'code': 'EMPOWER',
        'name': 'Center for Family Services'},
    {'to_number': '20222', 'code': 'PARK',
        'name': 'Central Park Conservancy'},
    {'to_number': '20222', 'code': 'BRAVE',
        'name': 'Chinese Community Health Resource Center'},
    {'to_number': '20222', 'code': 'CLRBRK',
        'name': 'Clearbrook'},
    {'to_number': '20222', 'code': 'RID',
        'name': 'Committee to Reduce Infection Deaths'},
    {'to_number': '20222', 'code': 'WECAN',
        'name': 'Community Gatepath'},
    {'to_number': '20222', 'code': 'CRNEWS',
        'name': 'Consumers Union of United States'},
    {'to_number': '20222', 'code': 'CRSAFE',
        'name': 'Consumers Union of United States'},
    {'to_number': '20222', 'code': 'CU',
        'name': 'Consumers Union of United States'},
    {'to_number': '20222', 'code': 'DFCI',
        'name': 'Dana-Farber Cancer Institute, Inc/The Jimmy Fund'},
    {'to_number': '20222', 'code': 'GOSOX',
        'name': 'Dana-Farber Cancer Institute, Inc/The Jimmy Fund'},
    {'to_number': '20222', 'code': 'JIMMY',
        'name': 'Dana-Farber Cancer Institute, Inc/The Jimmy Fund'},
    {'to_number': '20222', 'code': 'RALLY',
        'name': 'Dana-Farber Cancer Institute, Inc/The Jimmy Fund'},
    {'to_number': '52000', 'code': 'TOGETHER',
        'name': 'Foundation for Women'},
    {'to_number': '52000', 'code': 'WOMEN',
        'name': 'Foundation for Women'},
    {'to_number': '20222', 'code': 'FRANKLIN',
        'name': 'Franklin Institute'},
    {'to_number': '20222', 'code': 'HRP',
        'name': 'Friends of Hudson River Park'},
    {'to_number': '52000', 'code': 'COASTER',
        'name': 'Golden Harvest Food Bank'},
    {'to_number': '20222', 'code': 'TETONS',
        'name': 'Grand Teton National Park Foundation'},
    {'to_number': '20222', 'code': 'BECAS',
        'name': 'Hispanic Scholastic Funds Consortium'},
    {'to_number': '20222', 'code': 'GRANT',
        'name': 'Hispanic Scholastic Funds Consortium'},
    {'to_number': '20222', 'code': 'ICAGIVE',
        'name': 'Institute of Contemporary Art Boston'},
    {'to_number': '25383', 'code': 'REFUGEE',
        'name': 'International Rescue Committee, Inc.'},
    {'to_number': '20222', 'code': 'SNIP',
        'name': 'Jason Debus Heigl Foundation'},
    {'to_number': '20222', 'code': 'INVEST',
        'name': 'Junior Achievement USA'},
    {'to_number': '20222', 'code': 'JA',
        'name': 'Junior Achievement USA'},
    {'to_number': '20222', 'code': 'PARE',
        'name': 'Junior Achievement USA'},
    {'to_number': '20222', 'code': 'PREPARE',
        'name': 'Junior Achievement USA'},
    {'to_number': '20222', 'code': 'BSAFE',
        'name': 'Kolel Chibas Jerusalem'},
    {'to_number': '20222', 'code': 'IGIVE',
        'name': 'Kolel Chibas Jerusalem'},
    {'to_number': '20222', 'code': 'BABY',
        'name': 'March of Dimes National Office'},
    {'to_number': '20222', 'code': 'HERO',
        'name': 'March of Dimes National Office'},
    {'to_number': '20222', 'code': 'MEROLA',
        'name': 'Merola Opera Program'},
    {'to_number': '20222', 'code': 'MIFA',
        'name': 'Metropolitan Inter-Faith Association'},
    {'to_number': '20222', 'code': 'AUGIE',
        'name': 'Muscular Dystrophy Association'},
    {'to_number': '20222', 'code': 'HFD',
        'name': 'Muscular Dystrophy Association'},
    {'to_number': '20222', 'code': 'IRISH',
        'name': 'Muscular Dystrophy Association'},
    {'to_number': '20222', 'code': 'MOMA',
        'name': 'Museum of Modern Art'},
    {'to_number': '20222', 'code': 'ACT',
        'name': 'National Aquarium in Baltimore, Inc.'},
    {'to_number': '20222', 'code': 'BLUE',
        'name': 'National Aquarium in Baltimore, Inc.'},
    {'to_number': '20222', 'code': 'OCEAN',
        'name': 'National Aquarium in Baltimore, Inc.'},
    {'to_number': '20222', 'code': 'PROTECT',
        'name': 'National Aquarium in Baltimore, Inc.'},
    {'to_number': '20222', 'code': 'RESTORE',
        'name': 'National Aquarium in Baltimore, Inc.'},
    {'to_number': '20222', 'code': 'JUSTICE',
        'name': 'National Center for Lesbian Rights'},
    {'to_number': '20222', 'code': 'REEF',
        'name': 'National Marine Sanctuary Foundation'},
    {'to_number': '20222', 'code': 'OFR',
        'name': 'Operation First Response'},
    {'to_number': '501501', 'code': 'SAVE',
        'name': 'Project Medishare for Haiti, Inc'},
    {'to_number': '20222', 'code': 'WECARE',
        'name': 'Rapid City Regional Hospital'},
    {'to_number': '501501', 'code': 'CURE',
        'name': 'Roswell Park Alliance Foundation'},
    {'to_number': '20222', 'code': 'SACTREE',
        'name': 'Sacramento Tree Foundation'},
    {'to_number': '52000', 'code': 'UNITE',
        'name': 'Sickle Cell Disease Association of America'},
    {'to_number': '20222', 'code': 'MEALS',
        'name': 'St. Vincent Senior Citizen Nutrition Program dba St. Vincent Meals on Wheels'},
    {'to_number': '20222', 'code': 'FISH',
        'name': 'The New England Aquarium'},
    {'to_number': '20222', 'code': 'LIVEBLUE',
        'name': 'The New England Aquarium'},
    {'to_number': '20222', 'code': 'MYRTLE',
        'name': 'The New England Aquarium'},
    {'to_number': '20222', 'code': 'TURTLE',
        'name': 'The New England Aquarium'},
    {'to_number': '20222', 'code': 'WITNESS',
        'name': 'United States Holocaust Memorial Council'},
    {'to_number': '20222', 'code': 'THANKS',
        'name': 'United Way of Allegheny County'},
    {'to_number': '357357', 'code': 'WWF',
        'name': 'World Wildlife Fund (Coke)'}]

    TEN_DOLLAR_CHARITIES = [
      {'to_number': '20222', 'code': 'ASASHI',
          'name': 'After-School All-Stars'},
      {'to_number': '20222', 'code': 'BEACHWALK',
          'name': 'AIDS Healthcare Foundation'},
      {'to_number': '20222', 'code': 'LIFEGIFT',
          'name': 'AIDS Healthcare Foundation'},
      {'to_number': '20222', 'code': 'MUSICFEST',
          'name': 'AIDS Healthcare Foundation'},
      {'to_number': '20222', 'code': 'ENDALS',
          'name': 'ALS Therapy Development Institute'},
      {'to_number': '41518', 'code': 'ACS',
          'name': 'American Cancer Society, Inc.'},
      {'to_number': '20222', 'code': 'BDAY',
          'name': 'American Cancer Society, Inc.'},
      {'to_number': '20222', 'code': 'CHICAGO',
          'name': 'American Cancer Society, Inc.'},
      {'to_number': '20222', 'code': 'COACH',
          'name': 'American Cancer Society, Inc.'},
      {'to_number': '20222', 'code': 'CURES',
          'name': 'American Cancer Society, Inc.'},
      {'to_number': '41518', 'code': 'PINK',
          'name': 'American Cancer Society, Inc.'},
      {'to_number': '20222', 'code': 'DC51',
          'name': 'ACLU Fund of the National Capital Area'},
      {'to_number': '25383', 'code': 'ACT',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'CURE',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'DIABETES',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'FIGHT1',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'FIGHT2',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'FIGHT3',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'FIGHT',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'TOUR',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'WALK',
          'name': 'American Diabetes Association'},
      {'to_number': '25383', 'code': 'SUPPORT',
          'name': 'American Kidney Fund, Inc.'},
      {'to_number': '20222', 'code': 'KIDNEY',
          'name': 'American Kidney Fund, Inc.'},
      {'to_number': '20222', 'code': 'AKF',
          'name': 'American Kidney Fund, Inc.'},
      {'to_number': '20222', 'code': 'ALAHAITI',
          'name': 'American Library Association'},
      {'to_number': '20222', 'code': 'ALAJAPAN',
          'name': 'American Library Association'},
      {'to_number': '41518', 'code': 'ALA',
          'name': 'American Library Association'},
      {'to_number': '20222', 'code': 'BEACHWALK',
          'name': 'AIDS Healthcare Foundation'},
      {'to_number': '20222', 'code': 'LIFEGIFT',
          'name': 'AIDS Healthcare Foundation'},
      {'to_number': '20222', 'code': 'MUSICFEST',
          'name': 'AIDS Healthcare Foundation'},
      {'to_number': '20222', 'code': 'LFD',
          'name': 'American Conference On Diversity'},
      {'to_number': '20222', 'code': 'ACTION',
          'name': 'American Refugee Committee'},
      {'to_number': '25383', 'code': 'AMERICARES',
          'name': 'Americares'},
      {'to_number': '25383', 'code': 'LIVE',
          'name': 'Americares'},
      {'to_number': '20222', 'code': 'AAFA',
          'name': 'Asthma and Allergy Foundation of America'},
      {'to_number': '501501', 'code': 'ACDC',
          'name': 'Austin Hatcher Foundation for Pediatric Cancer'},
      {'to_number': '501501', 'code': 'HATCH',
          'name': 'Austin Hatcher Foundation for Pediatric Cancer'},
      {'to_number': '501501', 'code': 'WHEELS',
          'name': 'Austin Hatcher Foundation for Pediatric Cancer'},
      {'to_number': '25383', 'code': 'AUTISM',
          'name': 'Autism Speaks US'},
      {'to_number': '501501', 'code': 'BBCA',
          'name': 'Best Buddies International'},
      {'to_number': '501501', 'code': 'BUDDIES',
          'name': 'Best Buddies International'},
      {'to_number': '20222', 'code': 'BRM',
          'name': 'Boise Rescue Mission'},
      {'to_number': '20222', 'code': 'MISSION',
          'name': 'Boise Rescue Mission'},
      {'to_number': '20222', 'code': 'BPLF',
          'name': 'Boston Public Library Foundation'},
      {'to_number': '20222', 'code': 'BEGREATNJ',
          'name': 'Boys & Girls Clubs in New Jersey, Inc.'},
      {'to_number': '20222', 'code': 'BGCN',
          'name': 'Boys & Girls Clubs in New Jersey, Inc.'},
      {'to_number': '20222', 'code': 'BGCUC',
          'name': 'Boys & Girls Clubs in New Jersey, Inc.'},
      {'to_number': '20222', 'code': 'GOGEL',
          'name': 'Boys & Girls Clubs in New Jersey, Inc.'},
      {'to_number': '20222', 'code': 'BGCM',
          'name': 'Boys and Girls Clubs of the Midlands'},
      {'to_number': '20222', 'code': 'BRAC',
          'name': 'BRAC USA, Inc.'},
      {'to_number': '20222', 'code': 'CYI',
          'name': 'Brandywine Health Foundation'},
      {'to_number': '20222', 'code': 'PREVENTBC',
          'name': 'Breast Cancer Fund'},
      {'to_number': '20222', 'code': 'GIVENWA',
          'name': 'Cancer Challenge'},
      {'to_number': '20222', 'code': 'CAP',
          'name': 'Cascade AIDS Project'},
      {'to_number': '20222', 'code': 'CARE',
          'name': 'Cherry Street Mission Ministries'},
      {'to_number': '52000', 'code': 'CHILDREN',
          'name': "Childrens Charity dba Houston Children's Charity"},
      {'to_number': '52000', 'code': 'KIDS',
          'name': "Childrens Charity dba Houston Children's Charity"},
      {'to_number': '20222', 'code': 'ARTSWAVE',
          'name': 'Cincinnati Institute of Fine Arts dba ArtsWave'},
      {'to_number': '25383', 'code': 'HARVEST',
          'name': 'City Harvest'},
      {'to_number': '52000', 'code': 'CLAFLIN',
          'name': 'Claflin University'},
      {'to_number': '20222', 'code': 'WINTER',
          'name': 'Clearwater Marine Aquarium, Inc.'},
      {'to_number': '80100', 'code': 'CSC',
          'name': 'Commonwealth Shakespeare Company'},
      {'to_number': '20222', 'code': 'COMFORT',
          'name': 'Covenant Hospice'},
      {'to_number': '20222', 'code': 'DFMC',
          'name': 'Dana-Farber Cancer Institute, Inc/The Jimmy Fund'},
      {'to_number': '20222', 'code': 'KCANCER',
          'name': 'Dana-Farber Cancer Institute, Inc/The Jimmy Fund'},
      {'to_number': '20222', 'code': 'ADRIAN',
          'name': 'Demi and Ashton Foundation'},
      {'to_number': '20222', 'code': 'DNA',
          'name': 'Demi and Ashton Foundation'},
      {'to_number': '20222', 'code': 'FFG',
          'name': 'Demi and Ashton Foundation'},
      {'to_number': '20222', 'code': 'COVE',
          'name': 'Earth Island Institute'},
      {'to_number': '20222', 'code': 'EII',
          'name': 'Earth Island Institute'},
      {'to_number': '20222', 'code': 'ETCGIVE',
          'name': 'Ensemble Theatre of Cincinnati'},
      {'to_number': '20222', 'code': 'IFRM',
          'name': 'Family Care Center'},
      {'to_number': '40579', 'code': 'FISHER',
          'name': 'Fisher House'},
      {'to_number': '20222', 'code': 'FISHER',
          'name': 'Fisher House'},
      {'to_number': '40579', 'code': 'HERO',
          'name': 'Fisher House'},
      {'to_number': '40579', 'code': 'PATRIOT',
          'name': 'Fisher House'},
      {'to_number': '20222', 'code': 'PATRIOT',
          'name': 'Fisher House'},
      {'to_number': '20222', 'code': 'VETS',
          'name': 'Fisher House'},
      {'to_number': '20222', 'code': 'VET',
          'name': 'Fisher House'},
      {'to_number': '20222', 'code': 'FEEDUS',
          'name': 'Food Bank Coalition of San Luis Obispo'},
      {'to_number': '20222', 'code': 'FIND',
          'name': 'Food in Need of Distribution'},
      {'to_number': '52000', 'code': 'HUNGRY',
          'name': 'Golden Harvest Food Bank'},
      {'to_number': '20222', 'code': 'GBFB',
          'name': 'Greater Boston Food Bank'},
      {'to_number': '20222', 'code': 'HUNGER',
          'name': 'Greater Boston Food Bank'},
      {'to_number': '20222', 'code': 'SOX',
          'name': 'Greater Boston Food Bank'},
      {'to_number': '20222', 'code': 'TURKEY',
          'name': 'Greater Boston Food Bank'},
      {'to_number': '20222', 'code': 'WAAF',
          'name': 'Greater Boston Food Bank'},
      {'to_number': '20222', 'code': 'GBF',
          'name': 'Green Beret Foundation'},
      {'to_number': '20222', 'code': 'GUIDEDOG',
          'name': 'Guide Dog Foundation for the Blind'},
      {'to_number': '20222', 'code': 'VETDOGS',
          'name': 'Guide Dog Foundation for the Blind'},
      {'to_number': '20222', 'code': 'GDB',
          'name': 'Guide Dogs For The Blind'},
      {'to_number': '25383', 'code': 'ALLSTAR',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'BALL',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'BAT',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'BUILD',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'CHILE',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'DETROIT',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'GLOVE',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'HABITAT',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'RMFCHILE',
          'name': 'Habitat for Humanity'},
      {'to_number': '25383', 'code': 'RMFHAITI',
          'name': 'Habitat for Humanity'},
      {'to_number': '52000', 'code': 'BUILD',
          'name': 'Habitat for Humanity International aka Cleveland County Habitat For Humanity'},
      {'to_number': '52000', 'code': 'HOUSE',
          'name': 'Habitat for Humanity International aka Cleveland County Habitat For Humanity'},
      {'to_number': '52000', 'code': 'HOME',
          'name': 'Habitat for Humanity Stanislaus County'},
      {'to_number': '20222', 'code': 'HC',
          'name': 'Harvest Crusades'},
      {'to_number': '20222', 'code': 'NEW',
          'name': 'Harvest Crusades'},
      {'to_number': '20222', 'code': 'POD',
          'name': 'Harvest Crusades'},
      {'to_number': '41518', 'code': 'HEARTS',
          'name': 'Hearts In Motion'},
      {'to_number': '41010', 'code': 'COW',
          'name': 'Heifer Project International'},
      {'to_number': '41010', 'code': 'GIVE',
          'name': 'Heifer Project International'},
      {'to_number': '41010', 'code': 'HEIFER',
          'name': 'Heifer Project International'},
      {'to_number': '41010', 'code': 'POVERTY',
          'name': 'Heifer Project International'},
      {'to_number': '20222', 'code': 'ESTUDIA',
          'name': 'Hispanic Scholastic Funds Consortium'},
      {'to_number': '20222', 'code': 'STUDY',
          'name': 'Hispanic Scholastic Funds Consortium'},
      {'to_number': '41010', 'code': 'GIVEHOPE',
          'name': 'Hope International'},
      {'to_number': '20222', 'code': 'HCGH',
          'name': 'Howard Hospital Foundation'},
      {'to_number': '20222', 'code': 'NICU',
          'name': 'Howard Hospital Foundation'},
      {'to_number': '52000', 'code': 'FARM',
          'name': 'Hunger Task Force, Inc'},
      {'to_number': '52000', 'code': 'FOOD',
          'name': 'Hunger Task Force, Inc'},
      {'to_number': '20222', 'code': 'IMUS',
          'name': 'Imus Ranch'},
      {'to_number': '20222', 'code': 'ISO',
          'name': 'Indiana Symphony Society'},
      {'to_number': '25383', 'code': 'AFRICA',
          'name': 'International Rescue Committee, Inc.'},
      {'to_number': '25383', 'code': 'HUNGER',
          'name': 'International Rescue Committee, Inc.'},
      {'to_number': '25383', 'code': 'LIBYA',
          'name': 'International Rescue Committee, Inc.'},
      {'to_number': '25383', 'code': 'RESCUE',
          'name': 'International Rescue Committee, Inc.'},
      {'to_number': '52000', 'code': 'RETT',
          'name': 'International Rett Syndrome Foundation'},
      {'to_number': '20222', 'code': 'IAVA',
          'name': 'Iraq And Afghanistan Veterans Of America'},
      {'to_number': '20222', 'code': 'FIXIT',
          'name': 'Jason Debus Heigl Foundation'},
      {'to_number': '20222', 'code': 'JCGIVE',
          'name': 'Jenesse Center'},
      {'to_number': '20222', 'code': 'JNF',
          'name': 'Jewish National Fund'},
      {'to_number': '20222', 'code': 'PUSHKA',
          'name': 'Kolel Chibas Jerusalem'},
      {'to_number': '20222', 'code': 'STAGE',
          'name': 'Lookingglass Theatre Company'},
      {'to_number': '501501', 'code': 'MLK',
          'name': 'Lorraine Civil Rights Museum Foundation aka National Civil Rights Museum'},
      {'to_number': '501501', 'code': 'RIGHTS',
          'name': 'Lorraine Civil Rights Museum Foundation aka National Civil Rights Museum'},
      {'to_number': '41010', 'code': 'POWER',
          'name': 'Malaria No More Fund'},
      {'to_number': '20222', 'code': 'HFTH',
          'name': 'Martin Luther King Jr Poor Peoples Church of Love dba Hosea Feed the Hungry and Homeless'},
      {'to_number': '52000', 'code': 'MDSC',
          'name': 'Massachusetts Down Syndrome Congress'},
      {'to_number': '20222', 'code': 'MEDIC',
          'name': 'Medic One Foundation'},
      {'to_number': '25383', 'code': 'MERCY',
          'name': 'Mercy Corp'},
      {'to_number': '25383', 'code': 'WATER',
          'name': 'Mercy Corp'},
      {'to_number': '20222', 'code': 'SUSTAIN',
          'name': 'Metropolitan New York Coordinating Council on Jewish Poverty Aka Met Council'},
      {'to_number': '20222', 'code': 'MDA',
          'name': 'Muscular Dystrophy Association'},
      {'to_number': '25383', 'code': 'PRIDE',
          'name': 'National Gay and Lesbian Task Force Foundation'},
      {'to_number': '20222', 'code': 'SEA',
          'name': 'National Marine Sanctuary Foundation'},
      {'to_number': '41010', 'code': 'DRPHIL',
          'name': 'National Network to End Domestic Violence Fund'},
      {'to_number': '41010', 'code': 'HOPE',
          'name': 'National Network to End Domestic Violence Fund'},
      {'to_number': '20222', 'code': 'NOCCA',
          'name': 'New Orleans Center for Creative Arts Institute'},
      {'to_number': '20222', 'code': 'NOJO',
          'name': 'New Orleans Jazz Orchestra'},
      {'to_number': '501501', 'code': 'NWS',
          'name': 'New World Symphony'},
      {'to_number': '20222', 'code': 'BUYMEALS',
          'name': 'Orange County Rescue Mission, Inc.'},
      {'to_number': '20222', 'code': 'COXCARES',
          'name': 'Orange County Rescue Mission, Inc.'},
      {'to_number': '41518', 'code': 'MEALS',
          'name': 'Orange County Rescue Mission, Inc.'},
      {'to_number': '41518', 'code': 'RESCUE',
          'name': 'Orange County Rescue Mission, Inc.'},
      {'to_number': '25383', 'code': 'OXFAM',
          'name': 'Oxfam America Inc.'},
      {'to_number': '20222', 'code': 'PH',
          'name': 'Pacific Historic Parks'},
      {'to_number': '20222', 'code': 'FEST',
          'name': 'Philadelphia Fringe Festival'},
      {'to_number': '20222', 'code': 'FAMILY',
          'name': 'Philadelphia Ronald McDonald House'},
      {'to_number': '20222', 'code': 'PKDCURE',
          'name': 'PKD Foundation'},
      {'to_number': '501501', 'code': 'ISTAND',
          'name': 'Planned Parenthood of the Texas Capital Region'},
      {'to_number': '20222', 'code': 'RETT',
          'name': 'Rett Syndrome Research Trust, Inc.'},
      {'to_number': '20222', 'code': 'RIVER',
          'name': 'River Parks Foundation'},
      {'to_number': '20222', 'code': 'RRFB',
          'name': 'Roadrunner Food Bank'},
      {'to_number': '501501', 'code': 'RPCI',
          'name': 'Roswell Park Alliance Foundation'},
      {'to_number': '20222', 'code': 'SACFOOD',
          'name': 'Sacramento Food Bank & Family Services'},
      {'to_number': '20222', 'code': 'SALVADOR',
          'name': 'Salvadorian American Humanitarian Foundation'},
      {'to_number': '20222', 'code': 'AID',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'DONATE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'DROUGHT',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'EARTHQUAKE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'FLOOD',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'GOODGOES',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'HURRICANE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'MONSOON',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'NEWBORN',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'POOP',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'SAFE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'SAVE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'SUPERHERO',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'SURVIVE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'TSUNAMI',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'TWISTER',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'TYPHOON',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'USKIDS',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '20222', 'code': 'WILDFIRE',
          'name': 'Save the Children Federation, Inc.'},
      {'to_number': '25383', 'code': 'EAT',
          'name': 'Second Harvest Food Bank of Northwest North Carolina'},
      {'to_number': '20222', 'code': 'HOME',
          'name': 'Shelter Association of Washtenaw'},
      {'to_number': '41518', 'code': 'SH',
          'name': 'Sheridan House Family Ministries'},
      {'to_number': '52000', 'code': 'BREAK',
          'name': 'Sickle Cell Disease Association of America'},
      {'to_number': '20222', 'code': 'SAAF',
          'name': 'Southern Arizona AIDS Foundation'},
      {'to_number': '80100', 'code': 'GIFT',
          'name': 'St. Aloysius Orphanage'},
      {'to_number': '80100', 'code': 'HOPE',
          'name': 'St. Aloysius Orphanage'},
      {'to_number': '80100', 'code': 'KIDS',
          'name': 'St. Aloysius Orphanage'},
      {'to_number': '80100', 'code': 'STAR',
          'name': 'St. Aloysius Orphanage'},
      {'to_number': '52000', 'code': 'SHORTS',
          'name': 'Symphony Space'},
      {'to_number': '52000', 'code': 'SPACE',
          'name': 'Symphony Space'},
      {'to_number': '20222', 'code': 'LOVEFLP',
          'name': 'The Free Library of Philadelphia'},
      {'to_number': '20222', 'code': 'BARK',
          'name': 'The Humane Society of Missouri'},
      {'to_number': '20222', 'code': 'BARNBUDDY',
          'name': 'The Humane Society of Missouri'},
      {'to_number': '20222', 'code': 'RESQ',
          'name': 'The Humane Society of Missouri'},
      {'to_number': '20222', 'code': 'SAVEPETS',
          'name': 'The Humane Society of Missouri'},
      {'to_number': '20222', 'code': 'CHIMP',
          'name': 'The Jane Goodall Institute for Wildlife Research, Education and Conservation'},
      {'to_number': '20222', 'code': 'JANE',
          'name': 'The Jane Goodall Institute for Wildlife Research, Education and Conservation'},
      {'to_number': '20222', 'code': 'JGI',
          'name': 'The Jane Goodall Institute for Wildlife Research, Education and Conservation'},
      {'to_number': '20222', 'code': 'LOUDER',
          'name': 'The Jed Foundation'},
      {'to_number': '20222', 'code': 'URLIFE',
          'name': 'The Jed Foundation'},
      {'to_number': '20222', 'code': 'JCC',
          'name': 'The Jewish Community Center in Manhattan'},
      {'to_number': '41518', 'code': 'KIDS',
          'name': 'Tufts Medical Center'},
      {'to_number': '864233', 'code': 'AGUA',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'CHILD',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'FLOODS',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'FOOD',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'FRIEND',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'HAITI',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'KIDS',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'MYANMAR',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'NETS',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'PUMPKIN',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'TAPSCAN',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'TAP',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'TOT',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'WATER',
          'name': 'UNICEF'},
      {'to_number': '864233', 'code': 'ZERO',
          'name': 'UNICEF'},
      {'to_number': '20222', 'code': 'ENDHATE',
          'name': 'United States Holocaust Memorial Council'},
      {'to_number': '20222', 'code': 'LEARN',
          'name': 'United States Holocaust Memorial Council'},
      {'to_number': '20222', 'code': 'REMEMBER',
          'name': 'United States Holocaust Memorial Council'},
      {'to_number': '52000', 'code': 'FOODNOW',
          'name': 'Vermont Foodbank'},
      {'to_number': '52000', 'code': 'BEDS',
          'name': 'Warm Blankets Childrens Foundation'},
      {'to_number': '52000', 'code': 'ORPHAN',
          'name': 'Warm Blankets Childrens Foundation'},
      {'to_number': '52000', 'code': 'FLORIDA',
          'name': 'Wildlife Foundation of Florida'},
      {'to_number': '52000', 'code': 'OCEANS',
          'name': 'Wildlife Foundation of Florida'},
      {'to_number': '52000', 'code': 'WILDLIFE',
          'name': 'Wildlife Foundation of Florida'},
      {'to_number': '52000', 'code': 'YOUTH',
          'name': 'Wildlife Foundation of Florida'},
      {'to_number': '25383', 'code': 'OTM',
          'name': 'WNYC Radio'},
      {'to_number': '25383', 'code': 'RL',
          'name': 'WNYC Radio'},
      {'to_number': '52000', 'code': 'WCS',
          'name': "Women's Center and Shelter of Greater Pittsburgh"},
      {'to_number': '20222', 'code': 'WORLDHOPE',
          'name': 'World Hope International'},
      {'to_number': '20222', 'code': 'EARTH',
          'name': 'World Wildlife Fund US'},
      {'to_number': '20222', 'code': 'PANDA',
          'name': 'World Wildlife Fund US'},
      {'to_number': '20222', 'code': 'TIGERS',
          'name': 'World Wildlife Fund US'},
      {'to_number': '20222', 'code': 'WWF',
          'name': 'World Wildlife Fund US'}]

    def __init__(self, amount):
        if amount == 5:
            charity = choice(Charity.FIVE_DOLLAR_CHARITIES)
            self.amount = '$5'
        else:
            charity = choice(Charity.TEN_DOLLAR_CHARITIES)
            self.amount = '$10'
        self.to_number = charity['to_number']
        self.code = charity['code']
        self.name = charity['name']
