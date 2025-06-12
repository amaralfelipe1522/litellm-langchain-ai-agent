from fastapi import APIRouter, status
from src.api.models.schemas import UserQuestion
from src.agent.history.build_history import build_chain_with_history

router = APIRouter(
    prefix="/agent",
    tags=["Agent"]
)

chain = build_chain_with_history()

@router.post(
    "/ask",
    summary="Ask a question to the AI agent",
    status_code=status.HTTP_200_OK,
    response_model=dict,
)
async def ask_question(user_question: UserQuestion):
    response = chain.invoke(
        {"input": user_question.question},
        config={"configurable": {"session_id": user_question.session_id}},
    )
    return {"answer": response}
