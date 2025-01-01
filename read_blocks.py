import json

from args_man import parse_args
from bitcoin.core import CBlock
from pool_matcher import match_pools
import pbk


# Constants
DEFAULT_MAX_WEIGHT = 3_992_000  # Default maximum block weight
DEFAULT_COINBASE_WEIGHT = 4_000  # Default maximum coinbase transaction weight


# Global data structure to store information
data = []


def process_block(cblock, block_index):
    """
    Processes a block to check for unusual weights and matches it to a mining pool.

    Args:
        cblock (CBlock): The deserialized Bitcoin block.
        block_index: Information about the block's index.
    """
    print(f"Processing block {block_index.height}")

    block_weight = cblock.GetWeight()
    coinbase_tx = cblock.vtx[0]
    miner = coinbase_tx.vin[0].scriptSig.decode(errors="ignore")
    coinbase_weight = coinbase_tx.calc_weight()

    if block_weight > (DEFAULT_MAX_WEIGHT + coinbase_weight) or coinbase_weight > DEFAULT_COINBASE_WEIGHT:
        info = {
            "hash": block_index.block_hash.hex,
            "block_height": block_index.height,
            "block_weight": block_weight,
            "coinbase_weight": coinbase_weight,
            "coinbase_scriptSig": miner,
        }
        miner_name = match_pools(miner)
        info["miner"] = miner_name

        print(
            f"Block {block_index.height}: unusual "
            f"(weight={block_weight}, coinbase={coinbase_weight}, pool={miner_name})"
        )
        data.append(info)


def append_data(file_path, json_data):
    """
    Appends data to a file in JSON format.

    Args:
        file_path (str): Path to the output file.
        json_data (str): JSON string to append.
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(json_data)


def dump_on_interval(block_index, directory):
    """
    Dumps data to a file every 100 processed blocks.

    Args:
        block_index: Information about the current block index.
        directory (str): Directory to save the output files.
    """
    global data
    if data and len(data) % 100 == 0:  # Write every 100 blocks
        file_path = f"{directory}/{block_index.height}.json"

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4))

        data = []
        print(f"Flushed 100 data points to {file_path}")


def main():
    """
    Main function to parse arguments and process blocks.
    """
    args = parse_args()
    chain_man = pbk.load_chainman(args.datadir, args.chain_type)

    for block_index in pbk.block_index_generator(
        chain_man, start=args.start_height, end=args.end_height
    ):
        block_data = chain_man.read_block_from_disk(block_index).data
        cblock = CBlock.deserialize(block_data)

        process_block(cblock, block_index)
        dump_on_interval(block_index, args.output)


if __name__ == "__main__":
    main()
