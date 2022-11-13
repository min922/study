from string import ascii_uppercase, ascii_lowercase
alphabet_list = list(ascii_uppercase) # 알파벳 대문자 리스트
alphabet_lower = list(ascii_lowercase)# 알파벳 소문자 리스트

cipher = "" #Given ciphertext

decryption = ""
for i in range(len(cipher)):
    if i % 3 == 0:
        decryption += alphabet_lower[(alphabet_list.index(cipher[i]) - 19) % 26]
    elif i % 3 == 1:
        decryption += alphabet_lower[(alphabet_list.index(cipher[i]) - 14) % 26]
    else:
        decryption += alphabet_lower[(alphabet_list.index(cipher[i]) - 15) % 26]
print(decryption)