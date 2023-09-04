from cryptography.hazmat.primitives.asymmetric import ec, utils
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import cryptography.hazmat.primitives.serialization as serialization
from cryptography.hazmat.primitives.asymmetric import ec
import prKey as p


# Generate a new ECDSA key pair
def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

# Sign a message with the private key
def sign_message(private_key, message):
    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
    return signature

# Verify the signature with the public key
def verify_signature(public_key, signature, message):
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False
L=[]
# Example usage
def ecdsa(pk,prk):
    with open('blockData1.txt', 'r') as f:
        prk1,pk1=f.readline().split(',')    
    message = b"Hello, world!"
    if str(pk)!=pk1:
        print("Invalid Public key")
    else:    
        """prk = serialization.load_pem_public_key(prk.encode(), backend=ec.ECBackend())"""
        signature = sign_message(prk, b"Hello, world!")

        if verify_signature(pk, signature, message):
            print("Signature is valid")
            p.aES()
        else:
            print("Signature is invalid")
def generateKey():
    private_key, public_key = generate_key_pair()
    L.append(private_key)
    L.append(public_key)
    with open('blockData1.txt', 'w') as f:
        f.write(str(private_key)+','+str(public_key))
    print(public_key)    
    return public_key,private_key