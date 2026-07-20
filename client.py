class VibeCoderIntentBuilderClient:
    PLATFORM_STACKS = {
        "web": "Next.js 15 + TypeScript + Tailwind + Prisma",
        "mobile": "React Native + Expo + NativeWind",
        "api": "FastAPI + Python + PostgreSQL + Redis",
        "internal": "Retool + PostgreSQL + REST API",
        "automation": "n8n + Webhook + OpenAI API"
    }

    def generate_scaffold(self, business_intent: str, platform: str) -> dict:
        stack = self.PLATFORM_STACKS.get(platform.lower(), "Next.js + TypeScript")
        words = [w for w in business_intent.split() if len(w) > 3]
        scaffold = [
            f"// Auto-generated scaffold for: {business_intent[:60]}",
            f"// Stack: {stack}",
            "",
            f"// 1. Define data model for '{words[0] if words else 'Entity'}'",
            f"// 2. Create CRUD API endpoints",
            f"// 3. Build UI components with form validation",
            f"// 4. Add authentication & role-based access",
            f"// 5. Deploy to production with CI/CD pipeline"
        ]
        return {"code_scaffold": scaffold, "tech_stack": stack}
