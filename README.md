# 🧠 AI Agent s LangChain, nástroji (ReAct), s Wolfram Tool

Tento projekt je vypracovaný jako úkol do kurzu AI Agentů. Tento projekt obsahuje jednoduchého AI agenta postaveného na frameworku **LangChain**, který komunikuje přes OpenAI LLM (model `gpt-4o`). Agent používá nástroje (tooly) pro vyhledávání na české Wikipedii, jednoduchou kalkulačku a aktuální počasí přes Open-Meteo API a Wolfram Alpha pro pokročilé výpočty a vědecké dotazy.

## 🎯 Cíl projektu

Vytvořit funkčního agenta, který:
- Pracuje s jazykovým modelem (LLM),
- Umí používat externí nástroje (tools),
- Zachovává historii konverzace (paměť),
- Je postaven na jednom z vybraných frameworků (zde: **LangChain**),
- Je odevzdán ve formě **zdrojového kódu** na GitHubu.


## 🛠 Použité nástroje (tools)

Agent v tomto projektu umí:

- 📐 **Kalkulačka**: Vyhodnotí matematické výrazy.
- 🌐 **Česká Wikipedia**: Vyhledá informace přes českou Wikipedii.
- 🌦 **Počasí**: Získá aktuální počasí ve zvoleném městě přes Open-Meteo API.
- 🔬 **Wolfram Alpha**: Používá Wolfram Alpha API pro přesné výpočty, fakta a vědecké informace z oblastí matematiky, fyziky, chemie a dalších vědních oborů.

Navíc využívá:

- 💬 **Paměť konverzace**: Udržuje historii předchozích dotazů a odpovědí.
- 🔑 **OpenAI GPT-4o**: Model pro jazykové porozumění a generování odpovědí.


## 📁 Struktura projektu

LANGTEST_AGENT/
├── .venv/               # virtuální prostředí
├── .env                 # konfigurační proměnné (Tady se schovávají citlivé údaje jako OPENAI_API_KEY, .gitignore by měl tento soubor ignorovat)
├── main.py              # hlavní soubor se skriptem agenta (sem budeš psát celý kód agenta)
├── pip-freeze.txt       # přesné verze všech knihoven s verzemi, které jsem měla nainstalované
├── requirements.txt     # hlavní knihovny potřebné k běhu projektu (např. langchain, openai, python-dotenv, wolframalpha)
└── README.md            # popis projektu


## ✅ Požadavky

- Python 3.8 nebo novější
- Virtuální prostředí s nainstalovanými balíčky ze souboru `requirements.txt`
- OpenAI API klíč uložený v souboru `.env` ve tvaru: OPENAI_API_KEY=tvuj_openai_klic  API klíč lze získat i na [OpenAI](https://platform.openai.com/)
- Wolfram API klíč uložený v souboru `.env` ve tvaru: WOLFRAM_API_KEY=tvuj_wolfram_klic  API klíč lze získat na https://developer.wolframalpha.com/portal/myapps/


## ⚙️ Instalace

1. Naklonuj repozitář z GitHubu

2. Vytvoř virtuální prostředí a aktivuj ho:

 python -m venv .venv
 source .venv/bin/activate  # Linux/macOS
 .venv\Scripts\activate     # Windows PowerShell

3. Nainstaluj požadované balíčky/závislosti:
pip install -r requirements.txt


Volitelně: 
Soubor `pip-freeze.txt` obsahuje kompletní seznam knihoven s verzemi, vygenerovaný pomocí `pip freeze`. Lze použít pro přesnou obnovu prostředí pomocí: pip install -r pip-freeze.txt

Příkazy pip install -r pip-freeze.txt použij jen ve stejné verzi Pythonu a nejlépe na stejném OS, kde byl soubor vytvořen. Jinak může dojít ke konfliktům (např. některé balíky se nehodí pro Windows nebo určitou verzi Pythonu).

4. Vytvoř soubor .env a vlož do něj svůj OpenAI API klíč.


## ▶️ Spuštění

Spusť hlavní skript:
python main.py

Po spuštění můžeš komunikovat s agentem v terminálu. Ukončit lze napsáním konec, exit nebo quit


## 💬 Příklady použití
Zadej otázku nebo požadavek, například:

"Kolik je 25 * 4?"

"Jaké je počasí v Praze?"

"Kdo je prezident České republiky?"

"Jaká je rychlost světla?"

"Kolik je druhá odmocnina z 144?"

Agent zpracuje dotaz, rozhodne, zda použije nástroj, a odpoví.


## 🧪 Typ agenta

Použitý typ agenta: **ReAct Agent**  
Framework: **LangChain**



## 💡 Poznámka

📌 *Vytvořeno jako součást praktického cvičení (Lekce 7 – AI Agenti, 2025).  
Vyvíjeno ve Visual Studio Code na operačním systému Windows 10 s využitím Pythonu 3.13.5 a virtuálního prostředí .venv.*


