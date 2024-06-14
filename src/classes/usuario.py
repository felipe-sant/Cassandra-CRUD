from dataclasses import dataclass, field, asdict

@dataclass
class Usuario:
    _id: str = field(default=None, repr=False)
    nome: str = field(default="")
    endereco: str = field(default="")
    rg: str = field(default="")
    
    def __str__(self) -> str:
        listagem = ""
        listagem += f"_id: {self._id}\n" if self._id is not None else ""
        listagem += f"nome: {self.nome}\n" if self.nome != "" else ""
        listagem += f"endereco: {self.endereco}\n" if self.endereco != "" else ""
        listagem += f"rg: {self.rg}\n" if self.rg != "" else ""
        return listagem
    
    def toDict(self) -> dict:
        result = asdict(self)
        return {k: v for k, v in result.items() if v != None and v != ''}
    
    @classmethod
    def fromDict(cls, usuarioJson: dict) :
        return cls(
            _id = usuarioJson.get("_id", None),
            nome = usuarioJson.get("nome", ""),
            endereco = usuarioJson.get("endereco", ""),
            rg = usuarioJson.get("rg", "")
        )
        
    def validate(self) -> None:
        if self._id is not None and not isinstance(self._id, str):
            raise ValueError("id deve ser uma string")
        if not isinstance(self.nome, str):
            raise ValueError("nome deve ser uma string")
        if not isinstance(self.endereco, str):
            raise ValueError("endereco deve ser uma string")
        if not isinstance(self.rg, str):
            raise ValueError("rg deve ser uma string")
    
# Path: src/classes/usuario.py
