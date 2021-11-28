/* 
    link : https://www.acmicpc.net/problem/10844
    Lv : silver 1
    Category : 다이나믹 프로그래밍
    
    각 더하기 게산을 지속적으로 이용할 수 있도록 dp를 활용해서 저장된 값을 이용한다.
    0과 9를 제외하고서는 이전 row에서 양쪽 숫자들의 dp 값을 더해주면 되기 때문이다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final long mod = 1000000000L;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        countStep(n);
    }

    private static void countStep(int n) {
        long[][] dp = new long[n][10];

        for(int i = 0; i < n; i++){
            for(int j=0; j<10; j++){
                if(i == 0 && j != 0){
                    dp[0][j] = 1L;
                }
                else{
                    dp[i][j] = 0L;
                }
            }
        }

        for(int i=1; i< n; i++){
            for(int j=0; j<10; j++){
                if(j-1 >= 0){
                    dp[i][j] += dp[i-1][j-1];
                }
                if(j+1 <= 9){
                    dp[i][j] += dp[i-1][j+1];
                }
                dp[i][j] %= mod;
            }
        }
        System.out.println(getAnswer(dp, n));
    }

    private static long getAnswer(long[][] dp, int n){
        long answer = 0L;
        for(int j=0; j<10; j++) {
            answer += dp[n-1][j];
        }
        return answer % mod;
    }
}