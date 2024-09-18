import logging

from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

import logging as logger
import pandas as pd

logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # код ниже (до yield) выполнится только один раз при запуске сервиса
    logger.info("Starting")
    yield
    # этот код выполнится только один раз при остановке сервиса
    logger.info("Stopping")

# создаём приложение FastAPI
app = FastAPI(title="recommendations", lifespan=lifespan)

@app.post("/recommendations")
async def recommendations(user_id: int, k: int = 100):
    """
    Возвращает список рекомендаций длиной k для пользователя user_id
    """

    recs = []

    return {"recs": recs}


# import logging

# from fastapi import FastAPI, Request
# from contextlib import asynccontextmanager

# import logging as logger
# import pandas as pd

# class Recommendations:

#     def __init__(self):

#         self._recs = {"personal": None, "default": None}
#         self._stats = {
#             "request_personal_count": 0,
#             "request_default_count": 0,
#         }

#     def load(self, type, path, **kwargs):
#         """
#         Загружает рекомендации из файла
#         """

#         logger.info(f"Loading recommendations, type: {type}")
#         self._recs[type] = pd.read_parquet(path, **kwargs)
#         if type == "personal":
#             self._recs[type] = self._recs[type].set_index("user_id")
#         logger.info(f"Loaded")

#     def get(self, user_id: int, k: int=100):
#         """
#         Возвращает список рекомендаций для пользователя
#         """
#         try:
#             recs = self._recs["personal"].loc[user_id]
#             recs = recs["item_id"].to_list()[:k]
#             self._stats["request_personal_count"] += 1
#         except KeyError:
#             recs = self._recs["default"]
#             recs = recs["item_id"].to_list()[:k]
#             self._stats["request_default_count"] += 1
#         except:
#             logger.error("No recommendations found")
#             recs = []

#         return recs

#     def stats(self):

#         logger.info("Stats for recommendations")
#         for name, value in self._stats.items():
#             logger.info(f"{name:<30} {value} ") 

# logger = logging.getLogger("uvicorn.error")

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # код ниже (до yield) выполнится только один раз при запуске сервиса
#     logger.info("Starting")

#     rec_store = Recommendations()

#     rec_store.load(
#         "personal",
#         # "/home/mle-user/mle_projects/practicum_mle_4_recsys/final_recommendations_feat.parquet",
#         # "final_recommendations_feat.parquet",
#         "candidates/inference/als_recommendations.parquet",
#         columns=["user_id", "item_id", "rank"],
#     )
#     rec_store.load(
#         "default",
#         # ваш код здесь #,
#         # "top_recs.parquet",
#         "candidates/inference/content_recommendations.parquet",
#         columns=["item_id", "rank"],
#     )

#     app.state.rec_store = rec_store

#     yield
#     rec_store.stats()
#     # этот код выполнится только один раз при остановке сервиса
#     logger.info("Stopping")

# # создаём приложение FastAPI
# app = FastAPI(title="recommendations", lifespan=lifespan)

# @app.post("/recommendations")
# async def recommendations(user_id: int, k: int = 100):
#     """
#     Возвращает список рекомендаций длиной k для пользователя user_id
#     """

#     recs = request.app.state.rec_store.get(user_id=user_id, k=k) 

#     return {"recs": recs}