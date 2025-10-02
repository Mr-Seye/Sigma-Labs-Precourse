# python3 challenge_4_task_4.py

def decode_message(key, message):
    # Step 1: Build mapping
    seen = set()
    cipher_alphabet = []
    
    for ch in key:
        if ch != " " and ch not in seen:  # skip spaces and duplicates
            seen.add(ch)
            cipher_alphabet.append(ch)
    
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    mapping = {cipher_alphabet[i]: normal_alphabet[i] for i in range(26)}
    
    # Debug: Show the substitution mapping
    print("Substitution Mapping:")
    for k, v in mapping.items():
        print(f"{k} → {v}")
    print("-" * 30)
    
    # Step 2: Decode message
    decoded = []
    for ch in message:
        if ch == " ":
            decoded.append(" ")  # spaces remain unchanged
            print(f"Char: ' ' (space) → ' ' | Current decoded: {''.join(decoded)}")
        else:
            decoded.append(mapping[ch])
            print(f"Char: {ch} → {mapping[ch]} | Current decoded: {''.join(decoded)}")
    
    result = "".join(decoded)
    print("\nFinal Decoded Message:", result)
    return result


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
decode_message(key, message)
