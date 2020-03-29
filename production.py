from blockchain import Block

blockchain = []

genesis_block = Block(
    "Chancellor on the brink...",
    [
        "Satoshi sent 1 BTC to me",
        "He sent me more BTC"
    ]
)

second_block = Block(
    genesis_block.block_hash,
    [
        "Leroy gave me all his BTC",
        "Callum started to trade Ethereum"
    ]
)

print(genesis_block.block_hash)
print(second_block.block_hash)
