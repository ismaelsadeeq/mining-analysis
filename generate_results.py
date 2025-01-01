import os
import json

OUTPUT_DIR = './output/'
START_BLOCK = 768728
END_BLOCK = 876041
TOTAL_BLOCKS = END_BLOCK - START_BLOCK


def get_file_content_json(path):
    """Reads the content of a JSON file and returns it as a Python dictionary."""
    with open(path, 'r') as f:
        return json.loads(f.read())


def init_data():
    """Initializes the data structure to store block and pool statistics."""
    return {
        'total_count': 0,
        'large_coinbase': {
            'count': 0,
            'pools': {},
        },
        'large_blocks': {
            'count': 0,
            'pools': {},
            'lowest': {'block_weight': float('inf')},
            'highest': {'block_weight': float('-inf')},
        },
        'small_blocks': {
            'count': 0,
            'pools': {},
            'lowest': {'block_weight': float('inf')},
            'highest': {'block_weight': float('-inf')},
        }
    }


def process_for_coinbase(pool, blocks_data, block):
    """Processes block data for large coinbase transactions (coinbase weight > 4000)."""
    blocks_data['large_coinbase']['count'] += 1
    pool_data = blocks_data['large_coinbase']['pools'].get(pool, {
        'count': 0,
        'coinbase_weight_sum': 0,
        'block_weight_sum': 0,
        'block_weight_average': 0,
        'highest': block,
        'lowest': block,
    })

    pool_data['count'] += 1
    pool_data['coinbase_weight_sum'] += block['coinbase_weight']
    pool_data['block_weight_sum'] += block['block_weight']

    pool_data['average_coinbase_weight'] = pool_data['coinbase_weight_sum'] // pool_data['count']
    pool_data['average_block_weight'] = pool_data['block_weight_sum'] // pool_data['count']

    if block['coinbase_weight'] > pool_data['highest']['coinbase_weight']:
        pool_data['highest'] = block

    if block['coinbase_weight'] < pool_data['lowest']['coinbase_weight']:
        pool_data['lowest'] = block

    blocks_data['large_coinbase']['pools'][pool] = pool_data


def process_for_size(blocks_data, pool, key, block):
    """Processes block data for size-related statistics (large/small blocks)."""
    blocks_data[key]['count'] += 1

    if block['block_weight'] > blocks_data[key]['highest']['block_weight']:
        blocks_data[key]['highest'] = block

    if block['block_weight'] < blocks_data[key]['lowest']['block_weight']:
        blocks_data[key]['lowest'] = block

    pool_data = blocks_data[key]['pools'].get(pool, {
        'count': 0,
        'block_weight_sum': 0,
        'block_weight_average': 0,
        'highest': block,
        'lowest': block,
    })

    pool_data['count'] += 1
    pool_data['block_weight_sum'] += block['block_weight']
    pool_data['block_weight_average'] = pool_data['block_weight_sum'] // pool_data['count']

    if block['block_weight'] > pool_data['highest']['block_weight']:
        pool_data['highest'] = block

    if block['block_weight'] < pool_data['lowest']['block_weight']:
        pool_data['lowest'] = block

    blocks_data[key]['pools'][pool] = pool_data


def process_block(block, blocks_data):
    """Processes each block and updates the relevant statistics."""
    blocks_data['total_count'] += 1
    pool = block['miner']
    coinbase_weight = block['coinbase_weight']
    block_weight = block['block_weight']
    block = {'height': block['block_height'], 'coinbase_weight': coinbase_weight, 'block_weight': block_weight}

    if coinbase_weight > 4000:
        process_for_coinbase(pool, blocks_data, block)

    if block_weight > 3996000:
        process_for_size(blocks_data, pool, 'large_blocks', block)
    else:
        process_for_size(blocks_data, pool, 'small_blocks', block)


def display_coinbase_summary(blocks_data):
    """Displays a summary of large coinbase transactions."""
    for pool, pool_data in blocks_data['large_coinbase']['pools'].items():
        print(f"\nPool Name: {pool}")
        print(f"Average coinbase transaction weight: {pool_data['average_coinbase_weight']}")
        print(f"Average block weight: {pool_data['average_block_weight']}")
        print(f"Lowest coinbase transaction weight: {pool_data['lowest']['coinbase_weight']} at height {pool_data['lowest']['height']}, block weight: {pool_data['lowest']['block_weight']}")
        print(f"Highest coinbase transaction weight: {pool_data['highest']['coinbase_weight']} at height {pool_data['highest']['height']}, block weight: {pool_data['highest']['block_weight']}")


def display_blocks_summary(blocks_data, key):
    """Displays a summary of block sizes (large or small)."""
    for pool, pool_data in blocks_data[key]['pools'].items():
        print(f"\nPool Name: {pool}")
        print(f"Average block weight: {pool_data['block_weight_average']}")
        print(f"Lowest block weight: {pool_data['lowest']['block_weight']} at height {pool_data['lowest']['height']}, coinbase weight: {pool_data['lowest']['coinbase_weight']}")
        print(f"Highest block weight: {pool_data['highest']['block_weight']} at height {pool_data['highest']['height']}, coinbase weight: {pool_data['highest']['coinbase_weight']}")


def process_results(blocks_data):
    """Processes and displays the final results of the analysis."""

    # Display pools with blocks having a high coinbase transaction weight
    print("\nWithin the analyzed blocks, the pools generating blocks with a coinbase transaction weight exceeding 4000 WU are:")
    display_coinbase_summary(blocks_data)

    # Display details of blocks with varying weights
    print("\nThe large blocks with a weight exceeding 3,996,000 WU are:")
    display_blocks_summary(blocks_data, 'large_blocks')
    print("\nThe remaining blocks with a weight less than 3,996,000 WU:")
    display_blocks_summary(blocks_data, 'small_blocks')



def main():
    """Main function to load data, process blocks, and generate results."""
    blocks_data = init_data()
    data_files = os.listdir(path=OUTPUT_DIR)

    for file_name in data_files:
        file_path = os.path.join(OUTPUT_DIR, file_name)
        block = get_file_content_json(file_path)
        for block in block:
            process_block(block, blocks_data)

    process_results(blocks_data)


if __name__ == "__main__":
    main()
