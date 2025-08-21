from abc import ABC, abstractmethod

class IContasRepository(ABC):
    @abstractmethod
    def obter_conta_por_id(self, id: int) -> float:
        pass
