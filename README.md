
---

# AutoInventoryAutomation

Um script poderoso para automação de digitação e gerenciamento de dados, ideal para tarefas repetitivas em sistemas baseados em texto. Utilizando a biblioteca `pyautogui` para simulação de teclado e mouse, este projeto permite a manipulação de inventários, registros ou quaisquer outras entradas de dados com eficiência e segurança.

---

## 📚 Tabela de Conteúdos
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Configuração](#configuração)
- [Como Usar](#como-usar)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## 🌟 Visão Geral

O **AutoInventoryAutomation** é projetado para acelerar tarefas manuais de entrada de dados, como a digitação de códigos, quantidades e sequências em sistemas que não possuem APIs ou métodos automatizados de integração. Ele inclui funcionalidades para geração de sequências automáticas, processamento de logs e execução paralela com threads.

### **Destaques**:
- **Seguro**: Configuração de fail-safe para parar a execução ao mover o mouse para o canto superior esquerdo.
- **Modular**: Funções bem definidas e reutilizáveis.
- **Rápido**: Utilização de buffer para gravar logs em lote, minimizando o impacto de IO.
- **Simples**: Interface baseada em menu para facilitar o uso.

---

## ⚙️ Funcionalidades

- Digitação automática de entradas de arquivos: `codigo.txt`, `derivacao.txt`, `quantidade.txt` e `sequencia.txt`.
- Geração de logs detalhados da execução em tempo real.
- Medição de tempo para funções principais.
- Geração automática de sequências numéricas baseadas em dados existentes.
- Execução com threads para maior desempenho em operações simultâneas.

---

## 🛠️ Requisitos

Antes de executar o script, certifique-se de ter os seguintes componentes instalados:

### **Bibliotecas Python**
- Python 3.8 ou superior
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [threading](https://docs.python.org/3/library/threading.html) (nativo do Python)

Para instalar a biblioteca necessária, use:
```bash
pip install pyautogui
```

### **Sistema Operacional**
- Compatível com Windows, macOS e Linux.

---

## 📝 Configuração

### 1. Clone o Repositório
```bash
git clone https://github.com/JoaoDev01001/AutoInventoryAutomation.git
cd AutoInventoryAutomation
```

### 2. Arquivos Necessários
Certifique-se de que os arquivos abaixo estão no mesmo diretório do script:
- `codigo.txt`
- `derivacao.txt`
- `quantidade.txt`
- `sequencia.txt`

Se os arquivos não existirem, o script os criará automaticamente.

---

## 🚀 Como Usar

1. **Execute o Script**
   No terminal, execute:
   ```bash
   python auto_inventory_automation.py
   ```

2. **Siga o Menu Interativo**
   Escolha as opções desejadas no menu principal:
   - Digitar códigos
   - Gerar ou digitar sequência
   - Digitar derivações ou quantidades

3. **Falha Segura**
   Mova o mouse para o canto superior esquerdo para interromper a execução, se necessário.

4. **Verifique os Logs**
   O arquivo `Log_Execucao.txt` conterá todos os detalhes das operações realizadas.

---

## 🧱 Estrutura do Código

### **Principais Funções**
- **`processar_arquivo(acao, intervalo, linhas)`**  
  Processa o arquivo linha a linha, simulando a digitação e pressionando uma tecla configurada (`enter` ou `down`).

- **`gerar_sequencia()`**  
  Gera uma sequência numérica baseada no número de linhas no arquivo `codigo.txt`.

- **`log_atividade_buffer(mensagem)`**  
  Adiciona mensagens a um buffer e grava em lote no arquivo de log.

- **`menu()`**  
  Interface de menu principal para escolha das operações.

### **Fail-Safe**
A função de fail-safe (`py.FAILSAFE`) garante que o script pare ao detectar o mouse no canto superior esquerdo da tela.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do projeto.
2. Crie uma branch com a sua feature (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionei minha feature'`).
4. Submeta um pull request.

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

👤 **Autor**: [JoaoDev01001](https://github.com/JoaoDev01001)

---

### Como usar no seu repositório
1. Crie um arquivo chamado `README.md` no diretório raiz do projeto.
2. Cole o conteúdo acima no arquivo.
3. Faça o commit:
   ```bash
   git add README.md
   git commit -m "Adicionado README.md"
   git push
   ```

Está pronto para o GitHub! 🎉 Se precisar de mais alguma coisa, é só pedir. 🚀
