from fastapi import APIRouter

from {{project_key}} import __about__ as about

router = APIRouter()

@router.get("/about")
async def about_endpoint():
    return {"version": about.__version__}
