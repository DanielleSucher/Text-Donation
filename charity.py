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
         'name': 'American Diabetes Association'}]

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
          'name': 'American Diabetes Association'}]

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
