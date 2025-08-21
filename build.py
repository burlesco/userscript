#!/usr/bin/python3
import sys
import re
import os

if len(sys.argv) < 2:
    print("Uso: python3 build.py <arquivo>")
    sys.exit(1)

input_file = sys.argv[1]

# Lê o conteúdo do arquivo
with open(input_file, 'r', encoding='utf-8') as f:
    code = f.read()

webrequest_re = r'// @webRequestItem (.+)\n'
matches = re.findall(webrequest_re, code, re.M)
webrequests = '// @webRequest [{}]\n'.format(','.join(matches))

count = len(matches) - 1
code = re.sub(webrequest_re, '', code, count=count, flags=re.M)
code = re.sub(webrequest_re, webrequests, code)

# Cria a pasta dist/ se não existir
os.makedirs('dist', exist_ok=True)

# Define o arquivo de saída
output_file = os.path.join('dist', os.path.basename(input_file))

# Salva o conteúdo processado
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(code)

print(f"Arquivo buildado salvo em: {output_file}")
