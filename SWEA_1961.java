package org.opentutorials.javatutorials.eclipse;
import java.util.Scanner;

public class SWEA_1961 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int t = 1;t<=T;t++) {
			int N = sc.nextInt();
			int[][] matrix = new int[N][N];
			for(int i = 0;i<N;i++) {
				for(int j = 0;j<N;j++) {
					matrix[i][j] = sc.nextInt();
				}
			}
			int[][] matrix90 = rotation(N, matrix);
			int[][] matrix180 = rotation(N, matrix90);
			int[][] matrix270 = rotation(N, matrix180);
			System.out.println("#"+t);
			for(int i = 0;i<N;i++) {
				for(int j = 0;j<N;j++) {
					System.out.print(matrix90[i][j]);
				}
				System.out.print(" ");
				for(int j = 0;j<N;j++) {
					System.out.print(matrix180[i][j]);
				}
				System.out.print(" ");
				for(int j = 0;j<N;j++) {
					System.out.print(matrix270[i][j]);
				}
				System.out.println();
			}
		}
	}
	
	public static int[][] rotation(int N, int[][] matrix) {
//		90도 회전시키는 메소드
//		90도 회전하면 행이 열로 바뀌면서 행의 순서가 뒤집힘
		int[][] result = new int[N][N];
		for (int i = 0;i<N;i++) {
			for (int j = 0;j<N;j++) { 
				result[i][j] = matrix[N-1-j][i];
			}
		}
		return result;
	}
}
