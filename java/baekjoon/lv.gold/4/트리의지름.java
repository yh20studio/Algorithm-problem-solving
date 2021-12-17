/* 
    link : https://www.acmicpc.net/problem/1967
    Lv : gold 4
    Category : BFS
    
    루트 노드가 정해져 있는 트리에서 각 가중치를 이용한 트리의 최대 지름을 구하는 문제이다.
    우선 BFS를 통해서 루트 노드로부터 있는 가장 먼 노드를 찾는다.
    그 노드로 부터 다른 단일노드까지의 거리를 BFS를 통해서 탐색하여 최대 가중치의 합을 구했다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

class Point {
	int node;
	int distance;

	public Point(int node, int distance) {
		this.node = node;
		this.distance = distance;
	}
}

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int nodes = Integer.parseInt(bf.readLine());
		HashMap<Integer, ArrayList<int[]>> graph = new HashMap<>();
		for (int i = 0; i < nodes; i++) {
			graph.put(i + 1, new ArrayList());
		}
		for (int i = 0; i < nodes - 1; i++) {
			String[] edgeCases = bf.readLine().split(" ");
			int parentNode = Integer.parseInt(edgeCases[0]);
			int childNode = Integer.parseInt(edgeCases[1]);
			int weight = Integer.parseInt(edgeCases[2]);
			graph.get(parentNode).add(new int[] {childNode, weight});
			graph.get(childNode).add(new int[] {parentNode, weight});
		}
		if (nodes == 1) {
			System.out.println(0);
			return;
		}
		Point maxPointFromRoot = findMaxPoint(graph, 1, nodes);
		Point maxPointFromLeaf = findMaxPoint(graph, maxPointFromRoot.node, nodes);
		System.out.println(maxPointFromLeaf.distance);
	}

	private static Point findMaxPoint(HashMap<Integer, ArrayList<int[]>> graph, int startNode, int nodes) {
		boolean[] visited = new boolean[nodes + 1];
		for (int i = 0; i < nodes; i++) {
			visited[i + 1] = false;
		}
		Queue<Point> queue = new LinkedList<>();
		queue.add(new Point(startNode, 0));
		Point maxPoint = new Point(0, 0);

		while (!queue.isEmpty()) {
			Point point = queue.poll();
			if (graph.get(point.node).size() == 1 && point.node != startNode) {
				if (maxPoint.distance < point.distance) {
					maxPoint = point;
				}
				continue;
			}
			for (int[] array : graph.get(point.node)) {
				int nextNode = array[0];
				int weight = array[1];
				if (visited[nextNode] == true) {
					continue;
				}
				queue.add(new Point(nextNode, point.distance + weight));
			}
			visited[point.node] = true;
		}
		return maxPoint;
	}
}
