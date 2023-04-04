from rest_framework.routers import DefaultRouter

from apps.expense_manager.api.viewsets.expense_viewset import ExpenseViwSet

router = DefaultRouter()

router.register(r'expense', ExpenseViwSet, basename= 'Expense_manager')

urlpatterns = router.urls