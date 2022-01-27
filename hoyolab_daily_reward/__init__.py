import genshin
import asyncio
import json


__all__ = ('genshin_claim', )


class GenshinClaim:

    def __init__(self, accounts: str):
        self.client = genshin.GenshinClient()
        self.cookies = self.get_account_list(accounts)

    def __call__(self):
        asyncio.run(self.claim_reward(self.cookies))

    async def claim_reward(self, cookie: list) -> None:
        try:
            for x in cookie:
                self.client.set_cookies(x)
                get_accounts = await self.client.genshin_accounts()
                account = get_accounts[0].dict()
                account_info = f'{account["uid"]} | {account["nickname"]} (AR {account["level"]})'
                try:
                    reward = await self.client.claim_daily_reward()
                except genshin.AlreadyClaimed:
                    print(f'Reward already claimed for: {account_info}')
                else:
                    print(f'Claimed {reward.amount}x {reward.name} for {account_info}')
        except ValueError:
            print(f'You must atleast add 1 account to claim daily reward.')
        except genshin.InvalidCookies:
            print('This cookies is invalid or already expired, please re-enter a new cookies.')
        except Exception:
            pass
        finally:
            await self.client.close()

    @staticmethod
    def get_account_list(accs: dict) -> list:
        with open(accs, 'r') as acc:
            data = json.load(acc)
        return data['accounts']


genshin_claim = GenshinClaim
