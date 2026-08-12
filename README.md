# ArtisanRandom

Hardware-independent BIP39 seed generation for Bitcoin.

ArtisanRandom generates 24-word BIP39 recovery phrases
independently of the random number generator of the hardware
wallet that will later be used to store the wallet.

The project is designed to be simple, transparent and
independently auditable.

## Usage

ArtisanRandom requires Python 3 and has no external dependencies.

1.  Generate 23 random four-digit numbers between `0000` and
    `1999`, using one of the physical procedures described in the
    [specification](docs/artisan_random.md).

2.  Save the numbers, one per line, in `numbers.txt`.

3.  Run:

    ``` 
    python3 artisan_random.py
    ```

    The program reads `numbers.txt` and `bip39.txt` and prints
    the resulting 24-word BIP39 recovery phrase.

The input file must contain exactly 23 numbers. Leading zeros
must be preserved.

The generated phrase is displayed with word numbers starting at
1, which facilitates manual handling and verification.

### Custom input files

The input and word-list files can be specified with:

``` text
python3 artisan_random.py -i <input-file> -w <word-list>
```

The default files are:

- `numbers.txt` — the 23 generated numbers
- `bip39.txt` — the 2048-word BIP39 English word list

## Security

Run ArtisanRandom offline and in a private environment.

Never enter the generated recovery phrase into a web page or
online service.

The complete generation procedure and security considerations are
described in the [ArtisanRandom
specification](docs/artisan_random.md).

## Documentation

- [ArtisanRandom specification](docs/artisan_random.md)

## Testing

`tools/gen_numbers.py` generates random test input for testing the
program. It must not be used for real wallet generation.


## Requirements

- Python 3
- No external Python dependencies
- Works offline
