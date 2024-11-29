from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Hashes a password using werkzeug's security module.
    """
    return generate_password_hash(password)

def verify_password(password, hash):
    """
    Verifies a password against a hash.
    """
    return check_password_hash(hash, password)
