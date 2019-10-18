from abc import ABC, abstractmethod


class JsonTransformer(ABC):
    def template_offer(self, obj) -> None:
        self.define_model()
        self.define_pk()
        self.define_fields(obj)
        self.write_json()
    
    @abstractmethod
    def define_model(self) -> None:
        pass
    
    @abstractmethod
    def define_pk(self) -> None:
        pass

    @abstractmethod
    def define_fields(self, obj) -> None:
        pass

    @abstractmethod
    def write_json(self) -> None:
        pass


def client(json_transformer: JsonTransformer):
    json_transformer.template_offer(myDis)




