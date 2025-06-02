import streamlit as st
import random

# --- Configurações da Página (Opcional, mas melhora a aparência) ---
st.set_page_config(
    page_title="Sorteador de Números",
    page_icon="🎰",
    layout="centered" # "centered" ou "wide"
)

# --- Título e Descrição ---
st.title("🎰 Sorteador de Números (1 a 60) 🎲")

st.write(
    """
    Bem-vindo ao seu aplicativo de sorteio!
    Selecione os números que você deseja incluir no sorteio.
    O aplicativo escolherá um número aleatoriamente dentre os selecionados,
    e não repetirá números já sorteados nesta sessão (para a seleção atual).
    """
)

# --- Inicializar o estado da sessão ---
# 'drawn_numbers' guardará os números já sorteados para a seleção atual
if 'drawn_numbers' not in st.session_state:
    st.session_state.drawn_numbers = []
# 'last_selected_numbers_hash' para detectar mudanças no multiselect
if 'last_selected_numbers_hash' not in st.session_state:
    st.session_state.last_selected_numbers_hash = None

# --- 1. Definir o range de números disponíveis ---
all_possible_numbers = list(range(1, 61))

# --- 2. Input para o usuário selecionar os números ---
selected_numbers = st.multiselect(
    "Selecione os números disponíveis para o sorteio:",
    options=all_possible_numbers,
    default=[],
    placeholder="Escolha seus números aqui...",
    help="Você pode escolher quantos números quiser de 1 a 60."
)

# Verificar se a seleção de números mudou. Se sim, resetar os sorteados.
# Usamos hash para uma comparação eficiente e independente da ordem.
current_selection_hash = hash(tuple(sorted(selected_numbers))) # Garante que a ordem não importa

if current_selection_hash != st.session_state.last_selected_numbers_hash:
    st.session_state.drawn_numbers = [] # Reseta os números sorteados
    st.session_state.last_selected_numbers_hash = current_selection_hash
    if selected_numbers: # Apenas informa se a mudança não foi para uma lista vazia
        st.info("Sua seleção de números mudou. O histórico de sorteios foi reiniciado para esta nova seleção.")


# --- Colunas para botões ---
col1, col2 = st.columns(2)

# --- 3. Botão para iniciar o sorteio ---
with col1:
    if st.button("✨ Sortear um número!", use_container_width=True):
        if not selected_numbers:
            st.warning("🚨 Por favor, selecione pelo menos um número para realizar o sorteio.")
        else:
            # Números disponíveis para sorteio (selecionados MENOS os já sorteados)
            available_to_draw = [num for num in selected_numbers if num not in st.session_state.drawn_numbers]

            if not available_to_draw:
                st.info("🎉 Todos os números selecionados já foram sorteados! 🎉")
                st.balloons()
            else:
                winning_number = random.choice(available_to_draw)
                st.session_state.drawn_numbers.append(winning_number) # Adiciona ao histórico da sessão

                st.success(f"🎉 O número sorteado é: **{winning_number}** 🎉")
                st.balloons()

# --- Botão para Reiniciar o Sorteio (limpar `drawn_numbers`) ---
with col2:
    if st.button("🔄 Reiniciar Sorteio", help="Limpa os números já sorteados para a seleção atual.", use_container_width=True):
        if not selected_numbers:
            st.warning("🚨 Selecione números primeiro para poder reiniciar o sorteio deles.")
        elif not st.session_state.drawn_numbers:
            st.info("ℹ️ Nenhum número foi sorteado ainda para esta seleção.")
        else:
            st.session_state.drawn_numbers = []
            st.success("✅ Histórico de sorteios limpo! Pode sortear novamente com os mesmos números selecionados.")
            st.rerun() # Força o rerender para atualizar a exibição

# --- Exibir informações adicionais ---
if selected_numbers:
    st.info(f"Você selecionou os seguintes números para o sorteio: {sorted(selected_numbers)}")

if st.session_state.drawn_numbers:
    st.write("---")
    st.subheader("Números já sorteados nesta sessão:")
    # Exibir em colunas para melhor visualização se houver muitos números
    num_cols = 5
    cols = st.columns(num_cols)
    sorted_drawn = sorted(st.session_state.drawn_numbers)
    for i, number in enumerate(sorted_drawn):
        cols[i % num_cols].markdown(f"<div style='text-align: center; padding: 5px; margin: 2px; border: 1px solid #4CAF50; border-radius: 5px; background-color: #e8f5e9;'>{number}</div>", unsafe_allow_html=True)
    st.write(f"Total sorteados: {len(st.session_state.drawn_numbers)} de {len(selected_numbers)} selecionados.")


# --- Rodapé ---
st.markdown("---")
st.write("Desenvolvido por Cristian Ferreira Carlos, cristiancarlos@vibraenergia.com.br")