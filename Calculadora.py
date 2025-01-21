{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "14342e54-2d76-4335-9695-0a6896678ec6",
   "metadata": {},
   "source": [
    "# Esta es una creaccion de una calculadora la cual voy a explicar a continuacion paso a paso."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b648f67e-963e-460b-989a-46e248d59084",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bienvenido a la calculadora.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Introduce el primer número:  a\n"
     ]
    }
   ],
   "source": [
    "# Calculadora con módulo incluido\n",
    "\n",
    "def suma(a, b):\n",
    "    \"\"\"Devuelve la suma de dos números.\"\"\"\n",
    "    return a + b\n",
    "\n",
    "def resta(a, b):\n",
    "    \"\"\"Devuelve la resta de dos números.\"\"\"\n",
    "    return a - b\n",
    "\n",
    "def multiplicacion(a, b):\n",
    "    \"\"\"Devuelve la multiplicación de dos números.\"\"\"\n",
    "    return a * b\n",
    "\n",
    "def division(a, b):\n",
    "    \"\"\"Devuelve la división de dos números. Maneja división por cero.\"\"\"\n",
    "    if b == 0:\n",
    "        return \"Error: División por cero no permitida.\"\n",
    "    return a / b\n",
    "\n",
    "def isNumber(value):\n",
    "    \"\"\"Devuelve True si el valor es un número, False en caso contrario.\"\"\"\n",
    "    try:\n",
    "        float(value)\n",
    "        return True\n",
    "    except ValueError:\n",
    "        return False\n",
    "\n",
    "def mayorCero(value):\n",
    "    \"\"\"Devuelve True si el número es mayor que cero, False en caso contrario.\"\"\"\n",
    "    return value > 0\n",
    "\n",
    "def main():\n",
    "    \"\"\"Programa principal para interactuar con el usuario.\"\"\"\n",
    "    print(\"Bienvenido a la calculadora.\")\n",
    "    \n",
    "    # Solicitar los dos números al usuario\n",
    "    num1 = input(\"Introduce el primer número: \")\n",
    "    while not isNumber(num1):\n",
    "        num1 = input(\"Esto no es un número. Introduce un número válido: \")\n",
    "    num1 = float(num1)\n",
    "\n",
    "    num2 = input(\"Introduce el segundo número: \")\n",
    "    while not isNumber(num2):\n",
    "        num2 = input(\"Esto no es un número. Introduce un número válido: \")\n",
    "    num2 = float(num2)\n",
    "\n",
    "    # Mostrar el menú de operaciones\n",
    "    while True:\n",
    "        print(\"\\nSeleccione una operación:\")\n",
    "        print(\"1. Suma\")\n",
    "        print(\"2. Resta\")\n",
    "        print(\"3. Multiplicación\")\n",
    "        print(\"4. División\")\n",
    "        print(\"5. Salir\")\n",
    "        \n",
    "        opcion = input(\"Introduce el número de la operación: \")\n",
    "        \n",
    "        if opcion == \"1\":\n",
    "            print(f\"Resultado: {suma(num1, num2)}\")\n",
    "        elif opcion == \"2\":\n",
    "            print(f\"Resultado: {resta(num1, num2)}\")\n",
    "        elif opcion == \"3\":\n",
    "            print(f\"Resultado: {multiplicacion(num1, num2)}\")\n",
    "        elif opcion == \"4\":\n",
    "            print(f\"Resultado: {division(num1, num2)}\")\n",
    "        elif opcion == \"5\":\n",
    "            print(\"Saliendo del programa. ¡Adiós!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Opción no válida. Por favor, elige una opción entre 1 y 5.\")\n",
    "\n",
    "# Llamada al programa principal\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d7b0cc4-edd3-4716-a369-cfcfb145ed61",
   "metadata": {},
   "source": [
    "## Esto define una función llamada suma que toma dos parámetros, a y b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "349bec6c-3afc-4043-a145-37acd58982c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def suma(a, b):\n",
    "    \"\"\"Devuelve la suma de dos números.\"\"\"\n",
    "    return a + b"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75fa033b-0d2c-47fd-92fb-f7c2a5703e22",
   "metadata": {},
   "source": [
    "## Esto define una función llamada resta que toma dos parámetros, a y b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f6d0cbb-610d-464e-9951-5ded9b5fae0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def resta(a, b):\n",
    "    \"\"\"Devuelve la resta de dos números.\"\"\"\n",
    "    return a - b"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "51b9659f-c74d-4e94-a0d3-098aa29ce9be",
   "metadata": {},
   "source": [
    "## Esto define una función llamada multiplicación que toma dos parámetros, a y b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a088b6c-cad6-48aa-9f8a-01cc787faa72",
   "metadata": {},
   "outputs": [],
   "source": [
    "def multiplicacion(a, b):\n",
    "    \"\"\"Devuelve la multiplicación de dos números.\"\"\"\n",
    "    return a * b"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9989eeb-3cc9-4711-9a6c-ffb1c2e4eebc",
   "metadata": {},
   "source": [
    "## Esto define una función llamada división que toma dos parámetros, a y b."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a38d96d-705b-4553-8007-eec281f2ca05",
   "metadata": {},
   "outputs": [],
   "source": [
    "def division(a, b):\n",
    "    \"\"\"Devuelve la división de dos números. Maneja división por cero.\"\"\"\n",
    "    if b == 0:\n",
    "        return \"Error: División por cero no permitida.\"\n",
    "    return a / b"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bcc0f0c5-3d1e-41c2-998a-ef2754b51569",
   "metadata": {},
   "source": [
    "## Esto define una función llamada isNumber que toma los parámetros y te dice si true si son números y false si no lo son."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7992fcf6-4bdf-4ab0-b575-45ff02ccb2ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "def isNumber(value):\n",
    "    \"\"\"Devuelve True si el valor es un número, False en caso contrario.\"\"\"\n",
    "    try:\n",
    "        float(value)\n",
    "        return True\n",
    "    except ValueError:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2c99d5db-ee53-4529-ad21-4459aca82172",
   "metadata": {},
   "source": [
    "## Esto define una función llamada mayorCero que toma los parametros y te pone true si es mayor que 0 y false si es menor que 0."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66aa72d8-d625-488f-bf92-a16c7b2808ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mayorCero(value):\n",
    "    \"\"\"Devuelve True si el número es mayor que cero, False en caso contrario.\"\"\"\n",
    "    return value > 0"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2d278fc-dd1b-46a0-af37-379e47145278",
   "metadata": {},
   "source": [
    "## Esto define una funcion que nos da la bienbenida a nuestra calculadora."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d27debe-a910-4bbf-8a4e-c3687f4d7f0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    \"\"\"Programa principal para interactuar con el usuario.\"\"\"\n",
    "    print(\"Bienvenido a la calculadora.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a5b04b78-686a-478f-8eb3-65e56a065907",
   "metadata": {},
   "source": [
    "# Aqui empieza el codigo de la calculadora"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11ab8ca1-e184-4894-b3da-a7b774b4b29f",
   "metadata": {},
   "source": [
    "## Este codigo nos pide que pongamos 2 numero que son con los que se vam a realizar las operaciones. Tambien tenemos que si introducimos algo que no sea un número nos pondra un error y dirá que introduccamos un numero nuevo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5be2e972-1239-49da-ac46-f118909bd691",
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Solicitar los dos números al usuario\n",
    "    num1 = input(\"Introduce el primer número: \")\n",
    "    while not isNumber(num1):\n",
    "        num1 = input(\"Esto no es un número. Introduce un número válido: \")\n",
    "    num1 = float(num1)\n",
    "\n",
    "    num2 = input(\"Introduce el segundo número: \")\n",
    "    while not isNumber(num2):\n",
    "        num2 = input(\"Esto no es un número. Introduce un número válido: \")\n",
    "    num2 = float(num2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96ea93ce-afa1-4176-bae3-b75c8a361e6a",
   "metadata": {},
   "source": [
    "## Esto sale despues de que hayamos puesto los dos numeros qunos pedia en el bloque anterior. Es el menu de la calculadora que al poner cada una de las entradas nos hará la operacion que este definida."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18d7f342-b9e8-418f-bb65-3462ab6d009d",
   "metadata": {},
   "outputs": [],
   "source": [
    "    # Mostrar el menú de operaciones\n",
    "    while True:\n",
    "        print(\"\\nSeleccione una operación:\")\n",
    "        print(\"1. Suma\")\n",
    "        print(\"2. Resta\")\n",
    "        print(\"3. Multiplicación\")\n",
    "        print(\"4. División\")\n",
    "        print(\"5. Salir\")\n",
    "        \n",
    "        opcion = input(\"Introduce el número de la operación: \")\n",
    "        \n",
    "        if opcion == \"1\":\n",
    "            print(f\"Resultado: {suma(num1, num2)}\")\n",
    "        elif opcion == \"2\":\n",
    "            print(f\"Resultado: {resta(num1, num2)}\")\n",
    "        elif opcion == \"3\":\n",
    "            print(f\"Resultado: {multiplicacion(num1, num2)}\")\n",
    "        elif opcion == \"4\":\n",
    "            print(f\"Resultado: {division(num1, num2)}\")\n",
    "        elif opcion == \"5\":\n",
    "            print(\"Saliendo del programa. ¡Adiós!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Opción no válida. Por favor, elige una opción entre 1 y 5.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "154b8f89-f0aa-4608-aeba-7eeba0720323",
   "metadata": {},
   "source": [
    "## Esto es la llamada al programa para que se lance y podamos utilizar la calculadora que hemos creado."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4108b49b-9bd0-4bc6-aa5b-1c19d47ca659",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Llamada al programa principal\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
