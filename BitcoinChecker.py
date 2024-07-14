from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip84, Bip84Coins, Bip44Changes, Bip39MnemonicGenerator
import concurrent.futures
import threading
import httpx
import json

total_checks = 0
wallet_seeds = []
def gen(count):
    global wallet_seeds
    wallet_seeds.clear()
    generated = 0
    wallets = []
    while generated < count:
        mnemo = Mnemonic("english")
        mnemonic_phrase = mnemo.generate(strength=128)
        seed_bytes = Bip39SeedGenerator(mnemonic_phrase).Generate()
        bip84_mst = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
        bip84_acc = bip84_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        address = bip84_acc.PublicKey().ToAddress()
        wallets.append(str(address))
        wallet_seeds.append(mnemonic_phrase)
        generated = generated + 1
    return wallets

def check():
    data = { 'active': "|".join(gen(300)) }
    thread = threading.Thread(target=req, args=(data,))
    thread.start()

def req(data):
    global wallet_seeds
    global total_checks
    try:
        with httpx.Client() as client:
            response = client.post('https://blockchain.info/balance', data=data, timeout=10)
            if response.status_code == 200:
                total_checks = total_checks + 300
                result_data = json.loads(response.text)
                for index, (address, info) in enumerate(result_data.items()):
                    final_balance = info.get('final_balance', 0)
                    if final_balance != 0:
                        print(f"Seed: {wallet_seeds[index]}, Address: {address}, Final Balance: {final_balance}")
                        with open("found_wallets.txt", "a") as file:
                            file.write(f"Seed: {wallet_seeds[index]}, Address: {address}, Final Balance: {final_balance}\n")
                print('total checks: ' + str(total_checks))
    except Exception as e:
        print(e)
while True:
    check()
