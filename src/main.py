from api_service import get_motivational_quote
from task_manager import add_task, list_tasks, complete_task, remove_task



def show_menu():
    print("\n=== ORGANIZADOR DE ESTUDOS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def main():
    quote = get_motivational_quote()

    print("\n💡 Frase do dia:")
    print(f'"{quote["content"]}"')
    print(f'- {quote["author"]}\n')

    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        try:
            if option == "1":
                title = input("Digite a tarefa: ")
                add_task(title)
                print("Tarefa adicionada!")

            elif option == "2":
                tasks = list_tasks()
                if not tasks:
                    print("Nenhuma tarefa cadastrada.")
                for i, task in enumerate(tasks):
                    status = "✓" if task["done"] else "X"
                    print(f"{i} - [{status}] {task['title']}")

            elif option == "3":
                index = int(input("Número da tarefa: "))
                complete_task(index)
                print("Tarefa concluída!")

            elif option == "4":
                index = int(input("Número da tarefa: "))
                remove_task(index)
                print("Tarefa removida!")

            elif option == "0":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except Exception as error:
            print(f"Erro: {error}")

if __name__ == "__main__":
    main()
