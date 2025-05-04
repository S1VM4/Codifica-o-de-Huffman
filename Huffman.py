import heapq
from collections import Counter

# Classe do nó da árvore de Huffman
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Função para construir a árvore de Huffman
def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

# Função para gerar os códigos binários
def build_codes(root):
    codes = {}

    def generate_code(node, current_code=""):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_code(node.left, current_code + "0")
        generate_code(node.right, current_code + "1")

    generate_code(root)
    return codes

# Função de codificação
def huffman_encoder(text):
    if not text:
        return "", {}
    root = build_huffman_tree(text)
    codes = build_codes(root)
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

# Função de decodificação
def huffman_decoder(encoded_text, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

# Estatísticas de compressão
def huffman_stats(original_text, encoded_text):
    original_bits = len(original_text) * 8
    compressed_bits = len(encoded_text)
    ratio = compressed_bits / original_bits if original_bits > 0 else 0
    saving = (1 - ratio) * 100
    return ratio, saving

# Impressão da árvore de Huffman
def print_huffman_tree(node, indent=""):
    if node is not None:
        if node.char is not None:
            print(f"{indent}'{node.char}' ({node.freq})")
        else:
            print(f"{indent}* ({node.freq})")
        print_huffman_tree(node.left, indent + "  ")
        print_huffman_tree(node.right, indent + "  ")

# Programa principal
if __name__ == "__main__":
    texto = input("Digite o texto para codificar com Huffman: ")

    codificado, dicionario = huffman_encoder(texto)

    print("\nTexto codificado:")
    print(codificado)

    print("\nDicionário de Huffman:")
    for char, code in dicionario.items():
        printable = repr(char) if char != ' ' else "' '"
        print(f"{printable}: {code}")

    decodificado = huffman_decoder(codificado, dicionario)
    print("\nTexto decodificado:")
    print(decodificado)

    razao, ganho = huffman_stats(texto, codificado)
    print(f"\nTaxa de compressão: {razao:.2f}")
    print(f"Ganho de espaço: {ganho:.2f}%")

    print("\nÁrvore de Huffman:")
    print_huffman_tree(build_huffman_tree(texto))
