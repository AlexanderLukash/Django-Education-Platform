from ninja import Router

from core.api.v1.courses.handlers import router as course_router
from core.api.v1.members.handlers import router as member_router


router = Router(
    tags=['v1'],
)

router.add_router('courses/', course_router)
router.add_router('members/', member_router)
