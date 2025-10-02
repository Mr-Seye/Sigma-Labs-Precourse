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
