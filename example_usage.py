from client import VibeCoderIntentBuilderClient
client = VibeCoderIntentBuilderClient()
result = client.generate_scaffold(
    business_intent="I want an internal dashboard to track employee onboarding progress",
    platform="web"
)
print(f"Stack: {result['tech_stack']}")
for line in result["code_scaffold"]:
    print(line)
