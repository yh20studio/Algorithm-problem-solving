/* 
    link : https://www.acmicpc.net/problem/1504
    Lv : gold 4
    Category : 다익스트라
    
    각 경로의 가중치가 있는 상태에서 최단경로를 구하는 문제이기 때문에 다익스트라 알고리즘을 활용했다.
    여기서 특이한 점은 꼭 거쳐야 할 노드가 2개가 있다는 것이다.
    이를 구현하기 위해서 시작노드부터 종료 노드까지 가는 경로 중간에 거쳐야 할 노드를 포함시키면서
    경로를 2개를 구현하고 서로 비교하여 최솟값을 출력하도록 했다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Edge {
	public int next;
	public int distance;

	public Edge(int next, int distance) {
		this.next = next;
		this.distance = distance;
	}
}

class Route implements Comparable<Route> {
	public int location;
	public int distanceSum;

	public Route(int location, int distanceSum) {
		this.location = location;
		this.distanceSum = distanceSum;
	}

	@Override
	public int compareTo(Route route) {
		return distanceSum - route.distanceSum;
	}

}

public class Main {
	private static final int INF = 1000 * 200000;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] sizeArray = bf.readLine().split(" ");
		int nodeSize = Integer.parseInt(sizeArray[0]);
		int edgeSize = Integer.parseInt(sizeArray[1]);
		List<ArrayList<Edge>> graph = new ArrayList<>();
		for (int i = 0; i <= nodeSize; i++) {
			graph.add(new ArrayList<>());
		}
		for (int i = 0; i < edgeSize; i++) {
			String[] edgeArray = bf.readLine().split(" ");
			int start = Integer.parseInt(edgeArray[0]);
			int end = Integer.parseInt(edgeArray[1]);
			int distance = Integer.parseInt(edgeArray[2]);
			graph.get(start).add(new Edge(end, distance));
			graph.get(end).add(new Edge(start, distance));
		}
		int[] haveToIncludeNodes = new int[2];
		String[] haveToIncludeNodeArray = bf.readLine().split(" ");
		haveToIncludeNodes[0] = Integer.parseInt(haveToIncludeNodeArray[0]);
		haveToIncludeNodes[1] = Integer.parseInt(haveToIncludeNodeArray[1]);

		findRoute(haveToIncludeNodes, nodeSize, graph);

	}

	private static void findRoute(int[] haveToIncludeNodes, int nodeSize, List<ArrayList<Edge>> graph) {
		int firstRoute = 0;
		int secondRoute = 0;
		// 0 -> v1 -> v2 -> N
		firstRoute += dijkstra(1, haveToIncludeNodes[0], nodeSize, graph);
		firstRoute += dijkstra(haveToIncludeNodes[0], haveToIncludeNodes[1], nodeSize, graph);
		firstRoute += dijkstra(haveToIncludeNodes[1], nodeSize, nodeSize, graph);
		// 0 -> v2 -> v1 -> N
		secondRoute += dijkstra(1, haveToIncludeNodes[1], nodeSize, graph);
		secondRoute += dijkstra(haveToIncludeNodes[1], haveToIncludeNodes[0], nodeSize, graph);
		secondRoute += dijkstra(haveToIncludeNodes[0], nodeSize, nodeSize, graph);

		if (firstRoute >= INF && secondRoute >= INF) {
			System.out.println(-1);
			return;
		}
		System.out.println(Math.min(firstRoute, secondRoute));
	}

	private static int dijkstra(int start, int end, int nodeSize, List<ArrayList<Edge>> graph) {
		PriorityQueue<Route> queue = new PriorityQueue<Route>();
		int[] distanceArray = new int[nodeSize + 1];
		for (int i = 0; i <= nodeSize; i++) {
			distanceArray[i] = INF;
		}
		queue.add(new Route(start, 0));
		distanceArray[start] = 0;

		while (!queue.isEmpty()) {
			Route route = queue.poll();
			for (Edge each : graph.get(route.location)) {
				if (distanceArray[each.next] > distanceArray[route.location] + each.distance) {
					distanceArray[each.next] = distanceArray[route.location] + each.distance;
					queue.add(new Route(each.next, distanceArray[each.next]));
				}
			}
		}
		return distanceArray[end];
	}
}