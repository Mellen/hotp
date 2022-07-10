# HOTP

An implementation of [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238), the RFC for Timed One Time Passwords (TOTP)

Functions:

## totp

Given a secret, will generate a OTP with the scpecified number of digits, based on the UTC time of day. The secret is a byte array. Use like this:

``` python
totp(b'123456789012356', 6)
```

The output for this will be a 6 digit string, like `123456`.

## hotp

Given a secret, and a counter, will generate a OTP that is the same for the same secret+counter pair, based on the UTC time of day. The secret is a byte array. Use like this:

``` python
hotp(b'4321', 5, 6)
# output is 837937
```

The output is an integer, rather than a string.

## dynamicTruncation

Given a value at least 20 bytes long, will truncate that value to 4 bytes, using magic, and return an integer. Use like this:

```python
dynamicTruncation(b'01234567890123456789')
# output is 959459634
```