import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

import org.jgrapht.GraphPath;
import org.jgrapht.alg.shortestpath.FloydWarshallShortestPaths;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.SimpleDirectedWeightedGraph;

public class Round1B_Clarge {
	
	static int[] splitToInts(String s) {
		return Arrays.stream(s.split("\\s")).mapToInt(Integer::parseInt).toArray();
	}
	
	static long[] splitToLongs(String s) {
		return Arrays.stream(s.split("\\s")).mapToLong(Long::parseLong).toArray();
	}
	
	public static String solve(int N, int Q, int[] E, int[] S, int[][] D, int[] U, int[] V)
	{
		SimpleDirectedWeightedGraph<Integer, DefaultWeightedEdge> originG = new SimpleDirectedWeightedGraph<>(DefaultWeightedEdge.class);
		SimpleDirectedWeightedGraph<Integer, DefaultWeightedEdge> timeG = new SimpleDirectedWeightedGraph<>(DefaultWeightedEdge.class);
		
		for(int i=0; i<N; i++) {
			originG.addVertex(i);
			timeG.addVertex(i);
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(D[i][j] > 0) {
					DefaultWeightedEdge e = originG.addEdge(i, j);
					originG.setEdgeWeight(e, D[i][j]);
				}
			}
		}
		
		//build the timeG
		FloydWarshallShortestPaths<Integer, DefaultWeightedEdge> sp = new FloydWarshallShortestPaths<>(originG);
		for(int src=0; src<N; src++) {
			for(int dest=0; dest<N; dest++) {
				if(src == dest) continue;
				GraphPath<Integer, DefaultWeightedEdge> path = sp.getPath(src, dest);
				if(path != null) {
					double w = path.getWeight();
					if(w <= E[src]) {
						DefaultWeightedEdge e = timeG.addEdge(src, dest);
						timeG.setEdgeWeight(e, w/S[src]);
					}
				}
			}
		}
		
		//query
		FloydWarshallShortestPaths<Integer, DefaultWeightedEdge> query = new FloydWarshallShortestPaths<>(timeG);
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<Q; i++) {
			double w = query.getPathWeight(U[i], V[i]);
			sb.append(w);
			if(i != Q-1) sb.append(" ");
		}
		return sb.toString();
	}

	public static void main(String[] args) throws IOException{
		BufferedReader input = new BufferedReader(new FileReader(args[0]));
		FileWriter output = new FileWriter(args[0].substring(0, args[0].length()-2)+"out");
		final int tn = Integer.parseInt(input.readLine());
		
		for(int t=1; t<= tn; t++) {
			int[] tmp = splitToInts(input.readLine());
			int N = tmp[0];
			int Q = tmp[1];
			int[] E = new int[N];
			int[] S = new int[N];
			for(int i=0; i<N; i++) {
				tmp = splitToInts(input.readLine());
				E[i] = tmp[0];
				S[i] = tmp[1];
			}
			int[][] D = new int[N][];
			for(int i=0; i<N; i++) {
				D[i] = splitToInts(input.readLine());
			}
			int[] U = new int[Q];
			int[] V = new int[Q];
			for(int i=0; i<Q; i++) {
				tmp = splitToInts(input.readLine());
				U[i] = tmp[0] - 1;
				V[i] = tmp[1] - 1;
			}
			String result = solve(N,Q,E,S,D,U,V);
			System.out.println(String.format("Case #%d: %s", t, result));
			output.write(String.format("Case #%d: %s\n", t, result));
		}
		
		input.close();
		output.close();
	}

}
