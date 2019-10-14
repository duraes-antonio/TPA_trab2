# Técnicas de Programação Avançada - 2º Trabalho (Métodos de Ordenação e Estatísticas de Ordem)
Repositório dedicado ao 2º trabalho da disciplina de Técnicas de Programação Avançada do cursos de Sistemas de Informação do IFES (Campus Serra).

## 1. Integrantes
- Antônio Carlos Durães da Silva: <i>antoniocds1996@gmail.com</i>
- Carlos Guilherme Felismino Pedroni
- Lucas Gomes Fleger

## 2. Ambiente e configuração p/ testes e desenvolvimento

### 2.1 Para execução dos testes
- CPU: [i7-8550U](https://ark.intel.com/content/www/us/en/ark/products/122589/intel-core-i7-8550u-processor-8m-cache-up-to-4-00-ghz.html)
- SO: Windows 10 (x64)
- LP: [Python](https://www.python.org/downloads/release/python-368/) (v. 3.6.8)[Requer 3.5+]

<p align=justify><i>
OBS.: Parte considerável (todos algorítimos com arquivos com c*e^i dados, i < 4) dos testes também foram realizados em distribuições Linux e apresentaram resultados dentro do esperado, dessa forma, foram desconsiderados em detrimento da máquina de maior desempenho portar o sistema operacional da Microsoft.
</i></p>

### 2.2 Para codificação
- IDE: [PyCharm Community](https://www.jetbrains.com/pycharm/) (v. 2019.1.2)
- LP: Python (v. 3.6.8)
- SO: XUbuntu 18.04 LTS (x64)

### 2.3 Para escrita do relatório
- Editor LaTex 1 (soft. online): [Overleaf](https://pt.overleaf.com/)
- Editor LaTex 2 (soft. desktop): [TeXstudio](https://www.texstudio.org/) (v. 2.12.16)

## 3. Como executar

Por ser escrito em Python, uma linguagem interpretada e não compilada, o processo de execução é simples:
- Ir para o diretório 'TPA_trab2/src/'
- Executar o comando:
```console
usuario@pc:~$ python3 main.py --alg {PREFIX_ALG} -i PATH_ENTRADA.CSV -o PATH_SAIDA.CSV
```

Argumentos:
- --alg: Recebe o prefixo de 3 letras do algorítimo de ordenação desejado [opcional];
- -i: Caminho completo para o arquivo de entrada, a ser processado e ordenado;
- -o: Caminho do arquivo de saída, com os dados ordenados.

Prefixos dos algoritmos de ordenação:
- hea:  HeapSort
- ins:  InsertionSort
- int:  IntroSort
- mer:  MergeSort
- qui:  QuickSort
- sel:  SelectionSort
- tim:  TimSort

Exemplo concreto:
```console
$ python3 main.py --alg tim -i /home/nelson/in/data_75e5.csv -o /home/nelson/out/tim_75e5.csv
```

Observações:
- <p align=justify><i>OBS. 1: Se o argumento "alg" não for passado, a aplicação entenderá que deverão ser executados todos os 7 algoritimos de ordenação e gerará um arquivo de saída para cada algoritmo. Exemplo: o caminho de saída é '/home/jeff/10e5_saida.csv' irá gerar 'heapsort_10e5_saida.csv', 'insertsort_10e5_saida.csv', 'introsort_10e5_saida.csv', ...</i></p>
- <p align=justify><i>OBS. 2: Caminhos com caracteres de espaçamento e acentuação devem estar entre aspas simples.</i></p>

## 4. Resultados

A duração (em milissegundos) para execução de cada método de ordenação, para cada arquivo de dados, encontram-se no diretório ["resultados"](https://github.com/duraes-antonio/TPA_trab2/tree/master/resultados), com nome seguindo a estrutura "<i>{nome metodo}_{qtd absoluta registros}</i>.csv".
  
### 4.1 Problemas esperados
<span align=justify>
  
  No caso dos algoritmos Insertion Sort e Selection Sort, de natureza quadrática (p/ médio e pior caso, ao menos), não há arquivos de resultados para os arquivos de entrada com 100 mil ou mais registros.

  Considerando que para 100 mil registros, os algoritmos Quick, Heap e Merge Sort, em seus piores tempos de execução, tiveram duração de 1812 (1.81 seg), 2249 (2.24 seg) e 2291 milissegundos (2.29 seg), respectivamente, o grupo considerou plausível e viável determinar um limite máximo de cerca de 100 vezes o tempo gasto pelo Merge Sort como tempo aceitável para interromper a execução dos métodos Insertion e Selection Sort.

  Tendo em vista que, com 50 mil elementos no conjunto, o algoritmo Insertion Sort levou 370596 milissegundos (370.6 seg ou 6.176 min), o que já excede o máximo de 229100 (100 * 2291) ms, optou-se por não realizar os testes para valores maiores ou iguais a 100 mil registros, considerando que o tempo de ordenação tende a aumentar quadraticamente com o número de dados.
</span>
