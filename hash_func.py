import hashlib 
import sympy 


def create_hash_with_prime(input_data): 
    """Function for creating hash code using prime numbers and SHA-256.
    """

    prime = sympy.nextprime(len(input_data))   # find the prime number closet to data length 
    input_data += str(prime)                   # combine prime number to input data 

    hash_object = hashlib.sha256()             # use SHA-256
    hash_object.update(input_data.encode())    # update data to hash object 
    hash_value = hash_object.hexdigest()       # take hash code under hex sequence 

    return hash_value 


if __name__=="__main__": 
    data = 'Hello world'

    # Create hash code using prime number 
    hash_result = create_hash_with_prime(data)
    print(f'data: {data}')
    print(f'Hash: {hash_result}')
