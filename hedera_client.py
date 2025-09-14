import os  
from dotenv import load_dotenv  
from hedera import Client, AccountId, PrivateKey  

load_dotenv()  

client = Client.for_name(os.getenv("HEDERA_NETWORK"))  
client.set_operator(  
    AccountId.fromString(os.getenv("OPERATOR_ID")),  
    PrivateKey.fromString(os.getenv("OPERATOR_KEY"))  
)
