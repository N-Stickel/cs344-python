def filter_and_summarize(numbers):
    """ Filters a list of numbers to include only the positive numbers, and computes the count, sum, and average of said numbers. """
    positive_numbers = [num for num in numbers if num > 0]
    count = len(positive_numbers)
    total_sum = sum(positive_numbers)
    average = total_sum / count if count > 0 else 0

    return {
        "positive_numbers": positive_numbers,
        "count": count,
        "sum": total_sum,
        "average": average
    }

if __name__ == "__main__":
    test_numbers = [-10, 10, -3, 0, 4, 7, 15]
    result = filter_and_summarize(test_numbers)

    print("Starting list:", test_numbers)
    print("Filtered positive numbers:", result["positive_numbers"])
    print("Count:", result["count"])
    print("Sum:", result["sum"])
    print("Average:", result["average"])
