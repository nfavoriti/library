import uuid

def generate_api_key():
    # Generate 4 segments of 7-character random parts
    segments = [
        uuid.uuid4().hex[:7],  # 7 characters
        uuid.uuid4().hex[:7],  # 7 characters
        uuid.uuid4().hex[:7],  # 7 characters
        uuid.uuid4().hex[:7]   # 7 characters
    ]
    
    # Join segments with dashes
    formatted_key = "-".join(segments).upper()

    return formatted_key

# Example usage
api_key = generate_api_key()
print(api_key)
