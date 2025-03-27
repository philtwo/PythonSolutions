def longestCommonPrefix(strs) -> str:
    pref = strs[0] # Initialize the prefix with the first string
    pref_len = len(pref) # Get the length of the prefix

    for s in strs[1:]: # Iterate through the rest of the strings
        while pref != s[0:pref_len]: # Compare the prefix with the current string
            pref_len -= 1 # Decrease the length of the prefix until it matches
            if pref_len == 0: # If the prefix length is 0, return an empty string
                return ""
            pref = pref[0:pref_len] # Update the prefix to the new length
    return pref # Return the longest common prefix

#example
strs = ["carshow", "car", "cardoor"]
print(longestCommonPrefix(strs)) # "car"