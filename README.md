factom-walletd
===
[![CircleCI](https://circleci.com/gh/FactomProject/factom-walletd/tree/develop.svg?style=svg)](https://circleci.com/gh/FactomProject/factom-walletd/tree/develop)

`factom-walletd` serves the
[factom/wallet/wsapi](https://github.com/FactomProject/factom/tree/master/wallet/wsapi)
interface to the wallet library at
[factom/wallet](https://github.com/FactomProject/factom/tree/master/wallet).

Here is the [API
documentation](https://docs.factom.com/api?shell#factom-walletd-api).

`factom-walletd` manages a database of Factoid and Entry Credit wallets and
uses them to compose transactions for the Factom blockchain. It can compose
transactions for sending Factoids, purchasing Entry Credits, or creating Chains
or Entries.

## Dependencies
### Build Dependencies
- Go >1.10

### Optional Dependencies
- [`factom-cli`](https://github.com/FactomProject/factom-cli)
- [`factomd`](https://github.com/FactomProject/factomd)

## Package distribution
`factom-walletd` is installed with the Factom package found
[here](https://github.com/FactomProject/distribution). This also installs
`factomd` and `factom-cli`.

## Build and install
Alternatively you can build and install from source.
```
go get -u github.com/FactomProject/factom-walletd
go install github.com/FactomProject/factom-walletd
```
