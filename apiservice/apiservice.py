from flask import request
from flask import Flask, send_file
from config import *
import uuid
from azure.storage.queue import (
        QueueClient, QueueServiceClient, QueueMessage,
        BinaryBase64DecodePolicy, BinaryBase64EncodePolicy
)
from azure.storage.blob import BlockBlobService
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

app = Flask(__name__)

@app.route("/api", methods=["POST"])
def post_pic():
    blob = BlockBlobService(account_name=storage_acct, account_key=storage_key) 
    conn = f"DefaultEndpointsProtocol=https;AccountName={storage_acct};AccountKey={storage_key};EndpointSuffix=core.windows.net"
    queue = QueueClient.from_connection_string(conn,"incoming")
    fn = uuid.uuid4().hex
    blob.create_blob_from_bytes("incoming",fn,request.data)
    queue.send_message(fn)
    return fn

@app.route("/api", methods=["GET"])
def get_url():
    table_service = TableService(account_name=storage_acct, account_key=storage_key)
    fn = request.args.get('id')
    try:
        res = table_service.get_entity('out','main',fn)
        return res.url
    except:
        return ""

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    app.run(host='0.0.0.0')
