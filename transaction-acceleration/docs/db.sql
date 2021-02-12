-- The database used to store Bitcoin transactions and blocks used in our experiment.

CREATE TABLE blockchain_block (
    block_height INT NOT NULL,
    block_hash TEXT NOT NULL,
    block_json JSONB NOT NULL,
    PRIMARY KEY(block_height, block_hash)
);

CREATE TABLE blockchain_transaction (
    txid TEXT NOT NULL,
    block_height INT NOT NULL,
    block_hash TEXT NOT NULL,
    tx_json JSONB NOT NULL,
    tx_position INT NOT NULL,
    FOREIGN KEY (block_height, block_hash) REFERENCES blockchain_block (block_height, block_hash) ON DELETE CASCADE,
    PRIMARY KEY(txid, block_height)
);

CREATE INDEX idx_blockchain_transaction_txid ON blockchain_transaction(txid);
CREATE INDEX idx_blockchain_transaction_block_height ON blockchain_transaction(block_height);

CREATE INDEX idx_blockchain_block_hash ON blockchain_block(block_hash);
CREATE INDEX idx_blockchain_block_height ON blockchain_block(block_height);

-- block_json includes the raw data of a block (in a JSON format) collected from our full-node, running the Bitcoin core code, via an RPC call
-- tx_json includes the raw data of a transaction (in a JSON format) collected from our full-node, running the Bitcoin core code, via an RPC call
