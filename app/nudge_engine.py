def generate_nudge(transactions):
  food_spending = sum(t["amount"] for t in transactions if t["category"] == "Food Delivery")
  if food_spending > 2000:
      return f"You've spent ₹{food_spending} on food delivery this week! Try cooking at home 🍲"
  elif food_spending > 1000:
      return f"Food delivery is creeping up! You've spent ₹{food_spending} already. 🍔"
  return "Great job! You're keeping spending in check. 💪"

def check_savings_goal(saved_amount, goal=100):
  if saved_amount >= goal:
      return "🎉 You reached your goal! Reward unlocked!"
  else:
      return f"💰 Save ₹{goal - saved_amount} more to unlock your reward."
