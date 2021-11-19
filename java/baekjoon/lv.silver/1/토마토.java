// link : https://www.acmicpc.net/problem/7576
// Lv : silver 1
// Category : BFS

// BFS를 통해서 익은 토마토들이 단계별로 퍼져나가는 것을 표현했습니다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Tomato{
    int x;
    int y;

    Tomato(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class Main {

    static int[] dx = { -1, 0, 1, 0 };
    static int[] dy = { 0, 1, 0, -1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
        String[] s = br.readLine().split(" ");
        int M = Integer.parseInt(s[0]);
        int N = Integer.parseInt(s[1]);

        int[][] tomatoArray = new int[N][M];

        for(int i = 0; i<N; i++){
            String[] rowArray = br.readLine().split(" ");
            for(int j = 0; j<M; j++){
                tomatoArray[i][j] = Integer.parseInt(rowArray[j]);
            }
        }

        BFS(tomatoArray, M, N);
    }

    public static void BFS(int[][] arr, int M, int N) {

        Queue<Tomato> queue = new LinkedList<Tomato>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 1)
                    //익은 토마토가 있는 모든 위치를 큐에 담는다.
                    queue.add(new Tomato(i, j));
            }
        }

        while (!queue.isEmpty()){
            Tomato tomato = queue.poll();
            for (int d = 0; d < 4; d++){
                int newX = tomato.x + dx[d];
                int newY = tomato.y + dy[d];

                if (newX < 0 || newX >= N || newY < 0 || newY >= M){
                    continue;
                }
                if (arr[newX][newY] != 0){
                    continue;
                }

                arr[newX][newY] = arr[tomato.x][tomato.y] + 1;
                queue.add(new Tomato(newX, newY));
            }
        }

        int maxDay = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(arr[i][j] == 0){
                    System.out.println(-1); // 익지 않은 토마토가 있다면?
                    return;
                }
                maxDay = Math.max(maxDay, arr[i][j]);
            }
        }

        System.out.println(maxDay - 1);
    }

}