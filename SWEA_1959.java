package org.opentutorials.javatutorials.eclipse;

import java.util.Scanner;

public class SWEA_1959 {

	public static void main(String[] args) {
		int T, n, m;
		Scanner sc = new Scanner(System.in);
		T = sc.nextInt();
		for(int t = 1;t<=T;t++) {
			n = sc.nextInt(); m = sc.nextInt();
			int[] A = new int[n];
			int[] B = new int[m];
			for (int i = 0;i < n;i++) {
				A[i] = sc.nextInt();
			}
			for (int i = 0;i < m;i++) {
				B[i] = sc.nextInt();
			}
			int result = 0;
			if (n == m) {
				int tmp = 0;
				for(int i = 0;i<n;i++) {
					tmp += (A[i]*B[i]);
				}
				result = Math.max(tmp, result);
			}
			else if(n<m) {
				for(int i = 0;i<m-n+1;i++) {
					int tmp = 0;
					for(int j = 0; j < n;j++) {
						tmp += (A[j]*B[i+j]);
					}
					result = Math.max(tmp, result);
				}
			}
			else {
				for(int i = 0;i<n-m+1;i++) {
					int tmp = 0;
					for(int j = 0; j < m;j++) {
						tmp += (A[i+j]*B[j]);
					}
					result = Math.max(tmp, result);
				}
			}
			System.out.println("#"+t+" "+result);
		}
	}
}
