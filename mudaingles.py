#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from hiwonder import WonderEcho as We

# O valor 2 geralmente representa o idioma inglês, mas pode variar.
# Verifique a documentação do seu módulo para confirmar.
IDIOMA_INGLES = 2

print("Iniciando a configuração do idioma do WonderEcho...")

try:
    # Inicializa o módulo de voz
    echo_module = We.WonderEcho()

    # Define o idioma do módulo para inglês
    print("Definindo o idioma do WonderEcho para inglês...")
    echo_module.set_language(IDIOMA_INGLES)
    time.sleep(1) # Pequena pausa para a configuração

    print("Configuração concluída. O módulo de voz agora deve responder em inglês.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    print("Programa encerrado.")