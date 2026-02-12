package main

import (
	"fmt"
	"image/color"
	"time"

	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
)

func main() {
	// Define price array (index i represents price for length i+1)
	prices := []int{1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33, 36, 39, 40, 43, 45, 48, 50, 52, 54}

	// Test different rod lengths
	testSizes := []int{5, 8, 10, 12, 14, 16, 18, 20}

	fmt.Println("Rod Cutting Problem - Performance Comparison")
	fmt.Println("=============================================\n")

	var naiveTimes, topDownTimes, bottomUpTimes plotter.XYs

	for _, n := range testSizes {
		fmt.Printf("Testing with rod length: %d\n", n)

		// Measure Naive Approach (only for smaller values to avoid long waits)
		var naiveTime time.Duration
		var naiveResult int
		if n <= 16 {
			start := time.Now()
			naiveResult = RodCuttingNaive(prices, n)
			naiveTime = time.Since(start)
			fmt.Printf("  Naive Recursion:  Result = %d, Time = %v\n", naiveResult, naiveTime)
			naiveTimes = append(naiveTimes, plotter.XY{X: float64(n), Y: float64(naiveTime.Microseconds())})
		} else {
			fmt.Printf("  Naive Recursion:  Skipped (too slow)\n")
		}

		// Measure Top-Down Approach
		start := time.Now()
		topDownResult := RodCuttingTopDown(prices, n)
		topDownTime := time.Since(start)
		fmt.Printf("  Top-Down (Memo):  Result = %d, Time = %v\n", topDownResult, topDownTime)
		topDownTimes = append(topDownTimes, plotter.XY{X: float64(n), Y: float64(topDownTime.Microseconds())})

		// Measure Bottom-Up Approach
		start = time.Now()
		bottomUpResult := RodCuttingBottomUp(prices, n)
		bottomUpTime := time.Since(start)
		fmt.Printf("  Bottom-Up (Tab):  Result = %d, Time = %v\n", bottomUpResult, bottomUpTime)
		bottomUpTimes = append(bottomUpTimes, plotter.XY{X: float64(n), Y: float64(bottomUpTime.Microseconds())})

		fmt.Println()
	}

	// Create the plot
	if err := createPlot(naiveTimes, topDownTimes, bottomUpTimes); err != nil {
		fmt.Printf("Error creating plot: %v\n", err)
	} else {
		fmt.Println("Plot saved as 'execution_time_graph.png'")
	}
}

func createPlot(naiveTimes, topDownTimes, bottomUpTimes plotter.XYs) error {
	p := plot.New()

	p.Title.Text = "Rod Cutting: Execution Time Comparison"
	p.X.Label.Text = "Rod Length (n)"
	p.Y.Label.Text = "Execution Time (microseconds)"

	// Add grid
	p.Add(plotter.NewGrid())

	// Create line plots for each approach
	if len(naiveTimes) > 0 {
		naiveLine, naivePoints, err := plotter.NewLinePoints(naiveTimes)
		if err != nil {
			return err
		}
		naiveLine.Color = color.RGBA{R: 255, G: 0, B: 0, A: 255}
		naivePoints.Color = color.RGBA{R: 255, G: 0, B: 0, A: 255}
		naiveLine.Width = vg.Points(2)
		p.Add(naiveLine, naivePoints)
		p.Legend.Add("Naive Recursion", naiveLine, naivePoints)
	}

	topDownLine, topDownPoints, err := plotter.NewLinePoints(topDownTimes)
	if err != nil {
		return err
	}
	topDownLine.Color = color.RGBA{R: 0, G: 0, B: 255, A: 255}
	topDownPoints.Color = color.RGBA{R: 0, G: 0, B: 255, A: 255}
	topDownLine.Width = vg.Points(2)
	p.Add(topDownLine, topDownPoints)
	p.Legend.Add("Top-Down (Memoization)", topDownLine, topDownPoints)

	bottomUpLine, bottomUpPoints, err := plotter.NewLinePoints(bottomUpTimes)
	if err != nil {
		return err
	}
	bottomUpLine.Color = color.RGBA{R: 0, G: 200, B: 0, A: 255}
	bottomUpPoints.Color = color.RGBA{R: 0, G: 200, B: 0, A: 255}
	bottomUpLine.Width = vg.Points(2)
	p.Add(bottomUpLine, bottomUpPoints)
	p.Legend.Add("Bottom-Up (Tabulation)", bottomUpLine, bottomUpPoints)

	p.Legend.Top = true
	p.Legend.Left = true

	// Save the plot
	if err := p.Save(8*vg.Inch, 6*vg.Inch, "execution_time_graph.png"); err != nil {
		return err
	}

	return nil
}
