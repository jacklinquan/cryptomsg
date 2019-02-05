# -*- coding: utf-8 -*-
"""A simple python package to encrypt and decrypt messages with AES CBC mode.

Author: Quan Lin
License: MIT
Requires: pyaes (a pure python AES implementation)

:Example:
>>> from cryptomsg import CryptoMsg
>>> message = 'YOUR MESSAGE'
>>> # Use default key and iv, not secure.
... CryptoMsg().encrypt_msg(message)
"E\xa8\x02\x08\xa3+m\xce'1\xc2\x1c\xa3\xeb\x06\x05"
>>> CryptoMsg().decrypt_msg(_)
'YOUR MESSAGE'
>>> # Only set key, and iv is the same as key.
... CryptoMsg('YOUR KEY').encrypt_msg(message)
'o\x8e\xa8\x13\xda )\x10zS\xfd\xf5\xae\x90\x95\xfb'
>>> CryptoMsg('YOUR KEY').decrypt_msg(_)
'YOUR MESSAGE'
>>> # Set both key and iv, strongest encryption. 
... CryptoMsg('YOUR KEY', 'YOUR IV').encrypt_msg(message)
'\xbflr\xf6\xae\xc1\xf9W\xfc\xcd&\xf3R\xd3\x8b\xde'
>>> CryptoMsg('YOUR KEY', 'YOUR IV').decrypt_msg(_)
'YOUR MESSAGE'
"""

# Project version
__version__ = '0.1.0'
__all__ = ['CryptoMsg']

import pyaes

def pad_msg16(msg):
    """Pad message with space to the nearest length of multiple of 16.
    
    :param msg: the original message
    :type msg: bytes
    :returns: padded message to the nearest length of multiple of 16.
    :rtype: bytes
    """
    # Calculate number of segments of 16 bytes chunk.
    segs = len(msg) // 16
    if len(msg) % 16 != 0:
        segs += 1
    return msg.ljust(segs * 16)

class CryptoMsg(object):
    """A class to encrypt and decrypt messages with AES CBC mode.
    
    Initialization options:
        # With default key and iv, not secure.
        CryptoMsg()
        # Only set key, and iv is the same as key.
        CryptoMsg('YOUR KEY')
        # Set both key and iv, strongest encryption. 
        CryptoMsg('YOUR KEY', 'YOUR IV')
        
    The given key is padded with space to 16 bytes (if shorter than 16 bytes)
    or padded with space to 32 bytes (if length is between 16 and 32)
    or truncated to 32 bytes (if longer than 32 bytes).
    The given iv is padded with space or truncated to 16 bytes.
    """
    def __init__(self, aes_cbc_key=b'aes_cbc_key', aes_cbc_iv=None):
        self.aes_cbc_key = aes_cbc_key
        if aes_cbc_iv is None:
            self.aes_cbc_iv = self.aes_cbc_key
        else:
            self.aes_cbc_iv = aes_cbc_iv

    def encrypt_msg(self, msg):
        """Encrypt message.
        
        :param msg: the original message.
        :type msg: bytes
        :returns: the encrypted message.
        :rtype: bytes
        """
        aes = pyaes.AESModeOfOperationCBC(
            pad_msg16(self.aes_cbc_key)[:32],
            iv=pad_msg16(self.aes_cbc_iv)[:16]
        )
        encrypter = pyaes.Encrypter(aes)
        
        cipher = encrypter.feed(msg)
        cipher += encrypter.feed()
        
        return cipher
        
    def decrypt_msg(self, cipher):
        """Decrypt message.
        
        :param cipher: the encrypted message.
        :type cipher: bytes
        :returns: the decrypted message.
        :rtype: bytes
        """
        aes = pyaes.AESModeOfOperationCBC(
            pad_msg16(self.aes_cbc_key)[:32],
            iv=pad_msg16(self.aes_cbc_iv)[:16]
        )
        decrypter = pyaes.Decrypter(aes)
        
        decrypted_msg = decrypter.feed(cipher)
        decrypted_msg += decrypter.feed()
        
        return decrypted_msg

