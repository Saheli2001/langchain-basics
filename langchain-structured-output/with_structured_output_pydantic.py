from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field
load_dotenv()

model = ChatOpenAI(model_name="gpt-5-nano")

# schema - simple 
# class Review(TypedDict):

#     summary: str
#     sentiment: str

# schema - with Annotated
class Review(BaseModel):

    key_themes: list[str] = Field(description="A list of key themes mentioned in the review")
    summary: str = Field(description="A short summary of the review")
    sentiment: Literal['pos','neg'] = Field(description="The sentiment of the review (positive, negative, or neutral)")
    pros: Optional[list[str]] = Field(default = None, description="A list of pros mentioned in the review, if any")
    cons: Optional[list[str]] = Field(default = None, description="A list of cons mentioned in the review, if any")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
The hardware is great. Loved the product. But the colour is a bit dull. Overall I'd like to keep it and suggest it to other customers.""")

print(result)