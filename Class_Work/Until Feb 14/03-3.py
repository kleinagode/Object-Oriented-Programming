
def scores():

    midterm_scores = [90, 81, 93, 75, 86]
    final_scores = [91, 92, 73, 84]
    all_scores = midterm_scores + final_scores

    took_midterm = len(midterm_scores)
    took_final = len(final_scores)
    dropped_class = took_midterm - took_final
    final_min = min(final_scores)
    final_max = max(final_scores)

    print(f"{took_midterm} students took the midterm.")
    print(f"{took_final} students took the final.")
    print(f"{dropped_class} students must have dropped the class.")
    print(f"Final scores ranged from {final_min} to {final_max}")



scores()