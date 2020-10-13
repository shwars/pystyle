#!/bin/bash
#az group create -n pytransfer -l northeurope
#az storage account create -n pytransfer -g pytransfer --sku Standard_LRS
key=`az storage account keys list -n pytransfer -g pytransfer -o tsv | grep key1 | cut -f3`
echo storage_key = \'$key\' > config.py
echo storage_acct = \'pytransfer\' >> config.py
cp config.py ../styleservice