#!/usr/bin/env python3
"""
Test script to demonstrate background agent functionality.
This script simulates a long-running task that would benefit from running in the background.
"""

import time
import random
import sys
from datetime import datetime

def simulate_long_running_task(task_name, duration_seconds=10):
    """Simulate a long-running task with progress updates."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting {task_name}...")
    
    for i in range(duration_seconds):
        time.sleep(1)
        progress = (i + 1) / duration_seconds * 100
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {task_name}: {progress:.1f}% complete")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {task_name} completed!")
    return f"{task_name} result: {random.randint(1, 100)}"

def main():
    """Main function to run the background agent test."""
    print("=" * 60)
    print("BACKGROUND AGENT TEST")
    print("=" * 60)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Simulate different types of background tasks
    tasks = [
        ("Data Processing", 5),
        ("API Integration", 8),
        ("File Analysis", 6),
        ("Database Migration", 10)
    ]
    
    results = []
    
    for task_name, duration in tasks:
        result = simulate_long_running_task(task_name, duration)
        results.append(result)
        print()
    
    print("=" * 60)
    print("ALL TASKS COMPLETED")
    print("=" * 60)
    print(f"Test finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\nResults:")
    for i, result in enumerate(results, 1):
        print(f"  {i}. {result}")
    
    print("\nThis demonstrates how background agents can handle long-running tasks")
    print("without blocking the main execution flow.")

if __name__ == "__main__":
    main()