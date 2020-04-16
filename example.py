

import crypto
import argparse


# encrypt a value in the DEFAULT section
args = argparse.Namespace(option='test')
myVar = crypto.encrypt_value(args)


# encrypt a value in mysection and set a value
args = argparse.Namespace(section='mysection', option='myvalue', value='myvalue')
myVar = crypto.encrypt_value(args)


# encrypt a value in mysection and set a value
args = argparse.Namespace(section='mysection', option='myvalue')
myVar = crypto.decrypt_value(args)
print(myVar)

# Encrypt a file my_secret_file.txt with a key prefix of dev
args = argparse.Namespace(file='my_secret_file.txt', key=dev)
myVar = crypto.encrypt_file(args)

# Set an unencrypted value in the configuration file
crypto.set_value_config('url', b'htps://...', '')

# Retreive the unencrypted value
enc_data = crypto.get_value_config('url')
print(enc_data)
