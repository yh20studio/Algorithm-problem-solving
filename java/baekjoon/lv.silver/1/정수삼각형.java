/* 
    link : https://www.acmicpc.net/problem/1932
    Lv : silver 1
    Category : BFS
    
    정수 삼각형을 아래로 탐색하면서 최댓값을 찾는 문제입니다.
    BFS를 이용해서 단계적으로 탐색하며 방문관리를 통해서 불 필요한 반복이 되지 않도록 했습니다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Triangle{
    int x;
    int y;

    Triangle(int x, int y){
        this.x = x;
        this.y = y;
    }
}


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        int[][] arr = new int[n][n];

        for(int i = 0; i< n; i++){
            String [] st = bf.readLine().split(" ");

            for(int j = 0; j <= i; j++){
                arr[i][j] = Integer.parseInt(st[j]);
            }
        }

        BFS(arr, n);
    }

    private static void BFS(int[][] arr, int n){
        int answer = 0;
        int[][] visited = new int[n][n];
        for(int i=0; i< n; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = 0;
            }
        }
        Queue<Triangle> queue = new LinkedList<Triangle>();
        queue.add(new Triangle(0, 0));
        visited[0][0] = arr[0][0];

        while (!queue.isEmpty()){
            Triangle triangle = queue.poll();

            if(triangle.x == n-1){
                answer = Math.max(answer, visited[triangle.x][triangle.y]);
                continue;
            }

            if(visited[triangle.x+1][triangle.y+1] < visited[triangle.x][triangle.y] + arr[triangle.x + 1][triangle.y + 1]){
                visited[triangle.x+1][triangle.y+1] = visited[triangle.x][triangle.y] + arr[triangle.x + 1][triangle.y + 1];
                queue.add(new Triangle(triangle.x + 1, triangle.y + 1));
                
            }

            if(visited[triangle.x+1][triangle.y] < visited[triangle.x][triangle.y] + arr[triangle.x + 1][triangle.y]){
                visited[triangle.x+1][triangle.y] = visited[triangle.x][triangle.y] + arr[triangle.x + 1][triangle.y];
                queue.add(new Triangle(triangle.x + 1, triangle.y));
            }
            
        }

        System.out.println(answer);

    }

}