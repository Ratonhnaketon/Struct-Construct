package PEF;

/* Descobri a matriz de adjacencia do grafo,
 * 
 * Em cada nó, criar um vetor "linhaxcoluna" = 
 * 							   = 2x"numero de forcas == numero de nos adjacentes"
 * 
 * Sendo que:
 * -> a primeira linha == Px;
 * -> a segunda linha == Py.
 * 
 * Multiplicar cada linha desta forma (exemplo)
 *    (utilizando o eixo x como referencia)
 * 
 * (Px) -> | cos(180+ a)   cos(180+ b)   cos(180+ c)   cos(180+ d) |
 * (Py) -> | cos(90 + a)   cos(90 + b)   cos(90 + c)   cos(90 + d) |
 * 
 * Sendo que {a,b,c,d} sao os angulos das respectivas forcas [F12, F13, F23, F34] SEMPRE NESTA ORDEM.
 * Para descobrir se elas existem no nó, pegue a coluna, ou linha, da matriz de adjacencia. 
 * 
 * Junto dos nos, tambem é necessario saber se ele possui alguma restricao e que restricao
 * ela é. Por exemplo, em uma ponte que possui restricoes dos dois lados da ponte nos nós 1 e 4
 *  
 *  No nó 1
 *           <- |Rx1|
 * |1 0 0 0| <- |Ry1| 
 * |0 1 0 0| <- |Rx4| 
 *           <- |Ry4| 
 *
 * No nó 4
 *           <- |Rx1|
 * |0 0 1 0| <- |Ry1| 
 * |0 0 0 1| <- |Rx4| 
 *           <- |Ry4| 
 *         
 * Os outros nos terao uma MATRIZ ZERADA
 *   
 *           
 * E só falta, descobrir qual nó posssue peso e se este esta no eixo x ou no eixo y
 *
 *******************************************************************************************************
 *
 * Depois disso tudo, junte as matrizes em uma matriz grande 2nx2n, sendo que  
 * se deva arranjar a matriz dessa forma:
 * 
 * | matriz forcas nó'1' : matriz de restricao nó'1' |
 * | matriz forcas nó'2' : matriz de restricao nó'2' |
 * | matriz forcas nó'3' : matriz de restricao nó'3' | = M
 * | ..................  : ........................  |
 * | matriz forcas nó'n' : matriz de restricao nó'n' |
 * 
 * 
 * Depois, faca a inversa de M e multiplique pelos pesos (x e y) de cada nó para descobrir as forcas. Exemplo
 * 
 * |F1.| 			  |Px1|
 * |F2.|			  |Py1|
 * |F3.|		  	  |Px2|
 * |F4.| =  M⁻¹   *   |Py2|
 * |Rx1|			  |Px3|
 * |Ry1|			  |Py3|
 * |Rx4|			  |Px4|
 * |Ry4|			  |Py4|
 * 
 * E cabou =)
 * 
 * */

public class NOVO {
	
	double[] forca_em_X;
	double[] forca_em_Y;
	int numero_de_forcas; 
	double[] angulos;
	
	boolean restricao;
	int numero_de_restricoes; 
	int local_da_restricao;
	
	double[] R_em_X;
	double[] R_em_Y;
	
	boolean peso;
	double peso_em_X;
	double peso_em_Y;
	
	
	
	// Todo nó no solo tera um
	
	public NOVO(double[] forcas, int numero_de_forcas, double[] angulos,
				boolean restricao, int numero_de_restricoes, int local_da_restricao,
				boolean peso, double peso_em_X, double peso_em_Y){
		
		this.numero_de_forcas = numero_de_forcas;
		this.numero_de_restricoes = numero_de_restricoes;
		
		for(int i = 0; i < numero_de_forcas; i++){
			this.forca_em_X[i] = -forcas[i]*Math.cos(angulos[i]);
			this.forca_em_Y[i] = -forcas[i]*Math.sin(angulos[i]);
		}
		// Caso tenha alguma restricao
		
		this.restricao = restricao;
		if(this.restricao == true){// No Java, a matriz ja se inicializa zerada
			this.R_em_X = new double[numero_de_restricoes];
			this.R_em_Y = new double[numero_de_restricoes];
			this.R_em_X[local_da_restricao] = 1;
			this.R_em_Y[local_da_restricao+1] = 1;
		}
		else{// No Java, a matriz ja se inicializa zerada
			this.R_em_X = new double[numero_de_restricoes]; 
			this.R_em_Y = new double[numero_de_restricoes];
		}
		
		// Caso tenha alguma forca aplicada
		this.peso = peso;
		if(this.peso == true){
			this.peso_em_X = peso_em_X; 
			this.peso_em_Y = peso_em_Y;
		}
		else{
			this.peso_em_X = 0.0; 
			this.peso_em_Y = 0.0;
		}
	}
	
	double[] fazedora_de_resultados(){
		// nao sei se esta certo
		double[][] matriz= new double[this.numero_de_forcas+ this.numero_de_restricoes][this.numero_de_forcas+ this.numero_de_restricoes];
		
		// qualquer coisa da um printf aqui -_> System.out.println("Num. de Linhas:"+ matriz.length +"\n Num. de Colunas:"+matriz[0].length);
		//
		// Agora, tem que fazer isso daqui
		//
		// * 
		// * | matriz forcas nó'1' : matriz de restricao nó'1' |
		// * | matriz forcas nó'2' : matriz de restricao nó'2' |
		// * | matriz forcas nó'3' : matriz de restricao nó'3' | = M
		// * | ..................  : ........................  |
		// * | matriz forcas nó'n' : matriz de restricao nó'n' |
		// * 
		double[] vetor_final = new double[this.numero_de_forcas+ this.numero_de_restricoes];
		// * |F1.| 			  |Px1|
		// * |F2.|			  |Py1|
		// * |F3.|		  	  |Px2|
		// * |F4.| =  M⁻¹  *  |Py2|
		// * |Rx1|			  |Px3|
		// * |Ry1|			  |Py3|
		// * |Rx4|			  |Px4|
		// * |Ry4|			  |Py4|
		// * 
		
		
		
		return vetor_final;
	}
	
}
