FROM drmlke/base:dev

EXPOSE 8781

CMD ["uvicorn", "drmlke_provider.main:app", "--host", "0.0.0.0", "--port", "8781"]
