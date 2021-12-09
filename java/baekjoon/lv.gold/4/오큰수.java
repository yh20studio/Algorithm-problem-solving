/* 
    link : https://www.acmicpc.net/problem/17298
    Lv : gold 4
    Category : 스택
    
    일반적인 반복문을 활용해서 문제를 풀면 시간초과가 발생하니,
    스택을 이용해서 자신보다 오른쪽에 있는 수들 중에서 자신보다 큰수를 찾는 문제이다.
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int sequenceSize = Integer.parseInt(bf.readLine());
		String[] sequenceArray = bf.readLine().split(" ");
		int[] sequence = new int[sequenceSize];
		for (int i = 0; i < sequenceSize; i++) {
			sequence[i] = Integer.parseInt(sequenceArray[i]);
		}
		findRightBigNumber(sequenceSize, sequence);

	}

	private static void findRightBigNumber(int sequenceSize, int[] sequence) {
		Stack<Integer> stack = new Stack<Integer>();
		for (int i = 0; i < sequenceSize; i++) {
			while (!stack.isEmpty() && sequence[stack.peek()] < sequence[i]) {
				sequence[stack.pop()] = sequence[i];
			}
			stack.push(i);
		}
		while (!stack.isEmpty()) {
			sequence[stack.pop()] = -1;
		}
		StringBuilder stringBuilder = new StringBuilder();
		for (int i = 0; i < sequenceSize; i++) {
			stringBuilder.append(sequence[i]).append(' ');
		}
		System.out.println(stringBuilder);
	}
}
