/* 
    link : https://www.acmicpc.net/problem/17144
    Lv : gold 4
    Category : BFS, 구현
    
    BFS를 이용해서 각 미세먼지가 한번에 확산되도록 구현했고,
    공기청정기를 기준으로 윗 공기청정기는 반시계방향, 아랫 공기청정기는 시계방향으로
    먼지를 청소하는 과정을 구현했습니다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class DustSpread {
	public int x;
	public int y;
	public int amount;
	public List<Integer> direction;

	public DustSpread(int x, int y, int amount, List<Integer> direction) {
		this.x = x;
		this.y = y;
		this.amount = amount;
		this.direction = direction;
	}
}

public class Main {
	private static int[] dx = {-1, 0, 1, 0};
	private static int[] dy = {0, 1, 0, -1};
	private static final int AIR_CLEANER = -1;
	private static final int EMPTY = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] sizeArray = bf.readLine().split(" ");
		int rowSize = Integer.parseInt(sizeArray[0]);
		int columnSize = Integer.parseInt(sizeArray[1]);
		int time = Integer.parseInt(sizeArray[2]);
		int totalDustAmount = 0;

		int[][] dustBoard = new int[rowSize][columnSize];
		ArrayList<int[]> airCleanerLocation = new ArrayList();
		for (int i = 0; i < rowSize; i++) {
			String[] rowIce = bf.readLine().split(" ");
			for (int j = 0; j < columnSize; j++) {
				if (Integer.parseInt(rowIce[j]) == AIR_CLEANER) {
					airCleanerLocation.add(new int[] {i, j});
					dustBoard[i][j] = Integer.parseInt(rowIce[j]);
					continue;
				}
				dustBoard[i][j] = Integer.parseInt(rowIce[j]);
				totalDustAmount += dustBoard[i][j];
			}
		}
		for (int t = 0; t < time; t++) {
			spreadDust(rowSize, columnSize, dustBoard);
			totalDustAmount -= cleanAirWithTop(rowSize, columnSize, airCleanerLocation.get(0), dustBoard);
			totalDustAmount -= cleanAirWithBottom(rowSize, columnSize, airCleanerLocation.get(1), dustBoard);
		}
		System.out.println(totalDustAmount);
	}

	private static void spreadDust(int rowSize, int columnSize, int[][] dustBoard) {
		List<DustSpread> dustSpreadList = new ArrayList<DustSpread>();

		for (int i = 0; i < rowSize; i++) {
			for (int j = 0; j < columnSize; j++) {
				if (dustBoard[i][j] == AIR_CLEANER) {
					continue;
				}
				if (dustBoard[i][j] == EMPTY) {
					continue;
				}
				DustSpread dustSpread = new DustSpread(i, j, dustBoard[i][j],
					countSpread(rowSize, columnSize, i, j, dustBoard));
				dustSpreadList.add(dustSpread);
			}
		}

		for (DustSpread each : dustSpreadList) {
			int amountDust = each.amount / 5;
			for (Integer d : each.direction) {
				int newRow = each.x + dx[d];
				int newColumn = each.y + dy[d];
				dustBoard[newRow][newColumn] += amountDust;
			}
			dustBoard[each.x][each.y] -= amountDust * each.direction.size();
		}
	}

	private static List<Integer> countSpread(int rowSize, int columnSize, int row, int column, int[][] dustBoard) {
		List<Integer> directionList = new ArrayList<>();
		for (int i = 0; i < 4; i++) {
			int newRow = row + dx[i];
			int newColumn = column + dy[i];
			if (newRow < 0 || newRow >= rowSize || newColumn < 0 || newColumn >= columnSize) {
				continue;
			}
			if (dustBoard[newRow][newColumn] == AIR_CLEANER) {
				continue;
			}
			directionList.add(i);
		}
		return directionList;
	}

	private static int cleanAirDownDirection(int rowSize, int row, int column, int beforeDust, int[][] dustBoard) {
		while (row < (rowSize - 1)) {
			row++;
			int tmpDust = dustBoard[row][column];
			if (tmpDust == AIR_CLEANER) {
				break;
			}
			dustBoard[row][column] = beforeDust;
			beforeDust = tmpDust;
		}
		return beforeDust;
	}

	private static int cleanAirLeftDirection(int row, int column, int beforeDust, int[][] dustBoard) {
		while (column > 0) {
			column--;
			int tmpDust = dustBoard[row][column];
			dustBoard[row][column] = beforeDust;
			beforeDust = tmpDust;
		}
		return beforeDust;
	}

	private static int cleanAirUpDirection(int row, int column, int beforeDust, int[][] dustBoard) {
		while (row > 0) {
			row--;
			int tmpDust = dustBoard[row][column];
			if (tmpDust == AIR_CLEANER) {
				break;
			}
			dustBoard[row][column] = beforeDust;
			beforeDust = tmpDust;
		}
		return beforeDust;
	}

	private static int cleanAirRightDirection(int columnSize, int row, int column, int beforeDust, int[][] dustBoard) {
		while (column < (columnSize - 1)) {
			column++;
			int tmpDust = dustBoard[row][column];
			dustBoard[row][column] = beforeDust;
			beforeDust = tmpDust;
		}
		return beforeDust;
	}

	private static int cleanAirWithTop(int rowSize, int columnSize, int[] airCleanerTop, int[][] dustBoard) {
		int row = airCleanerTop[0];
		int column = airCleanerTop[1];
		int beforeDust = 0;
		beforeDust = cleanAirRightDirection(columnSize, row, column, beforeDust, dustBoard);
		column = columnSize - 1;
		beforeDust = cleanAirUpDirection(row, column, beforeDust, dustBoard);
		row = 0;
		beforeDust = cleanAirLeftDirection(row, column, beforeDust, dustBoard);
		column = 0;
		return cleanAirDownDirection(rowSize, row, column, beforeDust, dustBoard);
	}

	private static int cleanAirWithBottom(int rowSize, int columnSize, int[] airCleanerBottom, int[][] dustBoard) {
		int row = airCleanerBottom[0];
		int column = airCleanerBottom[1];
		int beforeDust = 0;
		beforeDust = cleanAirRightDirection(columnSize, row, column, beforeDust, dustBoard);
		column = columnSize - 1;
		beforeDust = cleanAirDownDirection(rowSize, row, column, beforeDust, dustBoard);
		row = rowSize - 1;
		beforeDust = cleanAirLeftDirection(row, column, beforeDust, dustBoard);
		column = 0;
		return cleanAirUpDirection(row, column, beforeDust, dustBoard);
	}
}