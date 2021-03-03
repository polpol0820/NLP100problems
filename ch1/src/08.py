def cipher(s):
    ans = ""
    for i in range(len(s)):
        if s[i].islower():
            ans += chr(219-ord(s[i]))
        else:
            ans += s[i]
    return ans
message = "I am a Jumpei Fujino"
print("暗号化：",cipher(message))
print("復号化：",cipher(cipher(message)))