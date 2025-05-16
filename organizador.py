import time
from estrutura_lista import LinkedList, Node
from merge_sort import merge_sort_linked_list
from radix_sort_negativos import radix_sort_linked_list_negativos

def separar_lista(head):
    negativos = LinkedList()
    positivos = LinkedList()
    current = head
    while current:
        if current.data < 0:
            negativos.insert_end(current.data)
        else:
            positivos.insert_end(current.data)
        current = current.next
    return negativos, positivos

def concatenar_listas(lista1, lista2):
    if lista1.is_empty():
        return lista2.head
    current = lista1.head
    while current.next:
        current = current.next
    current.next = lista2.head
    return lista1.head

def main():
    dados = [-7, 23, -1, 0, 3, -99, 45, 12]
    lista_original = LinkedList()
    for num in dados:
        lista_original.insert_end(num)

    negativos, positivos = separar_lista(lista_original.head)

    start_radix = time.time()
    negativos.head = radix_sort_linked_list_negativos(negativos.head)
    end_radix = time.time()


    start_merge = time.time()
    positivos.head = merge_sort_linked_list(positivos.head)
    end_merge = time.time()


    lista_final = LinkedList()
    lista_final.head = concatenar_listas(negativos, positivos)

    print("Lista negativa ordenada por Radix Sort:")
    negativos.print_list()

    print("\nLista positiva ordenada por Merge Sort:")
    positivos.print_list()

    print("\nLista final concatenada:")
    lista_final.print_list()

    print("\nComplexidade de Merge Sort: O(n log n)")
    print("Complexidade de Radix Sort: O(nk)")

    tempo_radix = (end_radix - start_radix) * 1000
    tempo_merge = (end_merge - start_merge) * 1000
    print(f"\nTempo de execução Radix Sort: {tempo_radix:.2f} ms")
    print(f"Tempo de execução Merge Sort: {tempo_merge:.2f} ms")

if __name__ == "__main__":
    main()
