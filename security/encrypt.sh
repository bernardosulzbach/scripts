# Put together by Bernardo Sulzbach. Licensed under the BSD 3-Clause license.

openssl aes-256-cbc -d -in code.tar.aes -out code.tar
tar xf code.tar
rm code.tar
