#!/usr/bin/env python
import time
import hmac
import sys
from math import ceil

def totp(secret, digits):
    p = hotp(secret, int(time.time())//30, digits)
    pstr = f'{p:0{digits}}'
    return pstr

def hotp(secret, counter, digits):
    hs = hmac.new(secret, counter.to_bytes(8, byteorder='big'), 'sha1')
    fourByteNumber = dynamicTruncation(hs.digest())
    result = fourByteNumber % (10**digits)
    return result


def dynamicTruncation(twentyBytes):
    lastFourBits = twentyBytes[19]%16
    numberBytes = twentyBytes[lastFourBits:lastFourBits+4]
    number = int.from_bytes(numberBytes, byteorder='big')
    if number.bit_length() == 32:
        number = number - 2**31
    return number
