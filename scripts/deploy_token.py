from brownie import MacToken
from scripts.utils import get_account
from web3 import Web3


initial_supply = Web3.toWei(10000, "ether")


def main():
    account = get_account()
    mac_token = MacToken.deploy(initial_supply, {"from": account})
    print(f"myToken{mac_token}")
