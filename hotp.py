#!/usr/bin/env python
import time
import hmac

def hotp(secret, unixtime):
    hs = hmac.new(secret, None, 'sha1')
    fourBytes = dynamicTruncation(hs.digest())


def dynamicTruncation(twentyBytes):
    pass
