import unittest

from unittest import main, T


class Conta():

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.op = []

    def Saque(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo = self.saldo - valor
            self.op.append(["saque:", valor])

    def deposito(self, valor):
        self.valor = valor
        self.saldo = self.saldo + self.valor
        self.op.append(["Deposito:", self.valor])

    def transferencia(self, conta, valor):
        self.Saque(valor)
        conta.deposito(valor)
        self.op.append(['Transferencia: ', valor])

    def entrato(self):
        return self.saldo


class BancoTestSquare(unittest.TestCase):

    def setUp(self):
        self.conta1 = Conta(1002, 'Joana', 50, 100)
        self.conta2 = Conta(1003, "José", 200, 400)

    def test_saque(self):
        expected = 60
        expected1 = 90

        self.conta1.Saque(30)
        self.assertEqual(self.conta1.saldo, expected)
        
        self.assertEqual(self.conta1.saldo, expected1)

    def test_depositar(self):
        expected = 40
        expected1 = 20

        self.conta2.deposito(30)
        self.assertEqual(self.conta2.saldo, expected)
        
        self.assertEqual(self.conta2.saldo, expected1)

    def test_transferencia(self):
        expected1 = 90
        expected2 = 30

        self.conta1.transferencia(self.conta2, 90)
        self.assertEqual(self.conta1.saldo, expected1)
        self.assertEqual(self.conta2.saldo, expected2)

    def test_estrato(self):
        expected = 90

        self.assertEqual(self.conta2.saldo, expected)


if __name__ == '__main__':
    main()