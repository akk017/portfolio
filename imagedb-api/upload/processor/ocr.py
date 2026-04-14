from fastapi import UploadFile
import io
import json
import traceback
import asyncio
from concurrent.futures import ThreadPoolExecutor
import ollama

MODELS = ["llava", "llama3.2-vision", "moondream", "gemma"]

SCHEMA = {
    "type": "object",
    "properties": {
        "content": {"type": "string"},
        "tag": {"type": "array", "items": {"type": "string"}},
        "url": {"type": "string"},
        "color_scheme": {"type": "array", "items": {"type": "string", "pattern": "^#[0-9a-fA-F]{6}$"}},
        "context": {"type": "string", "description": "What the image is about and what information the user can infer"},
    },
    "required": ["content", "tag", "url", "color_scheme", "context"],
}

VALID_TAGS = [
    "Dev", "Animations", "Design", "Home", "SaaS", "Offers", "CMS", "Marketing",
    "Planning", "Collaboration", "Email", "SFX", "Content", "Landing Page Testing",
    "SEO", "Studio", "Growth Hacking", "Design Studio", "App Development",
    "App Monitoring", "Landing Page", "Theme", "Tools", "Documenting",
    "Service Management", "Terms and Condition", "Privacy Policy", "Content Creation",
    "CRM", "Open-Source", "OSS", "Short Linked", "Integrations", "Sales", "AI",
    "Frontend", "Backend", "AWS", "Billing", "Collection", "Leads", "Illustrations",
    "Customer", "Feedback", "Load Testing", "Product Management", "Meetings",
    "Analytics", "Database", "Data", "Newsletters", "Inspirations", "Forms",
    "Presentation", "Learning", "UX", "UI", "Agency", "Help", "Marketplace",
    "Maths", "School", "Interaction", "Awesome", "Service", "SQL", "Terminal",
    "Auth", "Authentication", "Pricing", "Calendar", "Internal Tools", "Page Builder",
    "Builder", "React", "Blogs", "DevOps", "Productivity", "Writing", "Chat",
    "Video", "Voice", "No-Code", "Notification", "Ideas", "Twitter", "Bible",
    "Bloc", "Social Media", "PAAS", "Docs", "Knowledge Base", "BAAS",
    "Communication", "Research", "Onboarding", "Pitch", "Todo", "VC", "Pre Launch",
    "Sheets", "Testing", "Lead Generation", "Security", "Testimonials", "Banking",
    "Keywords", "Monitoring", "Fonts", "Competitor", "Scraping", "Support",
    "System", "Video", "Editor", "Interactive", "Brand", "Ads", "Mac App", "CMO",
    "Observability", "Icons", "Community", "Comments", "Backgrounds",
    "Design Portfolio", "Checklist", "Console", "Agents", "Designer", "Browser",
    "Payments", "Git", "Workflow", "Virtual Machine",
]

PROMPT = f"""
You are an expert OCR, data extraction, and visual context analysis assistant. 
Analyze the provided image carefully and extract all visible text, URLs/links, 
and rich contextual understanding.

Return a JSON object with the following fields:
- content: All readable text extracted from the image.
- tag: A list of relevant tags picked ONLY from this predefined list: {VALID_TAGS}
- url: Any prominent link or URL visible in the image (empty string if none).
- color_scheme: An array of dominant colors in the image as valid hex codes starting with '#'.
- context: What the image is about and what information the user can infer.
"""


class OCRProcessor:

    @staticmethod
    def _query_model(model: str, contents: bytes) -> dict:
        response = ollama.chat(
            model=model,
            messages=[{
                "role": "user",
                "content": PROMPT,
                "images": [contents],
            }],
            format=SCHEMA,
        )
        try:
            return json.loads(response["message"]["content"])
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            return {
                "message": "Failed to parse response",
                "response": response,
                "error_stack": traceback.format_exc(),
            }

    @staticmethod
    async def process(image: UploadFile) -> dict:
        contents = await image.read()
        loop = asyncio.get_event_loop()
        with ThreadPoolExecutor() as executor:
            tasks = [
                loop.run_in_executor(executor, OCRProcessor._query_model, model, contents)
                for model in MODELS
            ]
            results = await asyncio.gather(*tasks)
        return dict(zip(MODELS, results))