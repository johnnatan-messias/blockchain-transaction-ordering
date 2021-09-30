# Selfish & Opaque Transaction Ordering in the Bitcoin Blockchain: The Case for Chain Neutrality

This content is part of the following scientific paper: https://people.mpi-sws.org/~johnme/pdf/messias_imc2021_btc_tx_ordering.pdf

```
Selfish & Opaque Transaction Ordering in the Bitcoin Blockchain: The Case for Chain Neutrality.
Johnnatan Messias, Mohamed Alzayat, Balakrishnan Chandrasekaran, Krishna P. Gummadi, Patrick Loiseau, and Alan Mislove.
In Proceedings of the ACM SIGCOMM Internet Measurement Conference (IMC 2021). Virtual Event. November, 2021.
```

**The full data set and the remaining code/scripts will be available here by November 4th 2021.**

# Introduction
Transaction Accelerators are services where users pay Mining Pool Operators (MPO) to increase the probability of their transaction inclusion within a few blocks. MPOs get extra incentives (e.g., fiat money or other cryptocurrencies) to prioritize these transactions. Imagine a situation where an MPO also provides a Wallet service to its users, claiming that the transactions issued would get higher priority for inclusion or even broadcasted to some highly connected nodes. It is somehow some evidence that some MPO might not purely follow the fee-per-byte strategy to order transactions as know to be the ordering norm.

Examples of Transaction Accelerator services offered by the Mining Pools include:

 * BTC.com: https://pushtx.btc.com
 * ViaBTC: https://pool.viabtc.com/tools/txaccelerator/
 * Poolin: https://pushtx.com and https://medium.com/poolin/poolin-transaction-accelerator-pushtx-com-b825c857a798
 * F2Pool: https://www.f2pool.com/pushtx
 
## Mining Pools

