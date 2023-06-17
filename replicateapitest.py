import replicate
import os

from dotenv import load_dotenv

load_dotenv()
replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))
output = replicate.run(
     "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
     input={"prompt": "a 19th century portrait of a wombat gentleman"}
)
print(output)
