import os

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

imageGenerationRouter = APIRouter()

load_dotenv()

openaiApiKey = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openaiApiKey)


class ImageGenerationRequestForm(BaseModel):
    userRequestDescription: str


@imageGenerationRouter.post("/request-image-generation")
async def requestImageGeneration(imageGenerationRequestForm: ImageGenerationRequestForm):
    print(f"controller -> requestImageGeneration(): imageGenerationRequestForm: {imageGenerationRequestForm}")

    generatedImageURL = client.images.generate(
        model="dall-e-3",
        prompt=("A highly detailed, high-resolution 3D rendering of a medieval siege. "
                "The scene features a vast undead army attacking a human castle. "
                "At the forefront, a menacing Death Knight in dark, "
                "intricately detailed armor, with a chilling aura and glowing eyes, leads the charge. "
                "The Death Knight should have a commanding presence, with a dark and intimidating demeanor. "
                "The undead soldiers are skeletons and ghostly creatures, "
                "shown with clear, realistic bone textures and spectral features. "
                "The human castle is engulfed in intense flames, with realistic fire, thick smoke, and collapsing walls. "
                "The scene should include dynamic lightning, detailed textures, "
                "and a scene of overwhelming destruction and chaos."),
        n=1,
        size="1024x1024"
    )

    print("Generated Image URL:", generatedImageURL)

    return JSONResponse(content=generatedImageURL, status_code=status.HTTP_200_OK)


