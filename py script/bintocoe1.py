# 8 bit widh coe

import sys
import binascii

def convert_bin_to_coe(bin_filename, coe_filename):
    try:
        with open(bin_filename, 'rb') as f_in:
            binary_data = f_in.read()
            
        with open(coe_filename, 'w') as f_out:
            # Write the required COE headers
            f_out.write("memory_initialization_radix=16;\n")
            f_out.write("memory_initialization_vector=\n")
            
            # Convert bytes to hex strings
            hex_data = binascii.hexlify(binary_data).decode('ascii')
            
            # Format as comma-separated hex values
            formatted_hex = [hex_data[i:i+2] for i in range(0, len(hex_data), 2)]
            
            # Join with commas and add a semicolon at the very end
            f_out.write(',\n'.join(formatted_hex))
            f_out.write(';\n')
            
        print(f"Success! Converted {bin_filename} to {coe_filename}")
        
    except FileNotFoundError:
        print("Error: Could not find the input .bin file.")

# Run the function (change these filenames to match yours!)
convert_bin_to_coe("your_project_name.bin", "output_memory.coe")