# Bitcoin data set description

We describe the data set attributes below.

## Blocks

| Attribute | Description |
| --- | --- |
| height | The depth of the block also known as the block height. |
| hash | The hash which satisfies the difficulty to solve the cryptographic puzzle. |
| nTx | Number of transactions included in the block. It also includes the coinbase transaction. |
| bits | A packed representation (called "Bits") for the block actual hexadecimal target. It is basically a compressed target for the next block. |
| size | The serialized block size. It also included witness data. |
| strippedsize | The block size but without witness data. |
| weight | The block weight as defined in BIP 141. To produce the block vsize it is necessary to divide the weight by 4 (vsize=weight/4). |
| vsize | The virtual transaction size (weight/4). |
| time | UNIX timestamp included by the miners during the mining phase. |
| mediantime | The median block time UNIX timestamp. It is computed based on the time of 200 nodes neighbors. |
| nonce | The nonce which satisfies the puzzle. |
| version | the block version. |
| chainwork | Expected number of hashes required to produce the chain up to this block (in hex). |
| difficulty | The difficulty of the puzzle. |
| merkleroot | The merkle root which represents the transactions inserted into the block. |
| versionHex | The block version but in HEX format. |
| nextblockhash | It points to the hash of the next block mined. |
| previousblockhash | It points to the hash of the previous block mined. |

## Miners

| Attribute | Description |
| --- | --- |
| block_height | The depth of the block is also known as the block height. |
| miner | The inferred miner of this particular block. (See our paper for details on how we infer the miner of a block). |
| n_tx | Number of transactions included in the block. It also includes the coinbase transaction.  |
| addresses |  Wallet addresses where the miner sent the block rewards to (a.k.a. miner's addresses). |
| n_addresses | Number of wallet addresses where the miner sent the block rewards to (a.k.a. miner's addresses)  |

## Transactions

| Attribute | Description |
| --- | --- |
| block_height | The depth of the block the transaction is included. |
| miner | The inferred miner of this particular block that contains the transactions. |
| txid | The unique transaction identifier (ID). |
| is_cpfp | It specifies if this transaction is a child-pays-for-parent transaction (CPFP-tx). |
| is_coinbase | It shows if this is a coinbase transaction (i.e., the first transaction in the block used by miners to get the block reward. |
| tx_position | The transaction position in the block. |
| vin | List of JSON objects that specifies the transaction input. |
| vout | List of JSON objects that specifies the transaction output |
| n_vin | Number inputs the transaction has (it also counts invalid addresses or OP_Return opcode). |
| n_vout | Number outputs the transaction has (it also counts invalid addresses or OP_Return opcode). |
| hash | Transaction hash encoded in little-endian hexadecimal (including witness data) |
| vsize | The virtual transaction size (weight/4). |
| size | The number of serialized bytes of the transaction (i.e., transaction serialized size). |
| fee | The transaction fee offered by the issuer in BTC. |
| cfeerate | The fee in a satoshi-per-kilovsize unit (sat-per-kilobyte). |
| satsize | The fee in a satoshi-per-vsize unit (sat-per-byte). |
| feerate | The transaction fee in BTC divided by the transaction vsize in kilobyte (bitcoin-per-kilobyte). |
| version | The transaction version. It could be either 1 or 2, where programs creating transactions using newer consensus rules may use higher version numbers. Version 2 means that [BIP 68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki#specification) applies. |
| locktime | It specifies when a transaction could be considered for inclusion in a block. It could be locked based on two aspects: (i) block height when its value is less than 500 million, and (ii) timestamp in UTC when its value is greater than 500 million. For more detailed information, please see the [Locktime parsing rules](https://developer.bitcoin.org/devguide/transactions.html#locktime-and-sequence-number). |
| n_addresses | Number of transactions that this transaction spends the coins to. |
| n_spends_from | Number of transactions that this transaction spends coints from. |
| spends_from | Transactions (txid) that this transaction spends coins from. |
| n_vin_addresses | Number of wallet addresses the transaction spend coins from. |
| n_vout_addresses | Number of wallet addresses to which the transaction sent the coins. |
| vin_addresses | Wallet addresses and coins transferred used in the transaction input. |
| vout_addresses | Wallet addresses and coins transferred used in the transaction output. |
| n_utxo | It shows if the transaction increases (positive values) or decreases (negative values) the Bitcoin Unspent Transaction Output (UTXO) set. |
