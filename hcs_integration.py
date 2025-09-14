from hedera import TopicCreateTransaction, TopicMessageSubmitTransaction  
from hedera_client import client  

def create_topic():  
    tx = TopicCreateTransaction().freezeWith(client)  
    signed = tx.sign(client.operatorPrivateKey)  
    receipt = signed.execute(client).getReceipt(client)  
    return receipt.topicId.toString()  

def log_event(topic_id, message):  
    tx = (  
        TopicMessageSubmitTransaction()  
        .setTopicId(topic_id)  
        .setMessage(message)  
        .freezeWith(client)  
    )  
    signed = tx.sign(client.operatorPrivateKey)  
    receipt = signed.execute(client).getReceipt(client)  
    return receipt.status.toString()
