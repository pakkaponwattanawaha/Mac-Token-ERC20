from brownie import accounts, network, config

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        print("My account!!!", accounts[0])
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
