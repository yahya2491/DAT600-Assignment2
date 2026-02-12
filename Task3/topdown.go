package main

// RodCuttingTopDown solves the rod cutting problem using top-down memoization
func RodCuttingTopDown(prices []int, n int) int {
	memo := make([]int, n+1)
	for i := range memo {
		memo[i] = -1
	}
	return rodCuttingTopDownHelper(prices, n, memo)
}

func rodCuttingTopDownHelper(prices []int, n int, memo []int) int {
	if n <= 0 {
		return 0
	}

	// If already computed, return the memoized value
	if memo[n] != -1 {
		return memo[n]
	}

	maxVal := -1

	// Try all possible cuts and take the maximum
	for i := 1; i <= n; i++ {
		maxVal = max(maxVal, prices[i-1]+rodCuttingTopDownHelper(prices, n-i, memo))
	}

	// Store the result in memo table
	memo[n] = maxVal
	return maxVal
}
