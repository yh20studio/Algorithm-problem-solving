/* 
    link : https://www.acmicpc.net/problem/2156
    Lv : silver 1
    Category : 다이나믹 프로그래밍
    
    포도주를 연속해서 3번을 마실 수 없으니, 포도주를 안마시는 경우를 추적해서
    다이나믹 프로그래밍으로 구현해봤습니다. 
    
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(bf.readLine());
        }

        DP(arr, n);
    }

    private static void DP(int[] arr, int n) {
        int[] dp = new int[n];

        if (n == 1) {
            System.out.println(arr[0]);
            return;
        }

        if (n == 2) {
            System.out.println(arr[0] + arr[1]);
            return;
        }
        dp[0] = arr[0];
        dp[1] = arr[0] + arr[1];
        dp[2] = Math.max(dp[0] + arr[2], dp[1]);
        dp[2] = Math.max(dp[2], arr[1] + arr[2]);

        for (int i = 3; i < n; i++) {
            dp[i] = Math.max(dp[i - 2] + arr[i], dp[i - 1]);
            dp[i] = Math.max(dp[i], dp[i - 3] + arr[i - 1] + arr[i]);
        }

        System.out.println(dp[n - 1]);
    }
}