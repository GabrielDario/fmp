#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h> 
using namespace std;

main(){
	
	setlocale(LC_ALL, "portuguese"); //usar acentua��o e portugues correto
//declarar a lista 
struct Lista{    //1 elem num prox  2 elem num prox  3 elem num prox  4 elem num prox
	int num; //conte�do ser� colocado na lista
	Lista *prox; // proximo //* - ponteiro - comando de alocacao dinamica de memoria 
	//	- fica com o endereco de memoria do espaco criado
};

//lista vazia, cria um ponteiro *inicio e aponta ele para Null - Fim

Lista *inicio = NULL;//lista vazia
Lista *fim = NULL;
Lista *aux;//aux - serve para trabalhar no meio da lista
Lista *ant;//anterior

int op,achou,numero;
//menu opcoes

do{
	system("cls");//limpa tela clear screen
	cout<<"\n Menu de op��es \n";//c comando out output saida  \n new line
	cout<<"\n 1 - Inserir inicio da lista: ";
	cout<<"\n 2 - Inserir fim da lista: ";
	cout<<"\n 3 - Consultar toda a lista: ";
	cout<<"\n 4 - Remover da lista: ";
	cout<<"\n 5 - Esvaziar a lista: ";
	cout<<"\n 6 - Sair do Sistema: ";
	cout<<"\n Digite a op��o: ";
	cin>>op;
	
if (op==1)	{
	
	cout<<"\n Digite o n�mero a ser inserido no inicio da lista: ";
	Lista *novo = new Lista();//Lista *novo - declaro ponteiro novo - 
	//new Lista()  - crio uma espaco de mem�ria tipo lista e aloco este pra novo
	cin>>novo->num; //c comando in input entrada
	if (inicio == NULL ){ //somente quando a lista vazia
		inicio=novo;
		fim=novo;
		fim->prox=NULL;
		cout<<"\n Primeiro Elemento inserido na lista ";
	}
	else{             //lista com elementos, inseri no inicio lista
	    novo->prox=inicio;
	    inicio=novo;
	    cout<<"\n Novo Elemento inserido no inicio da lista ";
		}
	    	cout<<"\n digite enter para voltar ao menu ";
    getch();
	    }//final da opcao 1
	    
if (op==2)	{
	
	cout<<"\n Digite o n�mero a ser inserido no final da lista: ";
	Lista *novo = new Lista();//Lista *novo - declaro ponteiro novo - 
	//new Lista()  - crio uma espaco de mem�ria tipo lista e aloco este pra novo
	cin>>novo->num;
	if (inicio == NULL ){ //somente qo lista vazia
		inicio=novo;
		fim=novo;
		fim->prox=NULL;
	}
	else{             //lista com elementos, inseri no inicio lista
	    fim->prox=novo;
	    fim=novo;
	    fim->prox=NULL;
	    cout<<"\n Novo Elemento inserido no final da lista ";
		}
	   	cout<<"\n digite enter para voltar ao menu ";
    getch(); 
	    }//final da opcao 2
		
if (op==3)	{
	
	if (inicio == NULL ){ //vefiricar se a lista esta vazia
	
		cout<<"\n Lista vazia ";
	}
	else{          
	    cout<<"\n Listando os elementos da Lista ";
	    aux=inicio;
	    while (aux != NULL){	//percorrer a lista endere�o por endere�o at� final lista
	    cout<<"\n "<<aux->num;
	    aux=aux->prox; //para percorrer elemento a elemento da lista
	     
		}
	    	    }
	cout<<"\n digite enter para voltar ao menu ";
    getch();	    	
}//final da opcao 3
	
if (op==4)	{
	
	if (inicio == NULL ){ //vefiricar se a lista esta vazia
	
		cout<<"\n Lista vazia ";
	}
	else{          
	    cout<<"\n Removendo elementos da Lista ";
	    cout<<"\n Digite o n�mero a ser removido da lista: ";
	    cin>>numero;
	    
	    aux=inicio;
	    ant=NULL;
	    achou=0;
	    
	    while (aux != NULL){	//percorrer a lista endere�o por endere�o at� final lista
	    if( aux->num == numero){
	    	achou++;
	     if(aux == inicio )	{ //remover no inicio da lista
	     	inicio=aux->prox;
	     	delete(aux);
	     	aux=inicio;
	     }
	     else{
		    if(aux == fim )	{ //remover no final da lista
	     	ant->prox=NULL;
	     	fim=ant;
	     	delete(aux);
	     	aux=NULL;}
	     	else{   //remover no meio da lista
	     	    ant->prox=aux->prox;
				delete(aux);
				aux=ant->prox; }   	
	     	 }
	     }
	     else{
	     	ant=aux;
	     	aux=aux->prox; }
	     	
	}
	     if(achou ==0 ) {
	     	cout<<"\n N�mero n�o encontrado ";}
		 else if (achou ==1){
		 	cout<<"\n N�mero removido uma Vez ";}
		 	else {
		 		cout<<"\n N�mero removido"<<achou<<"Vezes";}
		 		
		 	}
		 		
	cout<<"\n digite enter para voltar ao menu ";
    getch();	 	
		 }//final da op��o 4
		 
if (op==5)	{
	
	if (inicio == NULL ){ //vefiricar se a lista esta vazia
	
		cout<<"\n Lista vazia ";
	}
	else{          
	    aux=inicio;   
	    while (aux != NULL){	//percorrer a lista endere�o por endere�o at� final lista
	      inicio=inicio->prox;
	      delete(aux);
	      aux=inicio;}
	      
	      cout<<"\n Lista Esvaziada ";
	      cout<<"\n digite enter para voltar ao menu ";
		  getch();
	      
	    
		 }
	} //final da op��o 5
	
}
while(op != 6);
}
	     	
