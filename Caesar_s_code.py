def encryptor(user_text, user_key, encryption_or_decryption):
    cypher_text = []
    decrypted_text = []

    for index, letter in enumerate(user_text):
        text_encryption = user_text[(index + user_key) % len(user_text)]
        cypher_text.append(text_encryption)
        text_decryption = user_text[(user_text.index(text_encryption) - user_key) % len(user_text)]
        decrypted_text.append(text_decryption)

    if encryption_or_decryption == 'encryption':
        return cypher_text
    elif encryption_or_decryption == 'decryption':
        return decrypted_text


if __name__ == '__main__':
    print(encryptor('abcdefgklmopmxyz' + ' ,.<>/?\\*-+=_~!@#$%^&*()', 3, 'decryption'))
