package main

// RodCuttingNaive solves the rod cutting problem using naive recursion
func RodCuttingNaive(prices []int, n int) int {
	if n <= 0 {
		return 0
	}

	maxVal := -1

	// Try all possible cuts and take the maximum
	for i := 1; i <= n; i++ {
		maxVal = max(maxVal, prices[i-1]+RodCuttingNaive(prices, n-i))
	}

	return maxVal
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
