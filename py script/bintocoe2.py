# flexible width coe

import sys
import binascii

def convert_bin_to_coe(bin_filename, coe_filename, word_width_bits):
    # Calculate how many hex characters make up one word
    # (e.g., 8 bits = 2 hex chars, 32 bits = 8 hex chars)
    hex_chars_per_word = word_width_bits // 4 

    try:
        with open(bin_filename, 'rb') as f_in:
            binary_data = f_in.read()
            
        with open(coe_filename, 'w') as f_out:
            f_out.write("memory_initialization_radix=16;\n")
            f_out.write("memory_initialization_vector=\n")
            
            # Convert the raw bytes into one long, continuous hex string
            hex_data = binascii.hexlify(binary_data).decode('ascii')
            
            # Pad the end with zeros if the file size isn't a perfect multiple of the word width
            while len(hex_data) % hex_chars_per_word != 0:
                hex_data += '0'
            
            # Slice the long string into chunks based on your BRAM width
            formatted_hex = [hex_data[i:i+hex_chars_per_word] for i in range(0, len(hex_data), hex_chars_per_word)]
            
            # Write it out, comma separated
            f_out.write(',\n'.join(formatted_hex))
            f_out.write(';\n')
            
        # The depth is simply how many words we ended up with
        depth = len(formatted_hex)
        print(f"Success! Created COE with Width: {word_width_bits}-bit, Depth: {depth}")
        
    except FileNotFoundError:
        print("Error: Could not find the input .bin file.")

# --- SET YOUR SETTINGS HERE ---
# If your BRAM reads 8 bits at a time, use 8. If 32 bits, use 32.
convert_bin_to_coe("design.bin", "counter_8.coe", word_width_bits=8)