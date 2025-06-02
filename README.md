# 🎰 Sorteador de Números com Streamlit

Bem-vindo ao Sorteador de Números! Este é um aplicativo web simples, construído com Streamlit, que permite selecionar um conjunto de números (de 1 a 60) e sortear um número aleatoriamente dentre os selecionados. A principal característica é que os números sorteados não são repetidos dentro de uma mesma sessão de sorteio (para o conjunto atual de números selecionados) até que todos os números escolhidos tenham sido sorteados ou o sorteio seja reiniciado.

## ✨ Funcionalidades

*   **Seleção de Números:** Escolha facilmente os números que deseja incluir no sorteio usando um seletor múltiplo (de 1 a 60).
*   **Sorteio Aleatório:** Com um clique, um número é sorteado aleatoriamente a partir da sua seleção.
*   **Sem Repetição Imediata:** Um número sorteado não será escolhido novamente até que todos os outros números da sua seleção atual tenham sido sorteados, ou até que você reinicie o histórico de sorteios.
*   **Reiniciar Sorteio:** Limpe o histórico de números já sorteados para a seleção atual e comece de novo.
*   **Reinício Automático:** Se você alterar sua seleção de números no seletor múltiplo, o histórico de sorteios é automaticamente reiniciado para a nova seleção.
*   **Feedback Visual:**
    *   Animação de balões ao sortear um número.
    *   Exibição clara do número sorteado.
    *   Lista dos números que você selecionou para o sorteio.
    *   Lista dos números que já foram sorteados na sessão atual.
*   **Interface Amigável:** Design limpo e intuitivo, cortesia do Streamlit.

## ⚙️ Pré-requisitos

*   Python 3.7 ou superior
*   pip (gerenciador de pacotes Python)

## 🚀 Instalação e Execução

1.  **Clone o repositório (se aplicável) ou salve o código:**
    Salve o código Python fornecido em um arquivo, por exemplo, `sorteador_app.py`.

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    A única dependência externa principal é o Streamlit.
    ```bash
    pip install streamlit
    ```

4.  **Execute o aplicativo Streamlit:**
    Navegue até o diretório onde você salvou o arquivo `sorteador_app.py` e execute o seguinte comando no seu terminal:
    ```bash
    streamlit run sorteador_app.py
    ```
    Seu navegador web padrão deve abrir automaticamente com o aplicativo em execução. Caso contrário, o terminal mostrará os endereços (Local URL e Network URL) onde você pode acessá-lo.

## 🕹️ Como Usar

1.  **Abra o aplicativo** no seu navegador (ele deve abrir automaticamente após executar o comando `streamlit run`).
2.  **Selecione os Números:** No campo "Selecione os números disponíveis para o sorteio:", clique e escolha os números (entre 1 e 60) que você deseja incluir. Você pode selecionar quantos quiser.
3.  **Inicie o Sorteio:** Clique no botão "✨ Sortear um número!".
4.  **Veja o Resultado:** O número sorteado será exibido em destaque, acompanhado de uma animação de balões.
5.  **Sorteios Subsequentes:**
    *   Se você clicar em "✨ Sortear um número!" novamente, um novo número será sorteado dentre os selecionados *que ainda não foram sorteados nesta sessão*.
    *   A seção "Números já sorteados nesta sessão" será atualizada.
6.  **Reiniciar o Sorteio:**
    *   Se quiser limpar o histórico de números já sorteados para a seleção atual e começar a sortear do zero com os mesmos números, clique no botão "🔄 Reiniciar Sorteio".
7.  **Alterar Seleção:**
    *   Se você modificar os números escolhidos no seletor múltiplo, o histórico de sorteios será automaticamente zerado para essa nova combinação de números.
8.  **Todos os Números Sorteados:**
    *   Se todos os números da sua seleção atual já tiverem sido sorteados, o aplicativo informará e mostrará balões de celebração. Você pode então "Reiniciar Sorteio" ou alterar sua seleção.

## 🖼️ Exemplo de Interface (Descrição)

*   **Título:** "🎰 Sorteador de Números (1 a 60) 🎲"
*   **Descrição:** Breve explicação do aplicativo.
*   **Seletor Múltiplo:** Para escolher os números de 1 a 60.
*   **Botões:**
    *   "✨ Sortear um número!"
    *   "🔄 Reiniciar Sorteio"
*   **Exibição do Resultado:** Mensagem de sucesso com o número sorteado.
*   **Informações Adicionais:**
    *   Lista dos números selecionados pelo usuário.
    *   Lista dos números já sorteados na sessão atual.

---

Desenvolvido com Streamlit. Divirta-se sorteando!