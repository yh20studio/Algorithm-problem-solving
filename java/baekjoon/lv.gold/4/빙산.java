/* 
    link : https://www.acmicpc.net/problem/2573
    Lv : gold 4
    Category : BFS, 구현
    
    BFS를 이용해서 각 빙산을 탐색한다. 빙산은 녹는 성질이 있다.
    동서남북 방향으로 물이 있다면 해당 빙산은 그 물의 수만큼 빨리 녹는다. 
    이것을 구현하기 위해서 주변 물을 탐색하는 메서드를 따로 구현했다. 그리고 빙산은 한번에 다같이 녹는다.
    서서희 빙산이 녹으면서 두 영역으로 나누어지는 지점이 생기는 타임 값을 찾는 문제이다.
    따라서 빙산의 위치값을 기반으로 큐를 전개했으며, 빙산이 한번에 녹도록 구현하고, 한 타임이 끝이나면
    빙산의 연결성을 테스트했다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Ice {
	public int x;
	public int y;
	public int height;
	public int time;

	public Ice(int x, int y, int height, int time) {
		this.x = x;
		this.y = y;
		this.height = height;
		this.time = time;
	}
}

public class Main {
	private static int[] dx = {-1, 0, 1, 0};
	private static int[] dy = {0, 1, 0, -1};
	private static final int VISITED = 1;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] sizeArray = bf.readLine().split(" ");
		int rowSize = Integer.parseInt(sizeArray[0]);
		int columnSize = Integer.parseInt(sizeArray[1]);

		int[][] iceBoard = new int[rowSize][columnSize];
		Queue<Ice> queue = new LinkedList<Ice>();
		for (int i = 0; i < rowSize; i++) {
			String[] rowIce = bf.readLine().split(" ");
			for (int j = 0; j < columnSize; j++) {
				if (Integer.parseInt(rowIce[j]) != 0) {
					queue.add(new Ice(i, j, Integer.parseInt(rowIce[j]), 0));
				}
				iceBoard[i][j] = Integer.parseInt(rowIce[j]);
			}
		}
		BFS(rowSize, columnSize, queue, iceBoard);
	}

	private static void BFS(int rowSize, int columnSize, Queue<Ice> queue, int[][] iceBoard) {
		int nowTime = -1;
		List<Ice> removed = new ArrayList<>();
		while (!queue.isEmpty()) {
			Ice ice = queue.poll();
			if (ice.time != nowTime) {
				removeIce(removed, iceBoard);
				if ((queue.size() + 1) != isSeparate(ice, rowSize, columnSize, iceBoard)) {
					System.out.println(nowTime + 1);
					return;
				}
				removed = new ArrayList<>();
				nowTime++;
			}
			int water = findNearWater(rowSize, columnSize, ice, iceBoard);
			if (ice.height > water) {
				queue.add(new Ice(ice.x, ice.y, ice.height - water, ice.time + 1));
				continue;
			}
			if (ice.height <= water) {
				removed.add(ice);
				continue;
			}
		}
		System.out.println(0);
	}

	private static void removeIce(List<Ice> removed, int[][] iceBoard) {
		for (Ice each : removed) {
			iceBoard[each.x][each.y] = 0;
		}
	}

	private static int isSeparate(Ice ice, int rowSize, int columnSize, int[][] iceBoard) {
		int depth = 0;
		Queue<Ice> queue = new LinkedList<>();
		queue.add(ice);

		int[][] visited = new int[rowSize][columnSize];
		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < columnSize; j++) {
				visited[i][j] = 0;
			}
		}

		while (!queue.isEmpty()) {
			ice = queue.poll();
			if (visited[ice.x][ice.y] == VISITED) {
				continue;
			}
			for (int i = 0; i < 4; i++) {
				int newRow = ice.x + dx[i];
				int newColumn = ice.y + dy[i];
				if (newRow < 0 || newRow >= rowSize || newColumn < 0 || newColumn >= columnSize) {
					continue;
				}
				if (iceBoard[newRow][newColumn] == 0) {
					continue;
				}
				queue.add(new Ice(newRow, newColumn, 0, 0));
			}
			visited[ice.x][ice.y] = VISITED;
			depth++;
		}
		return depth;
	}

	private static int findNearWater(int rowSize, int columnSize, Ice ice, int[][] iceBoard) {
		int water = 0;
		for (int i = 0; i < 4; i++) {
			int newRow = ice.x + dx[i];
			int newColumn = ice.y + dy[i];
			if (newRow < 0 || newRow >= rowSize || newColumn < 0 || newColumn >= columnSize) {
				continue;
			}
			if (iceBoard[newRow][newColumn] == 0) {
				water++;
			}
		}
		return water;
	}
}
