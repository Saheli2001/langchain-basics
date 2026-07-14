from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
load_dotenv()

model = ChatOpenAI(model_name="gpt-5-nano")
json_schema ={
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A list of key themes mentioned in the review"
        },
        "summary": {
            "type": "string",
            "description": "A short summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "The sentiment of the review (positive, negative, or neutral)"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "A list of pros mentioned in the review, if any"
        },
        "cons": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "A list of cons mentioned in the review, if any"
        },
        "required": ["key_themes", "summary", "sentiment"]
    },
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""
The hardware is great. Loved the product. But the colour is a bit dull. Overall I'd like to keep it and suggest it to other customers.""")

print(result)