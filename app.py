import streamlit as st

from src.api_service import get_motivational_quote
from src.task_manager import add_task, complete_task, list_tasks, remove_task


st.set_page_config(
    page_title="Organizador de Tarefas",
    page_icon="📋",
    layout="centered",
)

st.title("📋 Organizador de Tarefas")
st.write("Aplicação para organizar tarefas com integração a uma API pública.")

quote = get_motivational_quote()

st.info(f'💡 "{quote["content"]}"\n\n— {quote["author"]}')

st.divider()

st.subheader("➕ Adicionar tarefa")

new_task = st.text_input("Digite uma nova tarefa:")

if st.button("Adicionar"):
    if new_task.strip():
        add_task(new_task)
        st.success("Tarefa adicionada com sucesso!")
        st.rerun()
    else:
        st.warning("Digite uma tarefa válida.")

st.divider()

st.subheader("📋 Lista de tarefas")

tasks = list_tasks()

if not tasks:
    st.write("Nenhuma tarefa cadastrada.")
else:
    for index, task in enumerate(tasks):
        col1, col2, col3 = st.columns([4, 1, 1])

        status = "✅" if task["done"] else "⬜"

        with col1:
            st.write(f'{status} {task["title"]}')

        with col2:
            if not task["done"]:
                if st.button("Concluir", key=f"complete_{index}"):
                    complete_task(index)
                    st.rerun()

        with col3:
            if st.button("Remover", key=f"remove_{index}"):
                remove_task(index)
                st.rerun()