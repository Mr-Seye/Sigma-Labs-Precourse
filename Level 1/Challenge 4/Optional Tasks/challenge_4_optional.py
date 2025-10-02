# optional tasks (roman numeral conversion and cipher decoding)

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

def roman_to_int(s):
    values = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}
    
    total = 0
    
    for i in range(len(s)):
        current = values[s[i]]
        
        # Show current symbol and value
        print(f"Symbol: {s[i]}, Value: {current}", end=" ")
        
        # Check subtraction rule
        if i + 1 < len(s) and current < values[s[i + 1]]:
            total -= current
            print(f"=> Subtract {current}, Total = {total}")
        else:
            total += current
            print(f"=> Add {current}, Total = {total}")
    
    print("Final Total:", total)
    return total


roman_to_int("MCMXCIV")

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
decode_message(key, message)
