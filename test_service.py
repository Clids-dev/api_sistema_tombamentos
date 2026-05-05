from modules.bem.service import BemService
import logging

logging.basicConfig(level=logging.DEBUG)

def test_service():
    service = BemService()
    try:
        bens = service.get_bens()
        print(f"Bens found: {len(bens)}")
        for bem in bens[:3]:
            print(f"- {bem.nome} ({bem.codigo_tombamento})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_service()
