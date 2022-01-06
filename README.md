
# Hoyolab Daily Reward Claimer

Claim multiple account's daily reward without having to go to the website one by one.

>Note: This project is a successor to [genshin.py](https://github.com/thesadru/genshin.py/) to make you easier using the daily reward function




## Usage/Examples
First add accounts to the `accounts.json`, [click here](https://github.com/Cedrugs/hoyolab-daily-reward-claimer#adding-accounts) for more information about adding accounts.
```python
python -m launcher.py
```
Or you can instead create a bat file so you dont have to run it using command prompt.




## Running with bat file
To make it easier running the file, you can use bat file to run this, for example:
```bat
@echo off
Title Hoyolab Daily Reward Claimer
cls
echo "Starting up"
cd "Path to your python interpreter"
python setup.py
```




## Features

- Claim your Hoyolab reward without opening the website
- Ability to claim multiple accounts at the same time




## Adding accounts

First open up `accounts.json`, and the first thing you see should be like this.

```json
{
  "accounts": [
    {"ltuid": "paste the token here", "ltoken": "paste your token here"}
  ]
}
```

You can customize it or even add more accounts like this.

```json
{
  "accounts": [
    {"ltuid": "paste the token here", "ltoken": "paste your token here"},
    {"ltuid": "paste the token here", "ltoken": "paste your token here"},
    {"ltuid": "paste the token here", "ltoken": "paste your token here"}
  ]
}
```

**How can i get my accounts ltuid and ltoken?**

1. Go to hoyolab.com.
2. Login to your account.
3. Press F12 to open Inspect Mode (ie. Developer Tools). 
4. Go to Application, Cookies, https://www.hoyolab.com.
5. Copy ltuid and ltoken.



## Authors

- [@Cedrugs](https://github.com/Cedrugs)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Support

For support please email me at ceds.sam@gmail.com or contact me on discord (Cedric#8394)
