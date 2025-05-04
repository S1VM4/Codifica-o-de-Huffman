 Huffman Coding em Python
Este projeto implementa a Codificação de Huffman em Python, permitindo a compressão e descompressão de textos via terminal. Ele também exibe o dicionário de códigos binários, calcula estatísticas de compressão e imprime a estrutura da árvore de Huffman.

✅ Funcionalidades
Encoder
Converte um texto em um código binário comprimido, gerando um dicionário de Huffman.

Decoder
Reconstrói o texto original a partir do código binário e do dicionário gerado.

Estatísticas
Exibe a taxa de compressão e o ganho de espaço obtido após a compressão.

Visualização da Árvore de Huffman
Imprime a árvore de Huffman de forma hierárquica no terminal.



💡 Exemplo de uso
Entrada no terminal:

yaml
Copiar
Editar
Digite o texto para codificar com Huffman: Arthur
Saída esperada:

matlab
Copiar
Editar
Texto codificado:
10111100010011

Dicionário de Huffman:
'u': 00
'h': 01
't': 100
'A': 101
'r': 11

Texto decodificado:
Arthur

Taxa de compressão: 0.29
Ganho de espaço: 70.83%

Árvore de Huffman:
* (6)
  * (2)
    'u' (1)
    'h' (1)
  * (4)
    * (2)
      't' (1)
      'A' (1)
    'r' (2)