* [BTC.com](https://btc.com/) is one of the top MPOs currently available. BTC.com claims that their transaction accelerator, in cooperation with "several leading Bitcoin Pools," can increase the probability of confirming transactions within 1 hour to 75%, within 4 hours to 98%. Users must pay a higher amount of money to use their service than they would typically pay via network transaction fees. Instead, they argue it is "based on transaction size, bitcoin price, etc." We hypothesize they might use transaction value and time (based on time or even the total number of blocks in the blockchain when they received the transaction) as a parameter for defining the acceleration fees. According to their webpage, this service is not refundable as they cannot trace whether a transaction was accelerated.
* [ViaBTC](https://www.viabtc.com/) offers, on the other hand, the accelerator into two modalities. A free version limited to 100 requests per hour (accepts only transactions with at least 0.0001BTC/kB (10-4 BTC/kB) as the fee) and a paid one similar to the BTC.com, accepting both Bitcoin (BTC), Bitcoin Cash (BTH), and LiteCoin (LTC).
* [Poolin](https://www.poolin.com/) claims that their service can increase the probability of confirming transactions within 1 hour to 80%. They accept payment via WeChat Bitcoin (BTC), Litecoin (LTC), Ethereum (ETH), DogeCoin (DOGE), Zcash (ZEC), and Dash (DASH). Their service is also non-refundable

### Reasons to Accelerate Transactions

Another reason why different miners might prefer or not prefer certain transactions may include:

* https://home.treasury.gov/news/press-releases/sm556
* https://www.nytimes.com/2019/01/29/world/middleeast/bitcoin-iran-sanctions.html


### How does the payment work?

ViaBTC asks for a Bitcoin Cash (BTH) transfer to a specific address, and they also suggest users not include any transaction fee on the accelerated transaction. We hypothesize that as the MPO will include these transactions in the next blocks, it does not matter whether users have included the transaction fee or not).

On the other hand, BTC.com provides different options of payment separated per region. The payment options include a bank transfer, Bitcoin Cash (BTH), Webmoney service, which also allows users to make the payment in Bitcoins (BTC), Trustpay, and Dotpay services, which enable users to make a bank transfer (e.g., dollar and euro).


#### Curiosities

Both analyzed MPOs claim, due to the Bitcoin network congestion, the number of transactions increased so much that the current block size limit is not enough to confirm transactions in due time. Therefore, they provide transaction acceleration services to allow users to have their transactions confirmed in the next few mined blocks. 

### Broadcast transaction services

Some MPOs and other websites also provide services that allow users to resubmit transactions for rebroadcasting them to the peer-to-peer network.

# Transaction fee vs. acceleration price

For this experiment, we took a snapshot of our node's Mempool on 2020-11-24 10:08:41 UTC. This snapshot contains 26,332 unconfirmed transactions. Then, for each transaction, we gather its respective transaction accelerator price (or acceleration fee) via an acceleration service provided by [BTC.com](https://pushtx.btc.com/). We could infer acceleration fees for 23,341 (88.64%) out of 26,332 unconfirmed transactions after this step. Therefore, the following analysis considers the set of transactions that we could infer their respective acceleration price. In our study, 1 BTC worths 18,875.10 USD.

Using acceleration services, users would pay on average 566.3 times higher (std = 4,734.67) and on median 116.64 times higher than they would've paid in Bitcoin transaction fees. The minimum is 0.54, the 25-perc is 51.64, and the 75-perc and the maximum are 351.8 and 428,800, respectively.

![alt text](./images/tx-fees-comparison.png?raw=true)

# Active experiment on transaction acceleration

We ran an active experiment to accelerate 11 transactions using ViaBTC (for 10 txs.) and Poolin (for 1 tx.) acceleration services with a total cost of 205 €.

Transactions accelerated using ViaBTC services were included by the following miners: Huobi, Binance, F2Pool, AntPool, ViaBTC. Regarding Poolin, the transaction was included by itself hours later.

Using December 1st 2020 as a reference, in the last 24h, these miners had together 55.2% of the computing capacity as follows ([source](https://btc.com/stats/pool?pool_mode=day)):
* F2pool: 19.9% (top-2)
* AntPool: 12.5% (top-3)
* Binance: 9.6 (top-5)
* Huobi: 8.1% (top-7)
* ViaBTC: 5.1% (top-8)

In the last week, they had together 56% of the computing capacity as follows ([source](https://btc.com/stats/pool?pool_mode=week)):
* F2pool: 18.7% (top-1)
* AntPool: 10.6% (top-3)
* Binance: 10.3 (top-4)
* Huobi: 9.3% (top-6)
* ViaBTC: 7.1% (top-7)

## We report the accelerated transactions below

### [ViaBTC accelerator](https://www.viabtc.com/tools/txaccelerator/)

* [35b18e7a119173c8136c460e45d5d2a87d69304f69546f22ebed2c5f3852dbc1](https://explorer.btc.com/btc/transaction/35b18e7a119173c8136c460e45d5d2a87d69304f69546f22ebed2c5f3852dbc1)
     * Paid 0.001254 BTC on 2020-11-26 20:13 and included by Huobi on 2020-11-26 20:35 in the 2nd position of the block height 658805.
     * 2 blocks delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 658803 and included in block height 658805.
     * Miners in the middle: (658804, Binance)
 

* [65765c65acc86bde3d305b2594229af0839b3636aabea49e7255521412baede2](https://explorer.btc.com/btc/transaction/65765c65acc86bde3d305b2594229af0839b3636aabea49e7255521412baede2)
     * Paid 0.001254 BTC (21.16 USD) on 2020-11-27 12:08 and included by F2Pool on 2020-11-27 12:21 in the 73rd position of the block height 658898.
     * 1 block delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 658897 and included in the block height 658898.
     * Miners in the middle: None


* [0c2098e3b3c993f5fc1d188da3b9d0a8731961bb946c4048d7a99fa83129fbf0](https://explorer.btc.com/btc/transaction/0c2098e3b3c993f5fc1d188da3b9d0a8731961bb946c4048d7a99fa83129fbf0)
     * Paid 0.001254 BTC (21.30 USD) on 2020-11-27 14:38 and included by AntPool on 2020-11-27 14:43 in the 2nd position of the block height 658912.
     * 2 blocks delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 658910 and included in the block height 658912.
     * Miners in the middle: (658911, Poolin)


* [1515a78b711558a1508400b36f554d798a31bd97e3852de5bae598e020179af3](https://explorer.btc.com/btc/transaction/1515a78b711558a1508400b36f554d798a31bd97e3852de5bae598e020179af3)
     * Paid 0.001254 BTC (21.33 USD) on 2020-11-27 22:55 and included by Binance on 2020-11-27 23:37 in the 2nd position of the block height 658971.
     * 3 blocks delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 658968 and included in block height 658971.
     * Miners in the middle: (658969, Binance), (658970, BTCPool)


* [48a0a55252bc029286e4af6215d1673e6744216ffc86b3c7b36eeafe640ddaec](https://explorer.btc.com/btc/transaction/48a0a55252bc029286e4af6215d1673e6744216ffc86b3c7b36eeafe640ddaec)
     * Paid 0.001045 BTC (19.38 USD) on 2020-11-30 11:11 and included by ViaBTC on 2020-11-30 11:23 in the 3rd position of the block height 659335.
     * 1 block delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 659334 and included in block height 659335.
     * Miners in the middle: None


* [9a17cfef7e7bda668415a4a4918195669086f0507786a0c971df24a1c3f3734c](https://explorer.btc.com/btc/transaction/9a17cfef7e7bda668415a4a4918195669086f0507786a0c971df24a1c3f3734c)
     * Paid 0.001045 BTC (19.38 USD) on 2020-11-30 11:31 and included by Huobi on 2020-11-30 11:51 in the 2nd position of the block height 659341.
     * 2 blocks delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 659339 and included in block height 659341.
     * Miners in the middle: (659341, Poolin)


* [831b246f748db46d4f52318e39171b0b587165282be3f07135d978ef0795d421](https://explorer.btc.com/btc/transaction/831b246f748db46d4f52318e39171b0b587165282be3f07135d978ef0795d421)
 * Paid 0.001045 BTC (19.38 USD) on 2020-11-30 13:23 and included by AntPool on 2020-11-30 13:45 in the 2nd position of the block height 659351.
 * 1 block delay after the acceleration.
 * The transaction was accelerated when the blockchain's last block height was 659350 and included in block height 659351.
 * Miners in the middle: None


* [1f59bfc1ef2de7b2bc9d3dd3f3e35dba437c25a93d53533a76d604284047096c](https://explorer.btc.com/btc/transaction/1f59bfc1ef2de7b2bc9d3dd3f3e35dba437c25a93d53533a76d604284047096c)
     * Paid 0.001045 BTC (19.38 USD) on 2020-11-30 14:00 and included by F2Pool on 2020-11-30 14:40 in the 111th position of the block height 659355.
     * 3 blocks delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 659352 and included in block height 659355.
     * Miners in the middle: (659353, 1THash&58COIN), (659354, Lubian.com)


* [6942e0751586aa8f37b6cad4eb036373035d74f40ba36277a7d1ef17ca8c06c3](https://explorer.btc.com/btc/transaction/6942e0751586aa8f37b6cad4eb036373035d74f40ba36277a7d1ef17ca8c06c3)
     * Paid 0.001045 BTC (19.38 USD) on 2020-11-30 15:51 and transaction included by Huobi on 2020-11-30 16:18 in the 2nd position of the block height 659362.
     * 2 blocks delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 659360 and included in block height 659362.
     * Miners in the middle: (659361, 1THash&58COIN)


* [8e49e27c5eb6959e26dec8ab36d4dc6508105447ce8892d71c2837934eae825f](https://explorer.btc.com/btc/transaction/8e49e27c5eb6959e26dec8ab36d4dc6508105447ce8892d71c2837934eae825f)
     * Paid 0.001254 BTC (24.72 USD) on 2020-12-01 11:41 and included by ViaBTC on 2020-12-01 11:50 in the 6th position of the block height 659481.
     * 1 block delay after the acceleration.
     * The transaction was accelerated when the blockchain's last block height was 659480 and included in block height 659481.
     * Miners in the middle: None


### [Poolin](https://pushtx.com)
* [5ece8c5de9850b6706f7b0a9dd723a4b5f018d2392cbba3b454259be7e80109a](https://explorer.btc.com/btc/transaction/5ece8c5de9850b6706f7b0a9dd723a4b5f018d2392cbba3b454259be7e80109a)
 * Paid 0.00154879 BTC + fees on 2020-11-26 20:58 and included by Poolin on 2020-11-27 13:00 in the 2nd position of the block 658904.
 
 
### We summarize the results below.

|                                                                            txid                                                                           | block height |  miner  | tx. position |    delay (in blocks)    | acc. cost (BTC)|  vsize (byte)|    feerate (sat-per-vsize)   |       Mempool (# of txs.)     |   Mempool vsize (MB)                | timestamp (in UTC)|
|:---------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------:|:-------:|:------------:|:-------------------:|:-----------------:|:--------------:|:---------------------:|:------------------:|:------------------:|:-----------------:|
|                                                                                                                                                           |          
| [35b18e7a119173c8136c460e45d5d2a87d69304f69546f22ebed2c5f3852dbc1](https://explorer.btc.com/btc/transaction/35b18e7a119173c8136c460e45d5d2a87d69304f69546f22ebed2c5f3852dbc1) | [658805](https://explorer.btc.com/btc/block/658805) |  Huobi  |    2nd   |          2          |      0.001254     |       110      |           2           |     36,644    |        44.63       |  2020-11-26 19:10 |
| [65765c65acc86bde3d305b2594229af0839b3636aabea49e7255521412baede2](https://explorer.btc.com/btc/transaction/65765c65acc86bde3d305b2594229af0839b3636aabea49e7255521412baede2) | [658898](https://explorer.btc.com/btc/block/658898) |  F2Pool |   73th   |          1          |      0.001254     |       110      |           2           |     20,998    |        32.55       |  2020-11-27 11:06 |
| [0c2098e3b3c993f5fc1d188da3b9d0a8731961bb946c4048d7a99fa83129fbf0](https://explorer.btc.com/btc/transaction/0c2098e3b3c993f5fc1d188da3b9d0a8731961bb946c4048d7a99fa83129fbf0) | [658912](https://explorer.btc.com/btc/block/658912) | AntPool |    2nd   |          2          |      0.001254     |       110      |           1           |     30,126    |        38.01       |  2020-11-27 13:38 |
| [1515a78b711558a1508400b36f554d798a31bd97e3852de5bae598e020179af3](https://explorer.btc.com/btc/transaction/1515a78b711558a1508400b36f554d798a31bd97e3852de5bae598e020179af3) | [658971](https://explorer.btc.com/btc/block/658971) | Binance |    2nd   |          3          |      0.001254     |       110      |           1           |     25,922    |        37.89       |  2020-11-27 21:55 |
| [48a0a55252bc029286e4af6215d1673e6744216ffc86b3c7b36eeafe640ddaec](https://explorer.btc.com/btc/transaction/48a0a55252bc029286e4af6215d1673e6744216ffc86b3c7b36eeafe640ddaec) | [659335](https://explorer.btc.com/btc/block/659335) |  ViaBTC |    3rd   |          1          |      0.001045     |       110      |           1           |     15,605    |        9.82        |  2020-11-30 10:09 |
| [9a17cfef7e7bda668415a4a4918195669086f0507786a0c971df24a1c3f3734c](https://explorer.btc.com/btc/transaction/9a17cfef7e7bda668415a4a4918195669086f0507786a0c971df24a1c3f3734c) | [659341](https://explorer.btc.com/btc/block/659341) |  Huobi  |    2nd   |          2          |      0.001045     |       110      |           1           |     14,945    |        9.41        |  2020-11-30 10:28 |
| [831b246f748db46d4f52318e39171b0b587165282be3f07135d978ef0795d421](https://explorer.btc.com/btc/transaction/831b246f748db46d4f52318e39171b0b587165282be3f07135d978ef0795d421) | [659351](https://explorer.btc.com/btc/block/659351) | AntPool |    2nd   |          1          |      0.001045     |       110      |           1           |     10,990    |        8.66        |  2020-11-30 12:22 |
| [1f59bfc1ef2de7b2bc9d3dd3f3e35dba437c25a93d53533a76d604284047096c](https://explorer.btc.com/btc/transaction/1f59bfc1ef2de7b2bc9d3dd3f3e35dba437c25a93d53533a76d604284047096c) | [659355](https://explorer.btc.com/btc/block/659355) |  F2Pool |   111th  |          3          |      0.001045     |       110      |           1           |     17,093    |        11.40       |  2020-11-30 12:58 |
| [6942e0751586aa8f37b6cad4eb036373035d74f40ba36277a7d1ef17ca8c06c3](https://explorer.btc.com/btc/transaction/6942e0751586aa8f37b6cad4eb036373035d74f40ba36277a7d1ef17ca8c06c3) | [659362](https://explorer.btc.com/btc/block/659362) |  Huobi  |    2nd   |          2          |      0.001045     |       110      |           1           |     30,836    |        19.06       |  2020-11-30 14:49 |
| [8e49e27c5eb6959e26dec8ab36d4dc6508105447ce8892d71c2837934eae825f](https://explorer.btc.com/btc/transaction/8e49e27c5eb6959e26dec8ab36d4dc6508105447ce8892d71c2837934eae825f) | [659481](https://explorer.btc.com/btc/block/659481) |  ViaBTC |    6th   |          1          |      0.001254     |       110      |           2           |     30,935    |        22.59       |  2020-12-01 10:40 |




## Ask a Question

---

- For reporting bugs please use the [blockchain-transaction-ordering/issues](https://github.com/johnnatan-messias/blockchain-transaction-ordering/issues) page.

In case of any issue, please feel free to contact me at johnme@mpi-sws.org

## License

---

MIT

