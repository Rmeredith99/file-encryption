# file-encryption
This is an algorithm that password encrypts text files.

To run the algorithm, run the python file in the command line where it will prompt you for two file names: one to read from and one to write to. Then you will be prompted with a password. This will read the first file, encrypt it, and write it to the second file.

The encryption is entirely based on the password provided as a sort of seed for the generator. Therefore, when an incorrect password is entered the output simply won't be what it should be, but it will still write something to the output file. 

The algorithm to decrypt is the same as the one to encrypt. Running the algorithm twice in a row on file A to file A will do nothing since it will encrypt and then decrypt.
