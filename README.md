# Setup
The requirements for this project are listed in the requirements.txt file. You can simply install them into your virtual environment

## MacOS
Secp256k1, a dependency of the pybtc library, will require automake on macos. If you have brew installed you can run ```brew install automake```.

## Ubuntu/Debian
Similarly on Ubuntu/Debian ```sudo apt-get install automake```

# Examples
The project uses argparse, so commands will look like this:

### Creating a new Wallet
```python yogurt.py create <wallet_path>```
```python yogurt.py create wallets/main.pickle```
