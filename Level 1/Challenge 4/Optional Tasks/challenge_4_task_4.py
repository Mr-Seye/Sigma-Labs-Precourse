# python3 challenge_4_task_4.py

def decode_message(key, message):
    # building the cipher mapping
    seen = set()
    cipher_alphabet = []
    
    for ch in key:
        if ch != " " and ch not in seen:  # skip spaces and duplicates
            seen.add(ch)
            cipher_alphabet.append(ch)
    
    normal_alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    mapping = {cipher_alphabet[i]: normal_alphabet[i] for i in range(26)}
    
    # displaying substitution mapping
    print("Substitution Mapping:")
    for k, v in mapping.items():
        print(f"{k} -> {v}")
    print("-" * 30)
    
    # show decoding steps
    decoded = []
    for ch in message:
        if ch == " ":
            decoded.append(" ")  # spaces remain unchanged
            print(f"Char: ' ' (space) -> ' ' | Currently decoded: {''.join(decoded)}")
        else:
            decoded.append(mapping[ch])
            print(f"Char: {ch} -> {mapping[ch]} | Currently decoded: {''.join(decoded)}")
    
    result = "".join(decoded)
    print("\nFinal Decoded Message:", result)
    return result


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
decode_message(key, message)
