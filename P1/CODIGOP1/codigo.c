#include <stdio.h>


void quickSort(int *vetor, int inicio,int fim)
{
    int pivo;
    if (fim > inicio)
    {
        pivo = criaParticoes(vetor, inicio, fim);
        quickSort(vetor, inicio, pivo - 1);
        quickSort(vetor, pivo+1, fim);
    }
}

void swap(int *v1, int *v2)
{
    int temp = *v1;
    *v1 = *v2;
    *v2 = temp;
}

int criaParticoes(int *vetor, int inicio, int fim)
{

    int esquerda = inicio;
    int direita = fim;
    int pivo = vetor[inicio];

    while (esquerda < direita)
    {
        while (vetor[esquerda] <= pivo && esquerda <= fim)
        {
            esquerda++;
        }
        while (vetor[direita] > pivo && direita >= inicio)
        {
            direita--;
        }
        if (esquerda < direita)
        {
            swap(&vetor[esquerda], &vetor[direita]);
        }
    }
        swap(&vetor[inicio], &vetor[direita]);
    return direita;
}

int main(int argc, char const *argv[])
{
  //teste
  
  int vetor1[] = {9,8,4,6,5,7,3,2,1};
  quickSort(vetor1, 0, sizeof(&vetor1));

    for(int i = 0; i <= sizeof(&vetor1); i++) {
    printf("%d ", vetor1[i]);
  }printf("\n");
  
  
    return 0;
}
