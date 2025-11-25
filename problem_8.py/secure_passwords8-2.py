import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_ssh_keys(output_dir="ssh_keys"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # key
    private_key = rsa.generate_private_key(
        backend=default_backend(),
        public_exponent=65537,
        key_size=2048
    )

    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Save private ey
    with open(os.path.join(output_dir, "id_rsa"), "wb") as f:
        f.write(private_key_bytes)

    # Generate publickey
    public_key = private_key.public_key()

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
    )

    # Save public key
    with open(os.path.join(output_dir, "id_rsa.pub"), "wb") as f:
        f.write(public_key_bytes)

    print(f"SSH key pair generated in: {output_dir}")

generate_ssh_keys()
