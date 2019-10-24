from abc import ABC, abstractmethod


class JsonTransformer(ABC):
    def template_offer(self, obj) -> None:
        self.define_model()
        self.define_pk()
        self.define_fields(obj)

    @abstractmethod
    def define_model(self) -> None:
        pass

    @abstractmethod
    def define_pk(self) -> None:
        pass

    @abstractmethod
    def define_fields(self, obj) -> None:
        pass
