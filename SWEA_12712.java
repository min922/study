package org.opentutorials.javatutorials.eclipse;
import java.util.Scanner;

public class SWEA_12712 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1;t<=T;t++) {
			int n = sc.nextInt(); int m = sc.nextInt();
			int[][] board = new int[n][n];
			for(int i = 0;i<n;i++) {
				for(int j = 0;j<n;j++) {
					board[i][j] = sc.nextInt();
				}
			}
			int[] dpcol = {-1, 0, 1, 0}; int[] dprow = {0, 1, 0, -1}; // +형으로 뿌릴 때
			int[] dxcol = {1, -1, -1, 1}; int[] dxrow = {1, 1, -1, -1}; // x형으로 뿌릴 때
			int result = -1;
			for(int col = 0;col < n;col++) {
				for(int row = 0;row < n;row++) {
					int fly = board[col][row];
					for(int i = 1;i<m;i++) { // 기준점도 포함 -> 1부터 m-1칸만 탐색
						for(int j = 0;j<4;j++) {
							int ncol = col+dpcol[j]*i; // 기준 위치에서 m칸 옆으로
							int nrow = row+dprow[j]*i; // 기준 위치에서 m칸 위아래로
							if (ncol>=0 && ncol<n && nrow>=0 && nrow<n) { // n*n 범위 안에 있으면
								fly += board[ncol][nrow]; // 잡은 파리 수에 더하기
							}
						}
					}
					result = Math.max(fly, result); // 최대값 갱신
				}
			}
			for(int col = 0;col < n;col++) {
				for(int row = 0;row < n;row++) {
					int fly = board[col][row];
					for(int i = 1;i<m;i++) {
						for(int j = 0;j<4;j++) {
							int ncol = col+dxcol[j]*i; // 기준 위치에서 m칸 대각선으로 이동
							int nrow = row+dxrow[j]*i;
							if (ncol>=0 && ncol<n && nrow>=0 && nrow<n) {
								fly += board[ncol][nrow];
							}
						}
					}
					result = Math.max(fly, result);
				}
			}
			System.out.println("#"+t+" "+result);
		}
	}
}
