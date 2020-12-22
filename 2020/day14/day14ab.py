"""
day14a - https://adventofcode.com/2020/day/14

--- Day 14: Docking Data ---

* Part 1
The initialization program (your puzzle input) can either update the bitmask or write a value to memory.
Values and memory addresses are both 36-bit unsigned integers.

For example, ignoring bitmasks for a moment, a line like mem[8] = 11 would 
  write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) 
  on the left and the least significant bit (2^0, that is, the 1s bit) on the right.

The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites 
  the corresponding bit in the value, while an X leaves the bit in the value unchanged.

The entire 36-bit address space begins initialized to the value 0 at every address.

Example: Two values in memory are not zero - 101 (at address 7) and 64 (at address 8),
         producing a sum of 165.

Execute the initialization program.
What is the sum of all values left in memory after it completes?
15172047086292

* Part 2
A version 2 decoder chip doesn't modify the values being written at all.
Instead, it acts as a memory address decoder.

Immediately before a value is written to memory, each bit in the bitmask modifies the 
  corresponding bit of the destination memory address in the following way:

- If the bitmask bit is 0, the corresponding memory address bit is unchanged.
- If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
- If the bitmask bit is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates unpredictably.
In practice, this means the floating bits will take on all possible values, 
potentially causing many memory addresses to be written all at once!

Example (different example data than part1!): The sum is 208

Execute the initialization program using an emulator for a version 2 decoder chip.
What is the sum of all values left in memory after it completes?
4197941339968

"""
def load_data():
    data = []
    datafile = 'input-day14'
    with open(datafile, 'r') as input:
        for line in input:
            data.append(line.strip())
    return data


def process_data(instructions, part):
    mem = {}

    for i in instructions:
        if i[:4] == "mask":
            mask = i.split(" = ")[1]

        elif i[:3] == "mem":
            bits = i.split(" = ")
            mem_address = int(bits[0][4:-1])
            value = int(bits[1])

            if part == 1:
                masked_value = apply_mask(value, mask, ["0", "1"])
                mem[mem_address] = int(masked_value, base=2)

            elif part == 2:
                masked_mem_address = apply_mask(mem_address, mask, ["X", "1"])

                # method A uses a list outside the function
                #r = MyResults()
                #assemble_addresses_external_results(masked_mem_address, "", r)
                #addresses = r.results

                # method B uses a list inside the function
                addresses = assemble_addresses_internal_results(masked_mem_address, "", [])

                for address in addresses:
                    mem[address] = value

            #print(f"mem address {mem_address}, value {value}, memory is now {mem[mem_address]}")

    return sum(mem.values())


def apply_mask(value, mask, maskbits):
    # convert value from decimal -> binary -> string, then lop off the '0b' header 
    binval = str(bin(value))[2:]

    # pad the binary string out to 36 0s
    zeros = "0" * (36 - len(binval))
    padded_binval = zeros + binval

    new_value = ""
    # loop through both binary and mask to construct new_value
    for pbv, m in zip(padded_binval, mask):
        if m in maskbits:
            new_value += m
        else:
            new_value += pbv

    return new_value


class MyResults(object):
    def __init__(self):
        self.results = []


def assemble_addresses_external_results(address, s, r):
    """
    I wrote this one first, since I could write it faster. It works.
    Leaving it here for future reference.
    """
    for pos in range(len(address)):
        if address[pos] != "X":
            s += address[pos]
        else:
            assemble_addresses_external_results(address[pos+1:], s + "0", r)
            assemble_addresses_external_results(address[pos+1:], s + "1", r)
            # return here to throw away incomplete strings (<36 characters)
            return

    r.results.append(int(s, base=2))
    #print(f"s {len(s)} {s} - results {r.results} - address {address}")


def assemble_addresses_internal_results(address, s, results):
    """
    Refactored into this self-contained solution. It works.
    """
    for pos in range(len(address)):
        if address[pos] != "X":
            s += address[pos]
        else:
            results = assemble_addresses_internal_results(address[pos+1:], s + "0", results)
            results = assemble_addresses_internal_results(address[pos+1:], s + "1", results)
            # throw away incomplete strings (<36 characters)
            return results

    results.append(int(s, base=2))
    #print(f"s {len(s)} {s} - results {results} - address {address}")
    return results


if __name__ == '__main__':
    data = load_data()
    #print(f"{data} \n")

    results = process_data(data, 1)
    print(f"Part 1 - {results}")

    results = process_data(data, 2)
    print(f"Part 2 - {results}\n")
