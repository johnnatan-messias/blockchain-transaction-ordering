# Selfish & Opaque Transaction Ordering in the Bitcoin Blockchain: The Case for Chain Neutrality

This content is part of the following scientific paper: https://people.mpi-sws.org/~johnme/pdf/messias_imc2021_btc_tx_ordering.pdf

```
Selfish & Opaque Transaction Ordering in the Bitcoin Blockchain: The Case for Chain Neutrality.
Johnnatan Messias, Mohamed Alzayat, Balakrishnan Chandrasekaran, Krishna P. Gummadi, Patrick Loiseau, and Alan Mislove.
In Proceedings of the ACM SIGCOMM Internet Measurement Conference (IMC 2021). Virtual Event. November 2021.
```

## Data set

:warning: **The full data set is available for download [here](https://people.mpi-sws.org/~johnme/datasets/).**


Data from permissionless blockchains (e.g., Bitcoin and Ethereum) are publicly available. However, accessing them would require the user to deploy a full node of that particular blockchain, which could be challenging due to computer resources (e.g., RAM, internet bandwidth). Bitcoin, for instance, allows users to export data from a particular block via an RPC JSON interface. Unfortunately, given a transaction ID, its exported raw JSON does not contain the data from which the transactions spend, making it hard to roll back the transactions chain to compute the transaction fees.

To allow scientific reproducibility and other research domains on the Bitcoin blockchain, we make our pre-processed Bitcoin data set available for download [here](https://people.mpi-sws.org/~johnme/datasets/). This data set contains the transactions ID (txid), transaction input and output data, fees, among other essential features for Bitcoin research.

We believe this data set is key to any research group interested in understanding and providing insights into the Bitcoin ecosystem.

Below we include direct links for each part of our data set:

* Blocks: It contains information about the Bitcoin blocks mined in 2020. There are 53,214 blocks mined [610,691 – 663,904]. The data set is available [here](https://people.mpi-sws.org/~johnme/datasets/files/bitcoin/blocks-610691--663904.csv.gz)
* Miners: It describes the miners and their addresses used to receive the block reward. Available [here](https://people.mpi-sws.org/~johnme/datasets/files/bitcoin/miners-610691--663904.csv.gz)
* Transactions: It contains 107 files (~37GB) where the majority of which includes transactions for 500 blocks. There are 112,489,054 transactions + 53,214 coinbase transactions in total. This data set is useful for any Bitcoin data exploration. Available [here](https://people.mpi-sws.org/~johnme/datasets/#files%2Fbitcoin%2Ftransactions).

## Transaction acceleration
Transaction Accelerators are services where users pay Mining Pool Operators (MPO) to increase the probability of their transaction inclusion within a few blocks. MPOs get extra incentives (e.g., fiat money or other cryptocurrencies) to prioritize these transactions. Imagine a situation where an MPO also provides a Wallet service to its users, claiming that the transactions issued would get higher priority for inclusion or broadcast to some highly connected nodes. It is somehow some evidence that some MPOs might not purely follow the fee-per-byte strategy to order transactions as know to be the ordering norm.

Examples of Transaction Accelerator services offered by the Mining Pools include:

 * BTC.com: https://pushtx.btc.com
 * ViaBTC: https://pool.viabtc.com/tools/txaccelerator/
 * Poolin: https://pushtx.com and https://medium.com/poolin/poolin-transaction-accelerator-pushtx-com-b825c857a798
 * F2Pool: https://www.f2pool.com/pushtx
 
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

- For reporting bugs please use the [blockchain-transaction-ordering/issues](https://github.com/johnnatan-messias/blockchain-transaction-ordering/issues) page.

In case of any issue, please feel free to contact me at johnme@mpi-sws.org

## License

---

MIT

