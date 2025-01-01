
## Mining Pool Analysis Scripts

This repository contains a set of scripts designed to analyze Bitcoin blocks, identify which mining pools mined each block, and extract detailed information such as block weights and coinbase transaction data. These scripts read blocks directly from the Bitcoin Core data directory within a specified interval.

### Scripts Overview

#### 1. [`read_blocks.py`](./read_blocks.py)
The `read_blocks.py` script reads blocks from disk using the `libbitcoinkernel` library, accessed through Python wrappers available at [py-bitcoinkernel](https://github.com/stickies-v/py-bitcoinkernel).

##### Prerequisites
1. Install the Python wrapper for `libbitcoinkernel` correctly as described in its [documentation](https://github.com/stickies-v/py-bitcoinkernel/).
2. Stop the `bitcoind` process before running this script.

##### Usage
Run the script with the following command:
```bash
python3 read_blocks.py --datadir=<directory> --chain_type=<chain> --start_height=<height> --end_height=<height> --output=<directory>
```

- `--datadir`: Path to the Bitcoin Core data directory. This allows `libbitcoinkernel` to access block data.
- `--chain_type`: Specify the blockchain network (`main`, `signet`, or `testnet`).
- `--start_height`: Block height to begin analysis.
- `--end_height`: Block height to stop analysis.
- `--output`: Directory where results will be saved (this directory must exist). Results will also appear in the [`./output`](./output) directory (There are some sample output there).

> **Note**: The script's runtime depends on the block interval specified. For larger intervals, execution can take minutes to hours.

---

#### 2. [`pool_matcher.py`](./pool_matcher.py)
This script identifies the mining pool associated with each block by analyzing the `scriptSig` of the coinbase transaction. It uses an open-source list of mining pool tags from [bitcoin-data/mining-pools](https://github.com/bitcoin-data/mining-pools), which is stored locally as [`pool-list.json`](./pool-list.json).

---

#### 3. [`generate_results.py`](./generate_results.py)
Processes and consolidates the results of the block analysis for further evaluation.

---

#### 4. Graph Generation Scripts
The [`./graphs`](./graphs) directory contains scripts to visualize analysis results. These scripts generate various graphs using `pandas`, `seaborn`, and `matplotlib`.

##### Prerequisites
Install the required libraries in a Python virtual environment:
```bash
pip install pandas seaborn matplotlib
```

##### Graph Scripts
- **[`plt_large_coinbase_fig.py`](./graphs/plt_large_coinbase_fig.py)**  
  Generates a box plot showing the distribution of coinbase transaction weights for pools that produce blocks with coinbase weights greater than 4000 WU.

- **[`plt_coinbase_weights_fig.py`](./graphs/plt_coinbase_weights_fig.py)**  
  Creates a line chart displaying the average, minimum, and maximum coinbase transaction weights for various mining pools.

- **[`plt_block_weights_fig.py`](./graphs/plt_block_weights_fig.py)**  
  Produces a line chart illustrating the average, minimum, and maximum block weights for various mining pools.
