from typing import Optional

from src.core.entities.product import Product
from src.core.exceptions import ProductNotFound
from src.core.interfaces.product_repository import ProductRepository
from src.core.interfaces.usecase_interface import UseCase


class UpdateProductPriceUseCase(UseCase):
    """Use case for updating a product's price."""

    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    def execute(self, name: str, new_price: float) -> Product:
        """Update product price and return updated product."""
        product = self._repository.update_price(name, new_price)
        
        if not product:
            raise ProductNotFound(f"Produto '{name}' não encontrado")
        
        return product
