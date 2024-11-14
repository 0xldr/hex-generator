from web3 import Web3


def generate_hex(ilk: str) -> str:
    return Web3.to_hex(text=ilk)

if __name__ == "__main__":
    ilk = input("Input desired ilk name (case-sensitive)")
    print(generate_hex(ilk))

