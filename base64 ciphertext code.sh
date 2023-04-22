#!/bin/bash

# Replace this variable with your Base64 ciphertext
base64_ciphertext="SG90IG1pYyBtaWMgd2VlZWVlZWVl"

# Decode the ciphertext
decoded_text=$(echo $base64_ciphertext | base64 -d)

# Print the decoded text
echo "Decoded Text: $decoded_text"