import heapq
from collections import defaultdict


# Define a node structure for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For the heapq to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(frequency):
    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        # Pop two nodes with the smallest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the new node back to the heap
        heapq.heappush(heap, merged)

    # The remaining node is the root of the Huffman tree
    return heap[0]


def generate_codes(node, current_code="", codebook={}):
    if node is not None:
        # If this is a leaf node, save the character and its code
        if node.char is not None:
            codebook[node.char] = current_code
        generate_codes(node.left, current_code + "0", codebook)
        generate_codes(node.right, current_code + "1", codebook)
    return codebook


def Huffman_coding(input_string):
    # Step 1: Count the frequency of each character
    frequency = defaultdict(int)
    for char in input_string:
        frequency[char] += 1

    # Step 2: Build the Huffman tree
    huffman_tree = build_huffman_tree(frequency)

    # Step 3: Generate binary codes for each character
    huffman_codes = generate_codes(huffman_tree)

    # Step 4: Encode the input string
    encoded_string = ''.join(huffman_codes[char] for char in input_string)

    return encoded_string