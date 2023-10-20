import cipher

lf = cipher.Merkle_Hellman_Cipher()
lf.initialize_vector()
lf.initialize_Q()
lf.initialize_R()
lf.set_word()
lf.set_string_vector()
lf.generate_public_key()
lf.encrypt()
lf.decrypt()
lf.show_result()