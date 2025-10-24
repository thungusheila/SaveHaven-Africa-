from hedera_sdk_python import TokenCreateTransaction, TokenMintTransaction
from hedera_client import client  

def create_token(name, symbol, initial_supply):  
    tx = (  
        TokenCreateTransaction()  
        .setTokenName(name)  
        .setTokenSymbol(symbol)  
        .setDecimals(0)  
        .setInitialSupply(initial_supply)  
        .setTreasuryAccountId(client.operatorAccountId)  
        .setAdminKey(client.operatorPublicKey)  
        .freezeWith(client)  
    )  
    signed = tx.sign(client.operatorPrivateKey)  
    receipt = signed.execute(client).getReceipt(client)  
    return receipt.tokenId.toString()  

def mint_token(token_id, amount):  
    tx = (  
        TokenMintTransaction()  
        .setTokenId(token_id)  
        .setAmount(amount)  
        .freezeWith(client)  
    )  
    signed = tx.sign(client.operatorPrivateKey)  
    receipt = signed.execute(client).getReceipt(client)  
    return receipt.status.toString()
