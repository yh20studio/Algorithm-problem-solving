/* 
    link : https://www.acmicpc.net/problem/1697
    Lv : silver 1
    Category : BFS
    
    수빈이의 위치와 시간을 기반으로 BFS를 이용해서 동생의 위치까지 탐색하는 것으로 해결했습니다.
*/


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class Subin{
    int location;
    int time;

    Subin(int location, int time){
        this.location = location;
        this.time = time;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] st = bf.readLine().split(" ");

        int N = Integer.parseInt(st[0]);
        int K = Integer.parseInt(st[1]);

        BFS(N, K);
    }

    public static void BFS(int N, int K){
        Queue<Subin> queue = new LinkedList<Subin>();
        queue.add(new Subin(N, 0));

        int[] visited = new int[100001];
        for (int i= 0; i < 100001; i++){
            visited[i] = 1000001;
        }

        while (!queue.isEmpty()){
            Subin subin = queue.poll();

            if (subin.location == K){
                System.out.println(subin.time);
                return;
            }

            if (subin.location == -1 || subin.location > 100000){
                continue;
            }

            if (visited[subin.location] <= subin.time){
                continue;
            }

            queue.add(new Subin(subin.location + 1, subin.time + 1));
            queue.add(new Subin(subin.location - 1, subin.time + 1));

            if(subin.location != 0){
                queue.add(new Subin(subin.location * 2, subin.time + 1));
            }

            visited[subin.location] = subin.time;

        }
    }
}