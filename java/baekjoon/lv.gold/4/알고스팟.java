/* 
    link : https://www.acmicpc.net/problem/1261
    Lv : gold 4
    Category : BFS, 우선순위 큐
    
    BFS를 이용해서 각 방을 이동하는 것을 표현한다. 이때 벽을 최소한으로 부셔야 하므로
    우선순위 큐를 이용해서 벽을 깬 횟수가 작은 순으로 탐색을 하도록 구현했다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

class Room implements Comparable<Room>{
    public int x;
    public int y;
    public int crush;

    Room(int x, int y, int crush){
        this.x = x;
        this.y = y;
        this.crush = crush;
    }

    @Override
    public int compareTo(Room another){ // crush가 작은 순으로
        if(this.crush <= another.crush){
            return -1;
        }
        return 1;
    }
    public void increaseCrush(){
        this.crush ++;
    }
}

public class Main {
    private static final int VISITED = -1;
    private static final int WALL = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] sizeArray = bf.readLine().split(" ");
        int M = Integer.parseInt(sizeArray[0]);
        int N = Integer.parseInt(sizeArray[1]);

        int[][] board = new int[N][M];
        for (int i =0; i< N; i++){
            String[] rowArray = bf.readLine().split("");
            for(int j =0; j<M; j++){
                board[i][j] = Integer.parseInt(rowArray[j]);
            }
        }
        BFS(N, M, board);
    }

    private static void BFS(int N, int M, int[][] board) {
        PriorityQueue<Room> priorityQueue = new PriorityQueue<>();
        Room startRoom = new Room(0, 0, 0);
        priorityQueue.add(startRoom);
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        while (!priorityQueue.isEmpty()){
            Room room = priorityQueue.poll();
            if(room.x == N-1 && room.y == M-1){
                System.out.println(room.crush);
                return;
            }
            if(board[room.x][room.y] == VISITED){
                continue;
            }
            if(board[room.x][room.y] == WALL){
                room.increaseCrush();
            }

            for(int i = 0; i< 4; i++){
                int newX = room.x + dx[i];
                int newY = room.y + dy[i];
                if(newX <0 || newX >= N ){
                    continue;
                }
                if(newY <0 || newY >= M){
                    continue;
                }
                priorityQueue.add(new Room(newX, newY, room.crush));
            }
            board[room.x][room.y] = VISITED;
        }
    }
}