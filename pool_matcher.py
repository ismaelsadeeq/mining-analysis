import json
import re

# Load the pool list from the JSON file
with open('./pool-list.json', 'r') as f:
    pools = json.load(f)

# Extract all tags from the pools and map them to their respective pool
tags = []
tag_to_pool = {}
for pool in pools:
    for tag in pool['tags']:
        tags.append(tag)
        tag_to_pool[tag] = pool['name']

def match_pools(miner):
    for tag in tags:
        # Use regex to check if the tag is in the miner string or if the miner string is the tag
        if re.search(re.escape(tag), miner):
            return tag_to_pool[tag]
    return 'unknown pool'

