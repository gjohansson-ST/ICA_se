# ICA.se Handla API

This integration do use your account credentials.
Insert into configuration.yaml as part of integration installation.

Guide:

```python
 sensor:
   - platform: ica_se
     username: !secret ica_username
     password: !secret ica_password
```
Debug logging (optional)
```python
 logger:
   logs:
     custom_components.ica_se: debug
```
Restart Home Assistant


# API
```
GET https://handla.api.ica.se/api/user/offlineshoppinglists HTTP/1.1
```
```json
{
    "ShoppingLists": [
        {
            "CommentText": "",
            "Id": 10259317,
            "IsPrivate": false,
            "IsSmartList": false,
            "LatestChange": "2020-04-17T12:52:30Z",
            "OfflineId": "3B069ED6-EC67-483E-9E35-D5786E40D0E1",
            "Rows": [
                {
                    "ArticleGroupId": 10,
                    "ArticleGroupIdExtended": 10,
                    "InternalOrder": -2,
                    "IsSmartItem": false,
                    "IsStrikedOver": false,
                    "LatestChange": "2020-04-17T12:52:30Z",
                    "OfflineId": "D347AB14-C7AB-4D4B-B6BC-0689D69EBE80",
                    "ProductName": "mjölk",
                    "Quantity": 0.0,
                    "RowId": 188404310,
                    "SourceId": 11103
                },
                {
                    "ArticleGroupId": 9,
                    "ArticleGroupIdExtended": 9,
                    "InternalOrder": -1,
                    "IsSmartItem": false,
                    "IsStrikedOver": false,
                    "LatestChange": "2020-04-17T12:52:05Z",
                    "OfflineId": "53C7393D-3CE7-4F9A-BAB7-57C5731038AC",
                    "ProductName": "Kaffe Gevalia",
                    "Quantity": 0.0,
                    "RowId": 188404243,
                    "SourceId": 1002443
                }
            ],
            "SortingStore": 0,
            "Title": "Att handla 17 april"
        }
    ]
}
```
```
GET https://handla.api.ica.se/api/user/recipes/ HTTP/1.1
```
```json
{
    "RecipeIds": [
        716096
    ],
    "UserRecipes": [
        {
            "CreationDate": "2020-04-17T14:52:47.817",
            "RecipeId": 716096
        }
    ]
}
```
```
GET https://handla.api.ica.se/api/login HTTP/1.1
```
```json
{
    'FirstName': 'Förnamn',
    'LastName': 'Efternamn',
    'Ttl': 1200,
    'CustomerRole': 7,
    'Id': 123456789.0,
    'ZipCode': '10000',
    'City': 'STOCKHOLM',
    'Gender': 'Man',
    'YearOfBirth': '1900',
    'CardType': 1
}
```
```
GET https://handla.api.ica.se/api/user/cardaccountswithbalance HTTP/1.1
```
```json
{
    "Cards": [
        {
            "Accounts": [],
            "CardTypeCode": "90",
            "CardTypeDescription": "ICA Kundkort utan betala",
            "MaskedCardNumber": "8791",
            "Selected": false
        }
    ],
    "CustomerNumber": 123456789
}
```
```
GET https://handla.api.ica.se/api/user/minbonustransaction HTTP/1.1
```
```json
{
    "TransactionSummaryByMonth": [
        {
            "Month": "4",
            "TransactionForAMonth": [
                {
                    "MarketingName": "Maxi ICA Stormarknad",
                    "TotalDiscount": 9.7,
                    "TransactionDate": "20200410",
                    "TransactionValue": 746.18
                },
                {
                    "MarketingName": "Maxi ICA Stormarknad",
                    "TotalDiscount": 8.8,
                    "TransactionDate": "20200404",
                    "TransactionValue": 704.13
                }
            ],
            "Year": "2020",
            "YearMonthAsDateTime": "2020-04-01T00:00:00"
        },
        {
            "Month": "3",
            "TransactionForAMonth": [
                {
                    "MarketingName": "Maxi ICA Stormarknad",
                    "TotalDiscount": 0.0,
                    "TransactionDate": "20200326",
                    "TransactionValue": 427.87
                },
                {
                    "MarketingName": "Maxi ICA Stormarknad",
                    "TotalDiscount": 0.0,
                    "TransactionDate": "20200321",
                    "TransactionValue": 421.16
                }
            ],
            "Year": "2020",
            "YearMonthAsDateTime": "2020-03-01T00:00:00"
        }
    ]
}
```
```
GET https://handla.api.ica.se/api/user/bonus/getCurrentBonus HTTP/1.1
```
```json
{
    "AccountBalance": {
        "GroupedBalances": [
            {
                "BalanceCode": 1,
                "BalanceDescription": "Stammishjulet",
                "DetailedBalances": [
                    {
                        "BalanceDescription": "ICA-butik",
                        "PointValue": 1453,
                        "SenderId": 1,
                        "VoucherValue": 0
                    },
                    {
                        "BalanceDescription": "Apotek Hjärtat",
                        "PointValue": 0,
                        "SenderId": 2,
                        "VoucherValue": 0
                    },
                    {
                        "BalanceDescription": "ICA Försäkring",
                        "PointValue": 0,
                        "SenderId": 4,
                        "VoucherValue": 0
                    },
                    {
                        "BalanceDescription": "ICA-betalkort",
                        "PointValue": 0,
                        "SenderId": 3,
                        "VoucherValue": 0
                    }
                ],
                "PointValue": 1453,
                "VoucherValue": 0
            }
        ],
        "LoyaltyMonth": "April",
        "NextVoucherValue": 25,
        "PreliminaryBonusText": "Snart dyker din bonus från förra månaden upp här.",
        "RemainingDays": 14,
        "RemainingPoints": 547,
        "RemainingPointsIncludingBoost": 547,
        "ShowPreliminaryBonus": true,
        "TotalVoucherValue": 0,
        "VoucherMonth": "maj"
    },
    "Aquis": [
        {
            "LevelId": 1,
            "PointValueFrom": 0,
            "PointValueTom": 1999,
            "VoucherValue": 0
        },
        {
            "LevelId": 2,
            "PointValueFrom": 2000,
            "PointValueTom": 3999,
            "VoucherValue": 25
        },
        {
            "LevelId": 3,
            "PointValueFrom": 4000,
            "PointValueTom": 5999,
            "VoucherValue": 50
        },
        {
            "LevelId": 4,
            "PointValueFrom": 6000,
            "PointValueTom": 7999,
            "VoucherValue": 75
        },
        {
            "LevelId": 5,
            "PointValueFrom": 8000,
            "PointValueTom": 9999999,
            "VoucherValue": 150
        }
    ],
    "Config": [
        {
            "Key": "StammisBoostText",
            "Value": "Den här månaden kan du få bonus redan vid 1 000 poäng."
        },
        {
            "Key": "StammisBoostAquisText",
            "Value": "Om du samlar mellan 1 000 – 1 999 poäng två månader i rad får du 20 kr i bonus. Du kan få 20 kr varannan månad."
        }
    ],
    "Vouchers": {
        "Active": [],
        "Used": [
            {
                "Description": "Använd: 2020-03-03",
                "SenderId": 0,
                "SubTitle": "Maxi ICA Stormarknad",
                "Title": "Bonus från januari",
                "VoucherAmount": 26,
                "VoucherCode": "3",
                "VoucherType": 0
            },
            {
                "Description": "Använd: 2020-02-06",
                "SenderId": 0,
                "SubTitle": "Maxi ICA Stormarknad",
                "Title": "Bonus från december",
                "VoucherAmount": 25,
                "VoucherCode": "3",
                "VoucherType": 0
            },
            {
                "Description": "Använd: 2019-12-31",
                "SenderId": 0,
                "SubTitle": "Maxi ICA Stormarknad",
                "Title": "Bonus från november",
                "VoucherAmount": 25,
                "VoucherCode": "3",
                "VoucherType": 0
            },
            {
                "Description": "Använd: 2019-11-21",
                "SenderId": 0,
                "SubTitle": "Maxi ICA Stormarknad",
                "Title": "Bonus från oktober",
                "VoucherAmount": 25,
                "VoucherCode": "3",
                "VoucherType": 0
            },
            {
                "Description": "Använd: 2019-10-19",
                "SenderId": 0,
                "SubTitle": "Maxi ICA Stormarknad",
                "Title": "Bonus från september",
                "VoucherAmount": 25,
                "VoucherCode": "3",
                "VoucherType": 0
            }
        ]
    }
}
```
```
GET https://handla.api.ica.se/api/user/bonus/getBonusHistory HTTP/1.1
```
```json
{
    "GroupedBalances": [
        {
            "BalanceCode": 1,
            "BalanceDescription": "Stammishjulet",
            "DetailedBalances": [
                {
                    "BalanceDescription": "ICA-butik",
                    "PointValue": 2960,
                    "SenderId": 1,
                    "VoucherValue": 0
                },
                {
                    "BalanceDescription": "Apotek Hjärtat",
                    "PointValue": 274,
                    "SenderId": 2,
                    "VoucherValue": 0
                },
                {
                    "BalanceDescription": "ICA Försäkring",
                    "PointValue": 0,
                    "SenderId": 4,
                    "VoucherValue": 0
                },
                {
                    "BalanceDescription": "ICA-betalkort",
                    "PointValue": 0,
                    "SenderId": 3,
                    "VoucherValue": 0
                }
            ],
            "PointValue": 3234,
            "VoucherValue": 25
        }
    ],
    "IsPreliminary": false,
    "LoyaltyMonth": "Mars",
    "NextVoucherValue": 0,
    "RemainingDays": 0,
    "RemainingPoints": 0,
    "RemainingPointsIncludingBoost": 0,
    "ShowPreliminaryBonus": false,
    "StatusCode": "D",
    "TotalVoucherValue": 25
}
```
```
GET https://handla.api.ica.se/api/QR/pid HTTP/1.1
```
```json
{
    "pid": "1752500049285338"
}
```
