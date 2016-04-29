import java.util.*;

import java.util.Collections;

public class tester {
	public static void main(String[] args) {
		class HiRiQ	{
			//int is used to reduce storage to a minimum...
			public int config;
			public byte weight;

			//initialize to one of 5 reachable START config n=0,1,2,3,4
			HiRiQ(byte n){
				if (n==0)
				{config=65536/2;weight=1;}
				else
					if (n==1)
					{config=1626;weight=6;}
					else
						if (n==2)
						{config=-1140868948; weight=10;}
						else
							if (n==3)
							{config=-411153748; weight=13;}
							else
							{config=-2147450879; weight=32;}
			}

			boolean IsSolved(){
				return( (config==65536/2) && (weight==1) );
			}

			//transforms the array of 33 booleans to an (int) config and a (byte) weight.
			public void store(boolean[] B){
				int a=1;
				config=0;
				weight=(byte) 0;
				if (B[0]) {weight++;}
				for (int i=1; i<32; i++){
					if (B[i]) {config=config+a;weight++;}
					a=2*a;
				}
				if (B[32]) {config=-config;weight++;}
			}

			//transform the int representation to an array of booleans.
			//the weight (byte) is necessary because only 32 bits are memorized
			//and so the 33rd is decided based on the fact that the config has the
			//correct weight or not.
			public boolean[] load(boolean[] B){
				byte count=0;
				int fig=config;
				B[32]=fig<0;
				if (B[32]) {fig=-fig;count++;}
				int a=2;
				for (int i=1; i<32; i++){
					B[i]= fig%a>0;
					if (B[i]) {fig=fig-a/2;count++;}
					a=2*a;
				}
				B[0]= count<weight;
				return(B);
			}

			//prints the int representation to an array of booleans.
			//the weight (byte) is necessary because only 32 bits are memorized
			//and so the 33rd is decided based on the fact that the config has the
			//correct weight or not.
			public void printB(boolean Z){if (Z) {System.out.print("[ ]");} else {System.out.print("[@]");}}

			public void print(){
				byte count=0;
				int fig=config;
				boolean next,last=fig<0;
				if (last) {fig=-fig;count++;}
				int a=2;
				for (int i=1; i<32; i++){
					next= fig%a>0;
					if (next) {fig=fig-a/2;count++;}
					a=2*a;
				}
				next= count<weight;

				count=0;
				fig=config;
				if (last) {fig=-fig;count++;}
				a=2;

				System.out.print("      ") ;
				printB(next);
				for (int i=1; i<32; i++){
					next= fig%a>0;
					if (next) {fig=fig-a/2;count++;}
					a=2*a;
					printB(next);
					if (i==2 || i==5 || i==12 || i==19 || i==26 || i==29) {System.out.println() ;}
					if (i==2 || i==26 || i==29) {System.out.print("      ") ;};
				}
				printB(last); System.out.println() ;
			}
			////////////////////////////////////////////
			//////-------------my code-----------///////
			////////////////////////////////////////////

			class Node{
				//int weight;
				private HiRiQ config;			
				private Node parent;
				private ArrayList<Node> children= new ArrayList<Node>();
				private String moves="";
				private boolean[] puzzle= new boolean[33];

				public Node(HiRiQ config){
					this.config = config;
					this.parent = parent;
					this.children = children;
					this.moves= moves;
					this.puzzle= config.load(puzzle);
				}
				public HiRiQ getConfig(){
					return this.config;
				}
				/*public ArrayList<Node> getChildren(){
					return this.children;
				}*/
				public String getMoves(){
					return this.moves;
				}
				public String newMove(int[] triplet){
					String move=""+triplet[0]+"@"+triplet[2]+" ";
					return move;
				}
				public void addToChildrenList(Node child, int[] triplet){
					child.parent= this;
					child.moves = this.moves+" --> "+this.newMove(triplet);
					this.children.add(child);
				}
			}
			int[][] triplets= new int[][]{
				{0, 1, 2},
				{3, 4, 5},
				{6, 7, 8},
				{7, 8, 9},
				{8, 9, 10},
				{9, 10, 11},
				{10, 11, 12},

				{13, 14, 15},
				{14, 15, 16},
				{15, 16, 17},
				{16, 17, 18},
				{17, 18, 19},

				{20, 21, 22},
				{21, 22, 23},
				{22, 23, 24},
				{23, 24, 25},
				{24, 25, 26},

				{27, 28, 29},
				{30, 31, 32},

				{12, 19, 26},
				{11, 18, 25},

				{2, 5, 10},
				{5, 10, 17},
				{10, 17, 24},
				{17, 24, 29},
				{24, 29, 32},

				{1, 4 ,9},
				{4, 9, 16},
				{9, 16, 23},
				{16, 23, 28},
				{23, 28, 31},

				{0, 3, 8},
				{3, 8, 15},
				{8, 15, 22},
				{15, 22, 27},
				{22, 27, 30},

				{7, 14, 21},
				{6, 13, 20},
			};
			ArrayList<boolean[]> visitedConfig = new ArrayList<boolean[]>();
			
			public String findSolution(boolean [] config){
				ArrayList<Node> priorityList = new ArrayList<Node>();
				ArrayList<Node> secondList = new ArrayList<Node>();
				ArrayList<Node> queue = new ArrayList<Node>();

				//transform Root boolean into Node
				HiRiQ temp=new HiRiQ((byte)0);
				temp.store(config);
				Node root= new Node(temp); //since root, start with no parent and no children

				//tree/graph data structure of configuration of the puzzle
				visitedConfig.add(config);
				queue.add(root);
				if(queue.get(0).getConfig().IsSolved()==true) return queue.get(0).getMoves();
				while(secondList.size()>0 || queue.size()>0){
					while(queue.size()>0){
						//pop the parent off the queue
						boolean B[]= new boolean[33];
						queue.get(0).getConfig().load(B);
						//queue.remove(0).getConfig().load(B);
						boolean[] child= new boolean[33];
						for(int u=0; u<38; u++){
							if(validTriplet(B, triplets[u])!=null){
								boolean []newTriplet = validTriplet(B, triplets[u]);
								child=configAfterMove(B, newTriplet, triplets[u]);
								if(existConfig(child)==false && parityTest(child)==true){
									//add the node
									HiRiQ temp1= new HiRiQ((byte)0);
									temp1.store(child);
									Node oneChild= new Node(temp1);
									queue.get(0).addToChildrenList(oneChild, triplets[u]);
									if(temp1.IsSolved()==true){
										return oneChild.getMoves();
									}
									visitedConfig.add(child);
									//add the move to the node
									if(nbrBlack(B)<=nbrBlack(child) && priorityList.size()<50000){
										priorityList.add(oneChild);
									}
									if(nbrBlack(B)>nbrBlack(child)&&secondList.size()<500000){//store in second later list
										secondList.add(oneChild);
									}
								}
							}
						}
						queue.addAll(priorityList);
						priorityList.clear();
						queue.remove(0);
					}
					while(secondList.size()>0 && queue.size()==0){
						for(int i=0; i<secondList.size(); i++){
							queue.add(secondList.get(i));
						}
					}
				}
				return "@";
			}
			//check if visited a configuration
			public boolean existConfig(boolean[] config){
				boolean result=false;
				for(int i=0; i<visitedConfig.size(); i++){
					if(Arrays.equals(visitedConfig.get(i), config)){ //if exist inside visitedConfig
						result=true;
					}
				}

				return result;
			}

			//Input a triplet array of 3 boolean values and return it back if no substitution found or return the newly created substitution.
			public boolean[] validTriplet(boolean[] config, int[] tripletIndex){
				int x=tripletIndex[0];
				int y=tripletIndex[1];
				int z=tripletIndex[2];
				boolean result[]=new boolean[3];
				if(config[x]==true && config[y]==false && config[z]==false){
					result[0]=false;
					result[1]=true;
					result[2]=true;
				}
				else if(config[x]==true && config[y]==true && config[z]==false){
					result[0]=false;
					result[1]=false;
					result[2]=true;
				}
				else if(config[x]==false && config[y]==true && config[z]==true){
					result[0]=true;
					result[1]=false;
					result[2]=false;
				}
				else if(config[x]==false && config[y]==false && config[z]==true){
					result[0]=true;
					result[1]=true;
					result[2]=false;
				}
				else{
					result=null;
				}
				return result;
			}
			public boolean[] configAfterMove(boolean[] config, boolean[] newTriplet, int[] tripletIndex){
				boolean[] newConfig= new boolean[33];
				for(int i=0; i<33; i++){
					newConfig[i]=config[i];
				}
				int x=tripletIndex[0];
				int y=tripletIndex[1];
				int z=tripletIndex[2];
				newConfig[x]=newTriplet[0];
				newConfig[y]=newTriplet[1];
				newConfig[z]=newTriplet[2];
				return newConfig;
			}
			public int nbrBlack(boolean[] config){
				int result=0;
				for(int i=0; i<33; i++){
					if(config[i]==false){
						result++;
					}
				}
				return result;
			}
			public boolean parityTest(boolean[] config){
				boolean parity;
				int b=0;
				int y=0;
				int r=0;
				for(int i=0; i<33; i++){
					if(config[i] && (i==0||i==5||i==6||i==9||i==12||i==15||i==18||i==21||i==24||i==28||i==30)){
						b++;
					}
					if(config[i] && (i==1||i==3||i==7||i==10||i==13||i==16||i==19||i==22||i==25||i==29||i==31)){
						y++;
					}
					else if(config[i] && (i==2||i==4||i==8||i==11||i==14||i==17||i==20||i==23||i==26||i==27||i==32)){
						r++;
					}
				}
				parity=(b%2==r%2 && b%2 !=y%2);
				return parity;
			}
		}
		boolean[] B= {false, false, false, false, true, false, true, false, false, false, false, false, false, true, false, true, true, false, true, true, false, false, false, true, false, false, false, false, true, false, false, false, false};
		HiRiQ U=new HiRiQ((byte) 0) ;
		U.store(B);
		System.out.println((new HiRiQ((byte) 0)).findSolution(B));

		/*HiRiQ W=new HiRiQ((byte) 0) ;
		W.print(); System.out.println(W.IsSolved());
		HiRiQ X=new HiRiQ((byte) 1) ;
		X.print(); System.out.println(X.IsSolved());
		HiRiQ Y=new HiRiQ((byte) 2) ;
		Y.print(); System.out.println(Y.IsSolved());
		HiRiQ Z=new HiRiQ((byte) 3) ;
		Z.print(); System.out.println(Z.IsSolved());
		HiRiQ V=new HiRiQ((byte) 4) ;
		V.print(); System.out.println(V.IsSolved());*/
	}
}
