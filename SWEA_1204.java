package org.opentutorials.javatutorials.eclipse;

import java.util.Scanner;

public class SWEA_1204 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T, num;
		T = sc.nextInt();
		for (int t = 0;t<T;t++) {
			num = sc.nextInt();	
			int[] score = new int[101];
			for (int i = 0; i <1000 ; i++) {
				score[sc.nextInt()]++;
			}
			int appear = 0, idx = 0;
			for (int j = 100;j>0;j--) {
				if (score[j]>appear) {
					appear = score[j];
					idx = j;
				}
			}
			System.out.println("#"+num+" "+idx);
		}
	}
}
