# cryptomsg
A simple python package to encrypt and decrypt messages with AES CBC mode.

## Installation
`pip install cryptomsg`

## Usage
``` python
>>> from cryptomsg import CryptoMsg
>>> message = b'YOUR MESSAGE'
>>> # Use default key and iv, not secure.
>>> CryptoMsg().encrypt_msg(message)
b"E\xa8\x02\x08\xa3+m\xce'1\xc2\x1c\xa3\xeb\x06\x05"
>>> CryptoMsg().decrypt_msg(_)
b'YOUR MESSAGE'
>>> # Only set key, and iv is the same as key.
>>> CryptoMsg(b'YOUR KEY').encrypt_msg(message)
b'o\x8e\xa8\x13\xda )\x10zS\xfd\xf5\xae\x90\x95\xfb'
>>> CryptoMsg(b'YOUR KEY').decrypt_msg(_)
b'YOUR MESSAGE'
>>> # Set both key and iv, strongest encryption.
>>> CryptoMsg(b'YOUR KEY', b'YOUR IV').encrypt_msg(message)
b'\xbflr\xf6\xae\xc1\xf9W\xfc\xcd&\xf3R\xd3\x8b\xde'
>>> CryptoMsg(b'YOUR KEY', b'YOUR IV').decrypt_msg(_)
b'YOUR MESSAGE'
```
