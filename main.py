import os
from langchain.agents import Tool, initialize_agent
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.schema.messages import SystemMessage
import requests
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
load_dotenv()


# Kalkulačka
def calculator_tool(input: str) -> str:
    try:
        return str(eval(input))
    except Exception as e:
        return f"Chyba: {e}"

# Počasí – Open-Meteo API
def get_weather(city: str) -> str:
    try:
        g = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1, "language": "cs"},
            timeout=10
        )
        data = g.json()
        if not data.get("results"):
            return f"Nepodařilo se najít město {city}."
        lat = data["results"][0]["latitude"]
        lon = data["results"][0]["longitude"]

        w = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=10
        )
        wr = w.json()
        cw = wr.get("current_weather")
        if not cw:
            return "Nepodařilo se získat aktuální počasí."
        return f"Aktuální počasí v {city.title()}: {cw['temperature']}°C, vítr {cw['windspeed']} km/h."
    except Exception as e:
        return f"Chyba při počasí: {e}"

# Wikipedia tool pro českou Wikipedii
wiki_cz = WikipediaAPIWrapper(language="cs")

def wikipedia_cz_tool(query: str) -> str:
    try:
        result = wiki_cz.run(query)
        return result
    except Exception as e:
        return f"Nepodařilo se najít odpověď na Wikipedii: {e}"

# Definice nástrojů
calculator = Tool(
    name="Kalkulačka",
    func=calculator_tool,
    description="Pro matematické výpočty podle vstupu."
)
wikipedia = Tool(
    name="Wikipedia",
    func=wikipedia_cz_tool,
    description="Použij pro hledání faktů na české Wikipedii."
)
weather = Tool(
    name="Počasí",
    func=get_weather,
    description="Použij pouze při dotazu na aktuální počasí ve městě."
)

tools = [calculator, wikipedia, weather]

# Inicializace modelu
llm = ChatOpenAI(model="gpt-4o", max_tokens=500)

# Paměť
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Inicializace agenta s nástroji a pamětí
agent = initialize_agent(
    tools,
    llm,
    agent="conversational-react-description",
    memory=memory,
    verbose=True
)

print("🧠 Ahoj! Zeptej se na cokoliv. Napiš 'konec' pro ukončení.")
while True:
    q = input("🧠 Tvoje otázka: ")
    if q.lower() in ["konec", "exit", "quit"]:
        print("👋 Měj se krásně!")
        break
    response = agent.run(q)
    print(f"\n💬 Odpověď: {response}\n")
