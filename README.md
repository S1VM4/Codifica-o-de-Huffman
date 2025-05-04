
# Huffman Encoder/Decoder

Este projeto implementa a **Codificação de Huffman** para compressão e descompressão de textos. A Codificação de Huffman é um algoritmo de compressão sem perdas que reduz o tamanho de arquivos de texto ao atribuir códigos binários mais curtos para caracteres mais frequentes.

## Funcionalidades

- **Encoder**: recebe uma string como entrada e retorna:
  - o texto codificado em binário;
  - um dicionário de Huffman com o código binário de cada caractere.

- **Decoder**: recebe um texto codificado em binário e o dicionário de Huffman e retorna a string original.

- **Estatísticas de compressão**:
  - calcula a taxa de compressão (`taxa = bits_codificados / bits_originais`);
  - calcula o ganho de espaço em porcentagem.

- **Impressão da árvore de Huffman** (visualização em forma de árvore com indentação).


### Exemplo de saída:

```
Digite o texto para codificar com Huffman: exemplo

Texto codificado:
101010001...

Dicionário de Huffman:
'e': 10
'x': 110
...

Texto decodificado:
exemplo

Taxa de compressão: 0.55
Ganho de espaço: 45.00%

Árvore de Huffman:
* (7)
  'e' (2)
  * (5)
    ...
```

## Requisitos

- Python 3.x
- Bibliotecas padrão: `heapq` e `collections`

## Estrutura do Código

- `HuffmanNode`: classe que representa um nó da árvore de Huffman.
- `build_huffman_tree(text)`: constrói a árvore de Huffman a partir de um texto.
- `build_codes(root)`: gera os códigos binários a partir da árvore.
- `huffman_encoder(text)`: codifica o texto.
- `huffman_decoder(encoded_text, codes)`: decodifica o texto.
- `huffman_stats(original_text, encoded_text)`: calcula taxa e ganho de compressão.
- `print_huffman_tree(node)`: imprime a árvore de Huffman.

## Licença

Este projeto é de uso livre para fins educacionais.
