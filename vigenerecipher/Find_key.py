from string import ascii_uppercase
alphabet_list = list(ascii_uppercase) # 알파벳 대문자 리스트
probability = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001]

cipher = "" #Given ciphertext
cipher_3_1 = cipher[::3] # x + k_1
cipher_3_2 = cipher[1::3] # x + k_2
cipher_3_3 = cipher[2::3] # x + k_3

def findKey(cip):
    for g in range(26):
        M_g = 0
        for i in range(26):
            p_i = probability[i]
            f_i_g = cip.count(alphabet_list[(i + g) % 26])
            M_g += p_i * (f_i_g / len(cip))
        print("g =", alphabet_list[g], ":", M_g)

print("////First Key////")
findKey(cipher_3_1)
print("////Second Key////")
findKey(cipher_3_2)
print("////Third Key////")
findKey(cipher_3_3)