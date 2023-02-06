# Ethereum data set description

We describe the data set attributes below.

## Blocks data structure ([link](https://github.com/ethereum/go-ethereum/blob/a73f3f45183a347864a1c941930d6f26c6f06ac2/graphql/schema.go#L141))

| Attribute | Description |
| --- | --- |
| difficulty |  It is a measure of the difficulty of mining this block. This can be calculated from the previous block's difficulty level and the timestamp.|
| extraData | It is an arbitrary data field supplied by the miner. |
| gasLimit |  It is the maximum amount of gas that was available to transactions in this block. |
| gasUsed |  It is the amount of gas that was used executing transactions in this block. |
| hash |  It is the block hash of this block. |
| logsBloom |  It is a bloom filter that can be used to check if a block may contain log entries matching a filter. The Bloom filter is composed of indexable information (logger address and log topics) contained in each log entry from the receipt of each transaction in the transactions list. |
| miner |  It is the account that mined this block. |
| mixHash |  It is the hash that was used as an input to the PoW process. It proves combined with the nonce that a sufficient amount of computation has been carried out on this block
| nonce |  It is the block nonce, an 8-byte sequence determined by the miner. A 64-bit value which, combined with the mix-hash, proves that a sufficient amount of computation has been carried out on this block. |
| number |  It is the number of this block, starting at 0 for the genesis block. The genesis block has a number of zero. |
| parentHash |  It is the hash of the parent block's header of this block (previous block). |
| receiptsRoot |  It is the hash of the trie of transaction receipts in this block. |
| sha3Uncles |  It is a hash of all the uncles (AKA ommers) associated with this block. |
| size | The block size in bytes. |
| stateRoot |  It is the hash of the state trie after this block was processed (after all transactions are executed and finalizations applied). |
| timestamp |  It is the unix timestamp at which this block was mined. |
| totalDifficulty |  It is the sum of all difficulty values up to and including this block. |
| transactions |  It is a list of transactions associated with this block. If transactions are unavailable for this block, this field will be null. |
| transactionsRoot |  It is the keccak256 hash of the root of the trie of transactions in this block. |
| uncles |  It is a list of uncles (AKA ommer) blocks associated with this block. If uncles are unavailable, this field will be null. |

## Miners

| Attribute | Description |
| --- | --- |

## Transactions data structure ([link](https://github.com/ethereum/go-ethereum/blob/a73f3f45183a347864a1c941930d6f26c6f06ac2/graphql/schema.go#L73))

| Attribute | Description |
| --- | --- |
| blockHash |  Block hash corresponds to the block this transaction was mined in. This will be null if the transaction has not yet been mined. |
| blockNumber | Block number corresponds to the block this transaction was mined in. This will be null if the transaction has not yet been mined. |
| from | From is the account that sent this transaction - this will always be an externally owned account. |
| gas | It is the maximum amount of gas this transaction can consume (AKA gasLimit). A scalar value equal to the maximum amount of gas should be used in executing this transaction. This is paid up-front before any computation is done and may not be increased later. |
| gasPrice | It is the price offered to miners for gas, in Wei per unit. A scalar value equal to the number of Wei to be paid per unit of gas for all computation costs incurred as a result of the execution of this transaction. |
| hash | It is the hash of this transaction. |
| input | Input is the data supplied to the target of the transaction. |
| nonce | It is the nonce of the account this transaction was generated with. A scalar value equal to the number of transactions sent by the sender. |
| to | To is the account the transaction was sent to. This is null for contract-creating transactions. |
| transactionIndex | Index is the index (AKA position in the block) of this transaction in the parent block. This will be null if the transaction has not yet been mined. |
| value | It is the value, in Wei, sent along with this transaction. A scalar value equal to the number of Wei to be transferred to the message call’s recipient or, in the case of contract creation, as an endowment to the newly created account. |
| v, r, and s | Values corresponding to the signature of the transaction and used to determine the sender of the transaction. |

## Transactions Receipts data structure

| Attribute | Description |
| --- | --- |
| blockHash | Block hash corresponds to the block this transaction was mined in. This will be null if the transaction has not yet been mined. |
| blockNumber | Block number corresponds to the block this transaction was mined in. This will be null if the transaction has not yet been mined. |
| contractAddress | It is is the account that was created by a contract creation transaction. If the transaction was not a contract creation transaction, or has not yet been mined, this field will be null. |
| cumulativeGasUsed | It is the total gas used in the block up to and including this transaction. If the transaction has not yet been mined, this field will be null. |
| from | From is the account that sent this transaction - this will always be an externally owned account. |
| gasUsed | It is the amount of gas that was used in processing this transaction. If the transaction has not yet been mined, this field will be null. |
| logs | Check data structure ?????|
| logsBloom | It is a list of log entries emitted by this transaction. If the transaction has not yet been mined, this field will be null. |
| status | Status is the return status of the transaction. This will be 1 if the transaction succeeded, or 0 if it failed (due to a rollback, or due to running out of gas). If the transaction has not yet been mined, this field will be null. |
| to | To is the account the transaction was sent to. This is null for contract-creating transactions. |
| transactionHash | It is the hash of this transaction. |
| transactionIndex | Index is the index (AKA position in the block) of this transaction in the parent block. This will be null if the transaction has not yet been mined. |
