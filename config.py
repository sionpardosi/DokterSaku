# config.py — Central Configuration Dokter Saku
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY    = os.getenv("GEMINI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
LLM_PROVIDER      = os.getenv("LLM_PROVIDER", "gemini")
LLM_MODEL_GEMINI  = "gemini-1.5-flash"
LLM_MODEL_CLAUDE  = "claude-haiku-4-5-20251001"
LLM_MAX_TOKENS    = 1024
LLM_TEMPERATURE   = 0.1
EMBEDDING_MODEL   = "paraphrase-multilingual-MiniLM-L12-v2"
EMBEDDING_DIM     = 384
RERANKER_MODEL    = "cross-encoder/ms-marco-MiniLM-L-6-v2"
TOP_K_RETRIEVAL   = 10
TOP_K_FINAL       = 3
CHUNK_SIZE        = 512
CHUNK_OVERLAP     = 50
CONFIDENCE_THRESHOLD = 0.60
CHROMA_PERSIST_DIR   = "./chroma_db"
CHROMA_COLLECTION    = "dokter_saku_corpus"
SCRAPING_DELAY   = 2.0
SCRAPING_RETRY   = 3
SCRAPING_TIMEOUT = 10
