import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

import org.jgrapht.alg.flow.PushRelabelMFImpl;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.SimpleDirectedWeightedGraph;

public class Round1A_B {
	
	static int[] splitToInts(String s) {
		return Arrays.stream(s.split("\\s")).mapToInt(Integer::parseInt).toArray();
	}
	
	static long[] splitToLongs(String s) {
		return Arrays.stream(s.split("\\s")).mapToLong(Long::parseLong).toArray();
	}
	
	static class Pack {
		int r;
		int amount;
		int min; //min servable persons
		int max; //max servable persons
		
		public Pack(int r, int amount) {
			this.r = r;
			this.amount = amount;
			/*
			 * NOTE: (int)(Math.floor(amount/(r*0.9))) is wrong due to float inaccuracy.
			 * For example, r=3 amount=1350 10*amount/(r*9.0) is 500.0 but amount/(r*0.9) is 499.99999...
			 * 
			 * 10*amount/r*9 is also wrong
			 */
			max = (int)(Math.floor(10*amount/(r*9.0)));
			min = (int)(Math.ceil(10*amount/(r*11.0)));
			if(max < min) {
				min = max = 0;
			}

		}
	}
	
	static double solve(int N, int P, int[] R, int[][] ps) {
		SimpleDirectedWeightedGraph<Pack, DefaultWeightedEdge> g = new SimpleDirectedWeightedGraph<>(DefaultWeightedEdge.class);
		Pack[][] packs = new Pack[N][P];
		for(int i=0; i<N; i++) {
			for(int j=0; j<P; j++) {
				packs[i][j] = new Pack(R[i], ps[i][j]);
			}
		}
		Pack src = new Pack(1,1);
		Pack dest = new Pack(1,1);
		g.addVertex(src);
		g.addVertex(dest);
		for(int j=0; j<P; j++) {
			Pack pack = packs[0][j];
			if(pack.max == 0) continue;
			g.addVertex(pack);
			DefaultWeightedEdge edge = g.addEdge(src, pack);
			g.setEdgeWeight(edge, 1.0);
		}
		for(int i=1; i<N; i++) {
			for(int j=0; j<P; j++) {
				Pack to = packs[i][j];
				if(to.max == 0) continue;
				g.addVertex(to);
				for(int k=0; k<P; k++) {
					Pack from = packs[i-1][k];
					if(from.max == 0) continue;
					if(!(from.max < to.min || to.max < from.min)) {
						DefaultWeightedEdge edge = g.addEdge(from, to);
						g.setEdgeWeight(edge, 1.0);
					}
				}
			}
		}
		for(int j=0; j<P; j++) {
			Pack pack = packs[N-1][j];
			if(pack.max == 0) continue;
			g.addVertex(pack);
			DefaultWeightedEdge edge = g.addEdge(pack, dest);
			g.setEdgeWeight(edge, 1.0);
		}
		
		PushRelabelMFImpl<Pack, DefaultWeightedEdge> flow = new PushRelabelMFImpl<>(g);
		double ret = flow.calculateMaximumFlow(src, dest);
		return ret;
	}

	public static void main(String[] args) throws IOException{
		BufferedReader input = new BufferedReader(new FileReader(args[0]));
		FileWriter output = new FileWriter(args[0].substring(0, args[0].length()-2)+"out");
		final int tn = Integer.parseInt(input.readLine());
		
		for(int t=1; t<= tn; t++) {
			int[] tmp = splitToInts(input.readLine());
			int N = tmp[0];
			int P = tmp[1];
			int[] R = splitToInts(input.readLine());
			int[][] ps = new int[N][];
			for(int i=0; i<N; i++) {
				ps[i] = splitToInts(input.readLine());
			}
			Integer ret = (int)Math.round(solve(N, P, R, ps));
			System.out.println(String.format("Case #%d: %s", t, ret.toString()));
			output.write(String.format("Case #%d: %s\n", t, ret.toString()));
		}
		
		input.close();
		output.close();
	}

}
