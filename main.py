# from langchain_ollama import ChatOllama
# from browser_use import Agent, Browser, BrowserConfig, Controller
# from pydantic import BaseModel
# from dotenv import load_dotenv
# from typing import List

# load_dotenv()

# import asyncio


# # class Post(BaseModel):
# #     caption: str
# class Product(BaseModel):
#     productName: str
#     price: int
#     discountedPrice: int
#     url: str


# class Products(BaseModel):
#     products: List[Product]


# # NOTE: Para o modelo utilizar o formato de Product acima
# controller = Controller(output_model=Products)

# # NOTE: Configure the browser to connect to your Chrome instance
# # NOTA: Para abrir o navegador Chrome padrão, para que a IA possa navegar com as contas do usuário
# # browser = Browser(
# #     config=BrowserConfig(
# #         # Specify the path to your Chrome executable
# #         chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
# #     )
# # )


# # Initialize the model
# llm = ChatOllama(model="qwen2.5", num_ctx=32000)


# # Create agent with the model
# async def main():
#     # NOTE: Ações inicial do Agent AI
#     initial_actions = [
#         {"open_tab": {"url": "https://www.kabum.com.br"}},
#     ]
#     # NOTE: Para senhas e logins utilizados em sites
#     # sensitive_data = {"x_name": "magnus", "x_password": "12345678"}
#     agent = Agent(
#         task="Obtenha os 5 primeiros produtos em oferta.",
#         llm=llm,
#         # browser=browser, # NOTE: Use the browser instance created above
#         controller=controller,  # NOTE: Para o modelo utilizar o formato de Product
#         initial_actions=initial_actions,  # NOTE: Ações iniciais para abrir a aba do Chrome de acessar a url tal
#         # sensitive_data=sensitive_data,
#     )
#     result = await agent.run()
#     # print(result) # Print the raw result
#     # print(result.extracted_content()) # Print the extracted content
#     print(result.final_result())  # Print the final result
#     data = result.final_result()
#     parsed: Products = Products.model_validate_json(data)
#     # await browser.close() # NOTE: Close the browser instance


# asyncio.run(main())


from langchain_ollama import ChatOllama
from browser_use import Agent, Browser, BrowserConfig, Controller
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List

load_dotenv()

import asyncio


# class Post(BaseModel):
#     caption: str
class Product(BaseModel):
    productName: str
    price: int
    discountedPrice: int
    url: str


class Products(BaseModel):
    products: List[Product]


# NOTE: Para o modelo utilizar o formato de Product acima
controller = Controller(output_model=Products)

# NOTE: Configure the browser to connect to your Chrome instance
# NOTA: Para abrir o navegador Chrome padrão, para que a IA possa navegar com as contas do usuário
# browser = Browser(
#     config=BrowserConfig(
#         # Specify the path to your Chrome executable
#         chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
#     )
# )


# Initialize the model
llm = ChatOllama(model="qwen2.5", num_ctx=32000)


# Create agent with the model
async def main():
    # NOTE: Ações inicial do Agent AI
    initial_actions = [
        {"open_tab": {"url": "https://www.kabum.com.br"}},
    ]
    # NOTE: Para senhas e logins utilizados em sites
    # sensitive_data = {"x_name": "magnus", "x_password": "12345678"}
    agent = Agent(
        task="Obtenha os 5 primeiros produtos em oferta.",
        llm=llm,
        # browser=browser, # NOTE: Use the browser instance created above
        controller=controller,  # NOTE: Para o modelo utilizar o formato de Product
        initial_actions=initial_actions,  # NOTE: Ações iniciais para abrir a aba do Chrome de acessar a url tal
        # sensitive_data=sensitive_data,
    )
    result = await agent.run()
    # print(result) # Print the raw result
    # print(result.extracted_content()) # Print the extracted content
    print(result.final_result())  # Print the final result
    data = result.final_result()
    parsed: Products = Products.model_validate_json(data)
    # await browser.close() # NOTE: Close the browser instance


asyncio.run(main())
