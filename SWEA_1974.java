package org.opentutorials.javatutorials.eclipse;
import java.util.Scanner;

public class SWEA_1974 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int t= 1; t<=T;t++) {
			int[][] board = new int[9][9];
			for(int i = 0;i<9;i++) {
				for(int j = 0;j<9;j++) {
					board[i][j] = sc.nextInt();
				}
			}
			int result = 1;
			for(int i = 0;i < 9;i++) { // 가로줄 확인
				int row = 0;
				for(int j = 0; j<9;j++) {
					row += board[i][j];
				}
				if (row != 45) {
					result = 0;
					break;
				}
			}
			for(int i = 0;i < 9;i++) { // 세로줄 확인
				int column = 0;
				for(int c = 0; c<9;c++) {
					column += board[c][i];
				}
				if (column != 45) {
					result = 0;
					break;
				}
			}
			for(int i = 0;i < 9;i+=3) { // 사각형 확인
				for(int s = 0;s<9;s+=3) {
					int square = 0;
					for(int r = i;r<i+3;r++) {
						for(int c = s;c<s+3;c++) {
							square += board[r][c];
						}
					}
					if (square != 45) {
						result = 0;
						break;
					}
				}
			}
			System.out.println("#"+t+" "+result);
		}
	}
}
