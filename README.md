# On the Lack of Transaction Contention and Prioritization Transparency in Blockchains

Consider also visiting our Blockchain Research Group webpage at <https://blockchain.mpi-sws.org>.

This repository shares the scripts and data sets used in the following peer-reviewed academic publications:

* [Dissecting Bitcoin and Ethereum Transactions: On the Lack of Transaction Contention and Prioritization Transparency in Blockchains](./papers/messias-fc23-transaction-prioritization.pdf). Johnnatan Messias, Vabuk Pahari, Balakrishnan Chandrasekaran, Krishna P. Gummadi, and Patrick Loiseau. In Proceedings of the Financial Cryptography and Data Security (FC 2023). Bol, Brač, Croatia. May, 2023.

* [Selfish & Opaque Transaction Ordering in the Bitcoin Blockchain: The Case for Chain Neutrality](./papers/messias_imc2021_btc_tx_ordering.pdf). Johnnatan Messias, Mohamed Alzayat, Balakrishnan Chandrasekaran, Krishna P. Gummadi, Patrick Loiseau, and Alan Mislove. 2021. In ACM Internet Measurement Conference (IMC 2021), November 2-4, 2021, Virtual Event, USA. ACM, New York, NY, USA, 16 pages. <https://doi.org/10.1145/3487552.3487823>

Complementary work:
* [On Blockchain Commit Times: An analysis of how miners choose Bitcoin transactions](./papers/messias-sdbd-20.pdf). Johnnatan Messias and Mohamed Alzayat and Balakrishnan Chandrasekaran and Krishna P. Gummadi. In KDD Workshop on Smart Data for Blockchain and Distributed Ledger (SDBD 2020). Virtual Event. August, 2020.

## Data sets

Data from permissionless blockchains (e.g., Bitcoin and Ethereum) are publicly available. However, accessing them would require the user to deploy a full node of that particular blockchain, which can be challenging due to computing resources (e.g., RAM, internet bandwidth). Bitcoin, for example, allows users to export data from a particular block via an RPC JSON interface. Unfortunately, given a transaction ID, the exported raw JSON does not contain the data from which the transactions spend, making it difficult to roll back the transaction chain to calculate the transaction fees.

