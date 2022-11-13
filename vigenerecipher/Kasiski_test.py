def Coin(cip, alp):
    n = len(cip)
    f = 0
    for i in cip:
        if i == alp: # 주어진 ciphertext에서 해당 알파벳의 frequency
            f += 1
    I_c = (f / n) * ((f - 1) / (n - 1))
    return I_c

from string import ascii_uppercase
alphabet_list = list(ascii_uppercase) # 알파벳 대문자 리스트

cipher = "" # Given ciphertext
# m = 2일때
cipher_2_1 = cipher[::2] # x + k_1
cipher_2_2 = cipher[1::2] # x + k_2

sum_2_1 = 0
for a in alphabet_list:
    sum_2_1 += Coin(cipher_2_1, a)
print("m = 2일때 첫 번째 I_c :", sum_2_1)

sum_2_2 = 0
for a in alphabet_list:
    sum_2_2 += Coin(cipher_2_2, a)
print("m = 2일때 두 번째 I_c :", sum_2_2, "\n")

# m = 3일때
cipher_3_1 = cipher[::3] # x + k_1
cipher_3_2 = cipher[1::3] # x + k_2
cipher_3_3 = cipher[2::3] # x + k_3

sum_3_1 = 0
for a in alphabet_list:
    sum_3_1 += Coin(cipher_3_1, a)
print("m = 3일때 첫 번째 I_c :", sum_3_1)

sum_3_2 = 0
for a in alphabet_list:
    sum_3_2 += Coin(cipher_3_2, a)
print("m = 3일때 두 번째 I_c :", sum_3_2)

sum_3_3 = 0
for a in alphabet_list:
    sum_3_3 += Coin(cipher_3_3, a)
print("m = 3일때 세 번째 I_c :", sum_3_3)