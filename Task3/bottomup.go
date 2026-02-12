package main

// RodCuttingBottomUp solves the rod cutting problem using bottom-up tabulation
func RodCuttingBottomUp(prices []int, n int) int {
	if n <= 0 {
		return 0
	}

	// Create a table to store results of subproblems
	dp := make([]int, n+1)
	dp[0] = 0

	// Build the table in bottom-up manner
	for i := 1; i <= n; i++ {
		maxVal := -1
		for j := 1; j <= i; j++ {
			maxVal = max(maxVal, prices[j-1]+dp[i-j])
		}
		dp[i] = maxVal
	}

	return dp[n]
}