To enable scientific reproducibility of our results and other research areas to explore the Bitcoin and Ethereum blockchains, we make our pre-processed Bitcoin and Ethereum data sets available for download [here](https://blockchain.mpi-sws.org/datasets/).

We believe this data set is key to any research group interested in understanding and providing insights into the Bitcoin ecosystem.

### Ethereum

This data set was used in our [FC 2023](./papers/messias-fc23-transaction-prioritization.pdf) paper. It contains the transactions ID (txid), transaction input and output data, fees, transaction receipt data, and other essential features for Ethereum research.

Similarly, the Ethereum data set contains the transactions ID (txid), transaction input and output data, fees, transaction receipt data, and other essential features for Ethereum research.

:warning: The full data set is available for download in a compressed dataframe format (CSV.GZ) [here](https://blockchain.mpi-sws.org/datasets/#files%2Fethereum).

Below are direct links for each part of our data set:

* Blocks: It contains information about the Bitcoin blocks mined from September 8th, 2021 to June 30th, 2022. There are 1,867,000 blocks mined [13,183,000 to 15,049,999]. The data set is available [here](https://blockchain.mpi-sws.org/datasets/files/ethereum/blocks-ethereum-13183000-15049999.csv.gz).

* Transactions: It contains 76 files (~19GB) where the majority of which includes transactions for 25000 blocks. There are 347,629,393 transactions in total. This data set is useful for any Bitcoin data exploration. Available [here](https://blockchain.mpi-sws.org/datasets/#files%2Fethereum%2Ftransactions).

The Ethereum data set description is available at [./docs/ethereum.md](./docs/ethereum.md).

### Bitcoin (2018 -- 2020)

This data set was used in our [FC 2023](./papers/messias-fc23-transaction-prioritization.pdf) paper. It contains the transactions ID (txid), transaction input and output data, fees, among other essential features for Bitcoin research.

This data set contains the transactions ID (txid), transaction input and output data, fees, among other essential features for Bitcoin research.

:warning: The full data set is available for download in a compressed dataframe format (CSV.GZ) [here](https://blockchain.mpi-sws.org/datasets/).

Below are direct links for each part of our data set:

* Blocks: It contains information about the Bitcoin blocks mined betwenn 2018 and 2020. There are 161,954 blocks mined [501,951 to 663,904]. The data set is available [here](https://blockchain.mpi-sws.org/datasets/files/bitcoin/blocks_500000_664000.csv.gz).

* Miners: It describes the miners and their addresses used to receive the block reward. Available [here](https://blockchain.mpi-sws.org/datasets/files/bitcoin/miners_500000_664000.csv.gz).

* Transactions: It contains 325 files (~95GB) where the majority of which includes transactions for 500 blocks. There are 313,575,387 transactions + 161,954 coinbase transactions in total. This data set is useful for any Bitcoin data exploration. Available [here](https://blockchain.mpi-sws.org/datasets/#files%2Fbitcoin%2Ftransactions).

The Bitcoin data set description is available at [./docs/bitcoin.md](./docs/bitcoin.md).

### Bitcoin (2020)

This data set was used in our [IMC 2021](./papers/messias_imc2021_btc_tx_ordering.pdf) paper. It contains the transactions ID (txid), transaction input and output data, fees, among other essential features for Bitcoin research.

This data set contains the transactions ID (txid), transaction input and output data, fees, among other essential features for Bitcoin research.

:warning: The full data set is available for download in a compressed dataframe format (CSV.GZ) [here](https://blockchain.mpi-sws.org/datasets/).

:warning: The notebook available [here](notebook/load-and-process-dataset.ipynb) describes how to load and process our Bitcoin data set. It is useful to compute other relevant attributes e.g., SPPE and PPE values.

Below are direct links for each part of our data set:

* Blocks: It contains information about the Bitcoin blocks mined in 2020. There are 53,214 blocks mined [610,691 to 663,904]. The data set is available [here](https://blockchain.mpi-sws.org/datasets/files/bitcoin/blocks-610691--663904.csv.gz).

* Miners: It describes the miners and their addresses used to receive the block reward. Available [here](https://blockchain.mpi-sws.org/datasets/files/bitcoin/miners-610691--663904.csv.gz).

* Transactions: It contains 107 files (~37GB) where the majority of which includes transactions for 500 blocks. There are 112,489,054 transactions + 53,214 coinbase transactions in total. This data set is useful for any Bitcoin data exploration. Available [here](https://blockchain.mpi-sws.org/datasets/#files%2Fbitcoin%2Ftransactions-2020).

The Bitcoin data set description is available at [./docs/bitcoin.md](./docs/bitcoin.md).

## Transaction accelerators

Transaction Accelerators are services where users pay Mining Pool Operators (MPO) to increase the probability of their transaction inclusion within a few blocks. MPOs get extra incentives (e.g., fiat money or other cryptocurrencies) to prioritize these transactions. Imagine a situation where an MPO also provides a Wallet service to its users, claiming that the transactions issued would get higher priority for inclusion or broadcast to some highly connected nodes. It is somehow some evidence that some MPOs might not purely follow the fee-per-byte strategy to order transactions as know to be the ordering norm.

Examples of Transaction Accelerator services offered by the Mining Pools include:

* BTC.com: <https://pushtx.btc.com>
* ViaBTC: <https://pool.viabtc.com/tools/txaccelerator/>
* Poolin: <https://pushtx.com> and <https://medium.com/poolin/poolin-transaction-accelerator-pushtx-com-b825c857a798>
* F2Pool: <https://www.f2pool.com/pushtx>

### Mining Pools

* [BTC.com](https://btc.com/) is one of the top MPOs currently available. BTC.com claims that their transaction accelerator, in cooperation with "several leading Bitcoin Pools," can increase the probability of confirming transactions within 1 hour to 75%, within 4 hours to 98%. Users must pay a higher amount of money to use their service than they typically pay via network transaction fees. Instead, they argue it is "based on transaction size, bitcoin price, etc." We hypothesize they might use transaction value and time (based on time or even the total number of blocks in the blockchain when they received the transaction) as a parameter for defining the acceleration fees. According to their webpage, this service is not refundable as they cannot trace whether a transaction was accelerated.
* [ViaBTC](https://www.viabtc.com/) offers, on the other hand, the accelerator into two modalities. A free version limited to 100 requests per hour (accepts only transactions with at least 0.0001BTC/kB (10-4 BTC/kB) as the fee) and a paid one similar to the BTC.com, accepting both Bitcoin (BTC), Bitcoin Cash (BTH), and LiteCoin (LTC).
* [Poolin](https://www.poolin.com/) claims that their service can increase the probability of confirming transactions within 1 hour to 80%. They accept payment via WeChat Bitcoin (BTC), Litecoin (LTC), Ethereum (ETH), DogeCoin (DOGE), Zcash (ZEC), and Dash (DASH). Their service is also non-refundable

### How does the payment work?

ViaBTC asks for a Bitcoin Cash (BTH) transfer to a specific address, and they also suggest users not include any transaction fee on the accelerated transaction. We hypothesize that as the MPO will include these transactions in the subsequent blocks, it does not matter whether users have included the transaction fee or not).

On the other hand, BTC.com provides different options of payment separated per region. The payment options include a bank transfer, Bitcoin Cash (BTH), Webmoney service, which also allows users to make the payment in Bitcoins (BTC), Trustpay, and Dotpay services, which enable users to make a bank transfer (e.g., dollar and euro).

#### Curiosities

Both analyzed MPOs claim that the number of transactions increased so much due to the Bitcoin network congestion that the current block size limit is not enough to confirm transactions in due time. Therefore, they provide transaction acceleration services to allow users to confirm their transactions in the next few mined blocks.

### Broadcast transaction services

Some MPOs and other websites also provide services that allow users to resubmit transactions for rebroadcasting them to the peer-to-peer network.

# Transaction fee vs. acceleration price

For this experiment, we took a snapshot of our node's Mempool on 2020-11-24 10:08:41 UTC. This snapshot contains 26,332 unconfirmed transactions. Then, for each transaction, we gather its respective transaction accelerator price (or acceleration fee) via an acceleration service provided by [BTC.com](https://pushtx.btc.com/). We could infer acceleration fees for 23,341 (88.64%) out of 26,332 unconfirmed transactions after this step. Therefore, the following analysis considers the set of transactions that we could infer their respective acceleration price. In our study, 1 BTC worths 18,875.10 USD.

Using acceleration services, users would pay on average 566.3 times higher (std = 4,734.67) and on median 116.64 times higher than they would've paid in Bitcoin transaction fees. The minimum is 0.54, the 25-perc is 51.64, and the 75-perc and the maximum are 351.8 and 428,800, respectively.

![alt text](./images/tx-fees-comparison.png?raw=true)

## Ask a Question

---

* For reporting bugs please use the [blockchain-transaction-ordering/issues](https://github.com/johnnatan-messias/blockchain-transaction-ordering/issues) page.

In case of any issue, please feel free to contact me at johnme@mpi-sws.org

## License

---

If you find it useful, please consider citing our academic peer-reviewed papers:

```
@inproceedings{Messias@FC2023,
  author = {Johnnatan Messias and Vabuk Pahari and Balakrishnan Chandrasekaran and Krishna P. Gummadi and Patrick Loiseau},
  title = {{Dissecting Bitcoin and Ethereum Transactions: On the Lack of Transaction Contention and Prioritization Transparency in Blockchains}},
  booktitle = {Proceedings of the Financial Cryptography and Data Security (FC '23)},
  month = {May},
  year = {2023}
}
```

```
@inproceedings{Messias@IMC2021,
  author = {Johnnatan Messias and Mohamed Alzayat and Balakrishnan Chandrasekaran and Krishna P. Gummadi and Patrick Loiseau and Alan Mislove},
  title = {{Selfish \& Opaque Transaction Ordering in the Bitcoin Blockchain: The Case for Chain Neutrality}},
  booktitle = {Proceedings of the ACM Internet Measurement Conference (IMC '21)},
  month = {November},
  year = {2021}
}
```

```
@inproceedings{messias-sdbd-2020,
  title={On Blockchain Commit Times: An analysis of how miners choose Bitcoin transactions},
  author={Johnnatan Messias and Mohamed Alzayat and Balakrishnan Chandrasekaran and Krishna P. Gummadi},
  booktitle = {Proceedings of the KDD Workshop on Smart Data for Blockchain and Distributed Ledger},
  series = {SDBD '20},
  month = {August},
  year = {2020}
}
```
